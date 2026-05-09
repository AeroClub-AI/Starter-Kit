# 📂 Examples Collection | مجموعه‌ی مثال‌های اجرایی

![Status](https://img.shields.io/badge/status-ready-green.svg)
![Offline](https://img.shields.io/badge/offline-friendly-yes-blue.svg)

---

## 🌍 English
This folder contains lightweight, self-contained aerospace & AI projects designed for Iranian students. Each example runs independently, includes its own `README.md`, configuration file, and requirements. No external datasets or constant internet required.  
🔹 *Pick one, clone it, run it, modify it.*

## 🇮🇷 فارسی
این پوشه شامل پروژه‌های سبک و مستقل هوافضا و هوش مصنوعیه که برای دانشجویان ایرانی طراحی شده. هر مثال به صورت جداگانه اجرا می‌شه، `README`، فایل تنظیمات و لیست وابستگی‌های خودش رو داره. بدون نیاز به اینترنت دائمی یا دیتاست خارجی.  
🔹 *یکی رو انتخاب کن، اجرا کن، تغییر بده، یاد بگیر.*

---

## 🗺️ Project Index / فهرست پروژه‌ها

| Example | Focus Area | Difficulty | Description |
|:---|:---|:---:|:---|
| 🛰️ [`orbit-prediction/`](orbit-prediction/) | Orbital Mechanics | 🟢 Beginner | Keplerian propagator, ECI coordinates, 3D visualization |
| 📊 [`satellite-ml-mini/`](satellite-ml-mini/) | AI & Telemetry | 🟡 Intermediate | Synthetic data generation, Isolation Forest anomaly detection |
| 🎯 [`pid-attitude-sim/`](pid-attitude-sim/) | GNC & Control | 🟡 Intermediate | Single-axis attitude control, actuator saturation, anti-windup |

---

## 🚀 How to Run Any Example
```bash
# 1. Navigate to the example folder
cd orbit-prediction  # or satellite-ml-mini, pid-attitude-sim

# 2. Install dependencies (recommended: use venv or conda)
pip install -r requirements.txt

# 3. Run
python main.py
```
✅ Each example automatically creates an `output/` folder with CSV data and plots.

---

## 💡 Pro Tips / نکات کاربردی
- 🔧 **تغییر پارامترها:** فقط فایل `config.yaml` رو ویرایش کن و دوباره `python main.py` بزن. نیازی به تغییر کد نیست.
- 💾 **کار آفلاین:** همه‌ی مثال‌ها ۱۰۰٪ لوکال اجرا می‌شن. برای مدیریت اینترنت محدود، راهنمای `../docs/Offline.md` رو بخون.
- 🌱 **اضافه کردن پروژه‌ی خودت:** از قالب `../templates/PROJECT_README.md` استفاده کن و یه Pull Request بزن.
- 🐍 **محیط مجازی:** پیشنهاد می‌کنیم برای جلوگیری از تداخل کتابخانه‌ها، از `python -m venv .venv` یا `conda` استفاده کنید.

---

<p align="center">
  <sub>Part of <a href="https://github.com/AeroClub-AI/Starter-Kit">AeroClub-AI Starter-Kit</a> | Built for Iranian Students 🛰️</sub>
</p>
```