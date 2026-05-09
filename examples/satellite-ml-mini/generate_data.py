import numpy as np
import pandas as pd
import yaml
import os

def generate_telemetry(cfg):
    n = cfg['data']['n_samples']
    t = np.arange(n)
    
    # Realistic-ish periodic signals + noise
    temp = 20 + 5 * np.sin(t * 0.01) + np.random.normal(0, cfg['data']['noise_std'], n)
    volt = 12.0 + 0.5 * np.cos(t * 0.005) + np.random.normal(0, cfg['data']['noise_std'] * 2, n)
    rpm  = 3000 + 100 * np.sin(t * 0.008) + np.random.normal(0, cfg['data']['noise_std'] * 50, n)
    
    df = pd.DataFrame({'time': t, 'temperature': temp, 'voltage': volt, 'rpm': rpm})
    df['is_anomaly'] = 0
    
    # Inject anomalies (spikes/drops)
    n_anom = int(n * cfg['data']['anomaly_fraction'])
    idx = np.random.choice(n, n_anom, replace=False)
    for i in idx:
        feat = np.random.choice(['temperature', 'voltage', 'rpm'])
        df.loc[i, feat] += np.random.choice([-1, 1]) * np.random.uniform(5, 15)
        df.loc[i, 'is_anomaly'] = 1
        
    os.makedirs(os.path.dirname(cfg['data']['output_path']), exist_ok=True)
    df.to_csv(cfg['data']['output_path'], index=False)
    print(f"✅ Generated {n} samples with {n_anom} anomalies.")