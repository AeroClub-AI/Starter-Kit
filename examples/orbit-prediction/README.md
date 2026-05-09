# 🛰️ Orbit Prediction (Keplerian) | پیش‌بینی مدار دو جسمی

![Status](https://img.shields.io/badge/status-ready-green.svg)
![Language](https://img.shields.io/badge/language-Python-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌍 English
A lightweight, offline-friendly Python script that propagates a satellite orbit using the **Two-Body Problem (Keplerian model)**. It solves Kepler's equation numerically, converts perifocal coordinates to ECI, and generates a 3D plot with Earth reference. Perfect for students learning orbital mechanics or prototyping CubeSat trajectories.

## 🇮🇷 فارسی
یه اسکریپت سبک پایتون برای پیش‌بینی مدار ماهواره با استفاده از **مسئله‌ی دو جسمی (مدل کپلری)**. این کد معادله‌ی کپلر رو عددی حل می‌کنه، مختصات رو به چارچوب ECI تبدیل می‌کنه و نمودار سه‌بعدی مدار رو همراه با کره‌ی زمین رسم می‌کنه. عالی برای یادگیری مکانیک مداری یا شبیه‌سازی اولیه‌ی مأموریت‌های کیوب‌ست.

## ⚙️ Requirements
| Tool | Version |
|:---|:---|
| Python | ≥3.8 |
| NumPy | ≥1.21 |
| Matplotlib | ≥3.5 |
| PyYAML | ≥6.0 |

## 🚀 Usage
```bash
pip install -r requirements.txt
python main.py
```
✅ Outputs: `output/trajectory.csv` (data), `output/orbit_plot.png` (visualization)

## 📁 Structure
- `main.py` — Core propagator & plotter
- `config.yaml` — Orbital parameters (editable)
- `output/` — Generated results (auto-created)

## 🤝 Contributing
- Found a bug? Open an issue with `[bug]` tag.
- Want to add perturbations (J2, drag)? Fork → Branch → PR.
- Need help? Check `docs/Offline.md` in the main repo.

---
<p align="center">
  <sub>Part of <a href="https://github.com/AeroClub-AI/Starter-Kit">AeroClub-AI Starter-Kit</a> | Built for Iranian Students 🛰️</sub>
</p>
```