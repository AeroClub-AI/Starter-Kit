import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import yaml
import os
import json
from generate_data import generate_telemetry

def main():
    cfg = yaml.safe_load(open('config.yaml'))
    data_path = cfg['data']['output_path']
    
    # Auto-generate if missing
    if not os.path.exists(data_path):
        generate_telemetry(cfg)
        
    df = pd.read_csv(data_path)
    features = ['temperature', 'voltage', 'rpm']
    X = df[features]
    y_true = df['is_anomaly']
    
    # Scale
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Train
    clf = IsolationForest(contamination=cfg['model']['contamination'],
                          random_state=cfg['model']['random_state'])
    clf.fit(X_scaled)
    y_pred = (clf.predict(X_scaled) == -1).astype(int)
    
    # Metrics
    print("\n📊 Classification Report:")
    print(classification_report(y_true, y_pred, target_names=['Normal', 'Anomaly']))
    
    # Save
    os.makedirs(cfg['output']['dir'], exist_ok=True)
    metrics = classification_report(y_true, y_pred, output_dict=True)
    with open(os.path.join(cfg['output']['dir'], cfg['output']['metrics_file']), 'w') as f:
        json.dump(metrics, f, indent=2)
        
    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['time'], df['temperature'], c=y_pred, cmap='coolwarm', alpha=0.7, s=20)
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (°C)')
    plt.title('Anomaly Detection in Satellite Telemetry')
    plt.colorbar(label='Prediction (0=Normal, 1=Anomaly)')
    plt.savefig(os.path.join(cfg['output']['dir'], cfg['output']['plot_file']), dpi=150)
    print(f"\n✅ Results saved to {cfg['output']['dir']}")

if __name__ == "__main__":
    print("🛰️ Starting Satellite ML Mini-Project...")
    main()