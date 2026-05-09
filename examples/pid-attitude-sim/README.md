# 🎯 PID Attitude Control Simulation | شبیه‌سازی کنترل وضعیت با PID

![Status](https://img.shields.io/badge/status-ready-green.svg)
![Language](https://img.shields.io/badge/language-Python-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌍 English
A lightweight simulation of a **single-axis rotational system** (e.g., satellite wheel or drone pitch) controlled by a **PID controller**. Includes actuator saturation, Euler integration, and real-time response plotting. Fully offline, zero external dependencies. Perfect for learning GNC fundamentals, tuning PID gains, or prototyping attitude control logic.

## 🇮🇷 فارسی
یه شبیه‌سازی سبک از **سیستم چرخشی تک‌محوره** (مثل چرخ عکس‌العمل ماهواره یا محور pitch پهپاد) که با **کنترل‌کننده‌ی PID** مدیریت می‌شه. شامل محدودیت گشتاور عملگر، انتگرال‌گیری اویلر و رسم پاسخ بلادرنگ. کاملاً آفلاین، بدون وابستگی خارجی. عالی برای یادگیری مبانی هدایت و کنترل (GNC)، تنظیم گین‌های PID یا ساخت پروتوتایپ منطق کنترل وضعیت.

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
✅ Outputs: `output/attitude_data.csv`, `output/pid_response.png`

## 📁 Structure
- `main.py` — Dynamics solver, PID loop, plotting & CSV export
- `config.yaml` — Tunable physics, PID gains, simulation params
- `output/` — Generated time-history & visualization

## 🛠️ How to Tune
- `Kp` ↑ → Faster response, but may overshoot
- `Ki` ↑ → Eliminates steady-state error, but can cause oscillation
- `Kd` ↑ → Dampens overshoot, sensitive to noise
- ⚠️ Keep `max_torque` realistic to see saturation effects!

## 🤝 Contributing
- Want to add disturbance rejection or quaternions? Fork → Branch → PR.
- Try replacing Euler integration with RK4 for higher accuracy.
- Offline? Works 100% locally. See `docs/Offline.md`.

---
<p align="center">
  <sub>Part of <a href="https://github.com/AeroClub-AI/Starter-Kit">AeroClub-AI Starter-Kit</a> | Built for Iranian Students 🛰️</sub>
</p>
```