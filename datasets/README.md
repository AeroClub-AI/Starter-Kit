# 📊 Aerospace & AI Datasets | مجموعه‌ی داده‌های هوافضا و هوش مصنوعی

![Open Data](https://img.shields.io/badge/open-data-curated-green.svg)
![Offline Ready](https://img.shields.io/badge/offline-friendly-yes-blue.svg)
![Citation Required](https://img.shields.io/badge/citation-required-yes-orange.svg)

---

## 🌍 English
This folder **does not host heavy datasets directly**. To keep the repository lightweight and git-friendly, we provide:
1. ✅ Curated links to reputable, open-access aerospace & space-AI datasets
2. 📁 `sample/` folder with tiny test files for quick offline development
3. 📘 Clear guidelines on downloading, citing, and integrating external data into your projects.

## 🇮🇷 فارسی
این پوشه **داده‌های حجیم را مستقیماً هاست نمی‌کند**. برای سبک نگه داشتن مخزن و سازگاری با گیت، اینجا فقط موارد زیر قرار داره:
۱. ✅ لینک‌های انتخاب‌شده به داده‌های معتبر و متن‌باز هوافضا و هوش مصنوعی فضایی
۲. 📁 پوشه‌ی `sample/` شامل فایل‌های تستی بسیار سبک برای توسعه‌ی آفلاین
۳. 📘 راهنمای واضح برای دانلود، استناد و اتصال داده‌های خارجی به پروژه‌هاتون.

---

## 🌐 Curated External Datasets / منابع داده‌ی معتبر

| Category | Source | Description | Direct Link |
|:---|:---|:---|:---|
| 🛰️ **Orbital & TLE** | Celestrak / Space-Track | Satellite catalogs, TLE files, maneuver logs | [celestrak.org](https://celestrak.org/) |
| 🌍 **Earth Observation** | ESA Copernicus Open Access | Sentinel-1/2/5P imagery, atmospheric & land data | [scihub.copernicus.eu](https://scihub.copernicus.eu/) |
| 🌍 **Earth Observation** | NASA Earthdata Search | MODIS, Landsat, VIIRS, climate & topography | [earthdata.nasa.gov](https://earthdata.nasa.gov/) |
| 🤖 **Space AI / ML** | NASA Open Source AI | Labeled telemetry, anomaly datasets, ML pipelines | [github.com/nasa](https://github.com/nasa) |
| 🌬️ **CFD & Aero** | NASA CFD Validation Workshop | Experimental & numerical airfoil/wing datasets | [cfdval.larc.nasa.gov](https://cfdval.larc.nasa.gov/) |
| 🏗️ **Materials** | NIST Materials Data Repository | Composite properties, fatigue curves, thermal data | [materialsdata.nist.gov](https://materialsdata.nist.gov/) |

> 💡 **Tip:** Most portals support `wget -c <url>` or `curl -C -` for resume capability. Use university proxies or download managers for stable transfers.

---

## 📁 Folder Structure / ساختار پوشه
```
datasets/
├── README.md                 # این فایل
└── sample/                   # داده‌های تستی سبک (<5MB total)
    ├── orbit_tle_sample.txt  # نمونه‌ی TLE برای تست propagator
    ├── telemetry_100rows.csv # ۱۰۰ سطر تله‌متری مصنوعی
    └── image_patch_100x100.png # پچ کوچک تصویر ماهواره‌ای
```

---

## 🛠️ How to Use (Iran Context) / راهنمای استفاده در شرایط ایران
1. **دانلود هوشمند:** از `wget -c` یا نرم‌افزارهای دانلود ایرانی/خارجی با قابلیت Resume استفاده کن.
2. **ذخیره‌ی محلی:** داده‌ها رو توی یه درایو جداگانه یا هارد اکسترنال نگه دار. مسیر رو توی `config.yaml` پروژه‌ات تنظیم کن (`data_path: "D:/AeroData/sentinel2/"`).
3. **استفاده در کد:** همیشه از مسیرهای نسبی یا متغیرهای محیطی استفاده کن تا کد روی لپ‌تاپ استادت یا سیستم دوستت هم بدون خطا اجرا بشه.
4. **مدیریت نسخه:** داده‌های حجیم رو با گیت آپلود نکن. فقط لینک + `sample/` رو کامیت کن. برای آرشیو بلندمدت از Zenodo یا OSF استفاده کن و DOI بگیر.

---

## ⚖️ Licensing & Citation / لایسنس و استناد
- 🔹 هر دیتاست لایسنس مخصوص خودش رو داره (CC-BY, MIT, Public Domain, ESA EULA).
- 📚 **حتماً** در `README.md` پروژه‌ات و مقالات، منبع داده رو با فرمت زیر ذکر کن:
  ```
  Dataset: [Name], [Provider], [Year], [URL/DOI]
  License: [License Type]
  ```
- 🚫 از انتشار داده‌های طبقه‌بندی‌شده، نتایج آزمایشگاهی محدودشده یا تصاویر با وضوح تجاری/نظامی خودداری کن.
- ✅ اگر از داده‌ی عمومی استفاده کردی، یه خط تشکر در خروجی یا README اضافه کن: `Data courtesy of [Provider].`

---

## 🤝 Add a New Dataset / اضافه کردن داده‌ی جدید
1. لینک معتبر و پایدار رو پیدا کن (ترجیحاً دولتی/آکادمیک/متن‌باز).
2. یه فایل `sample/` بسیار سبک (<2MB) ازش استخراج کن.
3. این فایل رو به `sample/` اضافه کن و توضیح کوتاهی در این README بنویس.
4. یه Pull Request با تگ `[dataset]` باز کن. تیم نگهدارنده لینک و لایسنس رو بررسی می‌کنه.

---
<p align="center">
  <sub>Part of <a href="https://github.com/AeroClub-AI/Starter-Kit">AeroClub-AI Starter-Kit</a> | Data is the fuel of aerospace research 🛰️📊</sub>
</p>
```