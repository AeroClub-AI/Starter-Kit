# 🛰️ Satellite Telemetry Anomaly Detection | تشخیص ناهنجاری در تله‌متری ماهواره

![Status](https://img.shields.io/badge/status-ready-green.svg)
![Language](https://img.shields.io/badge/language-Python-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌍 English
A lightweight ML pipeline that generates synthetic satellite telemetry (temperature, voltage, RPM) and trains an **Isolation Forest** model to detect anomalies. Fully offline, zero external datasets required. Ideal for learning time-series anomaly detection in space systems or prototyping on-board health monitoring.

## 🇮🇷 فارسی
یه پایپ‌لاین سبک یادگیری ماشین که داده‌ی تله‌متری مصنوعی ماهواره (دما، ولتاژ، دور موتور) تولید می‌کنه و یه مدل **Isolation Forest** رو برای تشخیص ناهنجاری آموزش می‌ده. کاملاً آفلاین، بدون نیاز به دانلود دیتاست خارجی. عالی برای یادگیری تشخیص ناهنجاری در سری‌های زمانی فضایی یا ساخت نمونه‌ی اولیه‌ی پایش سلامت ماهواره.

## ⚙️ Requirements
| Tool | Version |
|:---|:---|
| Python | ≥3.8 |
| NumPy | ≥1.21 |
| Pandas | ≥1.3 |
| scikit-learn | ≥1.0 |
| Matplotlib | ≥3.5 |
| PyYAML | ≥6.0 |

## 🚀 Usage
```bash
pip install -r requirements.txt
python main.py
```
✅ Outputs: `data/telemetry.csv`, `output/metrics.json`, `output/anomaly_plot.png`

## 📁 Structure
- `generate_data.py` — Synthetic telemetry generator with injected anomalies
- `main.py` — ML pipeline: load → scale → train → predict → plot
- `config.yaml` — Tunable parameters for data & model
- `output/` — Generated results & visualizations

## 🤝 Contributing
- Want to test another model (LSTM, SVM, Autoencoder)? Fork → Branch → PR.
- Need real telemetry data? Check `datasets/` in the main repo for open ESA/NASA links.
- Offline? Works 100% locally. See `docs/Offline.md`.

---
<p align="center">
  <sub>Part of <a href="https://github.com/AeroClub-AI/Starter-Kit">AeroClub-AI Starter-Kit</a> | Built for Iranian Students 🛰️</sub>
</p>
```

---