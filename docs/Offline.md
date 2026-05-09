# 📶 Offline Git Guide | راهنمای کار آفلاین با گیت

![Offline Ready](https://img.shields.io/badge/offline-ready-yes-green.svg)
![Bandwidth Friendly](https://img.shields.io/badge/bandwidth-friendly-optimized-blue.svg)

---

## 🌍 English
Git was built for distributed work. You **don't need constant internet** to use it professionally. This guide shows you how to clone once, work offline for weeks, sync periodically, and save bandwidth using modern Git features.

## 🇮🇷 فارسی
گیت ذاتاً برای کار غیرمتمرکز طراحی شده. برای استفاده‌ی حرفه‌ای **نیازی به اینترنت همیشگی نداری**. این راهنما بهت یاد می‌ده چطور یک‌بار دانلود کنی، هفته‌ها آفلاین کار کنی، هر وقت تونستی سینک کنی و با ترفندهای جدید گیت، حجم اینترنتت رو هوشمندانه مدیریت کنی.

---

## 📦 ۱. دانلود یک‌باره (Shallow Clone)
به جای دانلود کل تاریخچه‌ی پروژه (که گاهی چند گیگابایت می‌شه)، فقط آخرین نسخه رو بگیر:
```bash
git clone --depth 1 https://github.com/Aerospace-IR/Starter-Kit.git
cd Starter-Kit
```
✅ `--depth 1` فقط کامیت آخر رو دانلود می‌کنه. سرعت ۳ تا ۵ برابر بیشتر، حجم بسیار کمتر.

---

## 💻 ۲. کار کاملاً آفلاین (Local Workflow)
بعد از کلون کردن، اینترنت رو می‌تونی خاموش کنی. گیت تمام عملیات رو به صورت محلی انجام می‌ده:
```bash
# ساخت شاخه‌ی جدید برای تغییراتت
git checkout -b feat/my-project

# اضافه کردن فایل‌ها و ثبت تغییرات
git add .
git commit -m "feat: add attitude control simulation"

# می‌تونی ده‌ها بار این کار رو تکرار کنی. همه‌چیز روی لپ‌تاپته.
```
🔹 کامیت‌ها تا زمانی که `push` نزنی، فقط روی سیستم خودت می‌مونن. کاملاً امن و آفلاین.

---

## 🔄 ۳. همگام‌سازی دوره‌ای (Periodic Sync)
هر وقت به اینترنت پایدار دسترسی پیدا کردی:
```bash
# اول تغییرات بقیه رو بگیر و ادغام کن
git fetch origin
git merge origin/main

# یا یک‌جا:
git pull origin main

# بعد شاخه‌ی خودت رو آپلود کن
git push origin feat/my-project
```
⚠️ همیشه قبل از `push`، `pull` بزن تا با تغییرات جدید تداخل ایجاد نشه.

---

## 🎒 ۴. صرفه‌جویی در حجم با Sparse Checkout
اگر فقط به یه بخش خاص (مثلاً `examples/`) نیاز داری، کل ریپازیتوری رو دانلود نکن:
```bash
git init my-workspace
cd my-workspace
git remote add origin https://github.com/Aerospace-IR/Starter-Kit.git
git config core.sparseCheckout true

# فقط پوشه‌های مورد نظرت رو مشخص کن
git sparse-checkout init --cone
git sparse-checkout set examples/ docs/

# حالا فقط همون پوشه‌ها دانلود می‌شن
git pull origin main --depth=1
```
📉 این روش حجم دانلود رو تا ۷۰-۸۰٪ کاهش می‌ده. عالی برای اینترنت محدود یا موبایل.

---

## 🗜️ ۵. مدیریت فایل‌های سنگین و دیتاست‌ها
گیت برای کد ساخته شده، نه برای فایل‌های حجیم. قوانین طلایی:
- ❌ فایل‌های `>10MB` رو مستقیم `commit` نکن.
- ✅ از `Git LFS` برای مدل‌های ML یا دیتاست‌های ضروری استفاده کن.
- 🔗 بهتره دیتاست‌ها رو روی پلتفرم‌هایی مثل Zenodo، Kaggle یا Google Drive آپلود کنی و لینک رو توی `datasets/README.md` بذار.
- 📝 فایل `.gitignore` رو همیشه آپدیت نگه دار تا فایل‌های موقت (`__pycache__`, `*.mat`, `*.log`, `.ipynb_checkpoints`) آپلود نشن.

---

## 🛠️ عیب‌یابی سریع (Troubleshooting)

| مشکل | راه‌حل |
|:---|:---|
| `Authentication failed` | از `Personal Access Token (PAT)` به جای رمز عبور استفاده کن. یا SSH تنظیم کن. |
| تداخل در `merge` | `git status` رو بزن، فایل‌های conflict رو دستی ویرایش کن، بعد `git add <file>` و `git commit` |
| کند بودن `clone/push` | در دانشگاه: `git config --global http.proxy http://proxy.university.ac.ir:8080` |
| می‌خوای تاریخچه‌ی کامل رو بگیری (بعداً) | `git fetch --unshallow` یا `git fetch --depth=1000` |

---

## 📋 چیت‌شیت دستورات (Quick Reference)
```bash
git clone --depth 1 <url>          # دانلود سبک
git checkout -b <branch>           # ساخت شاخه جدید
git add .                          # آماده‌سازی تغییرات
git commit -m "message"            # ثبت محلی
git pull origin main               # دریافت تغییرات جدید
git push origin <branch>           # آپلود شاخه
git sparse-checkout set <dir1>     # دانلود فقط پوشه‌های خاص
git log --oneline -5               # مشاهده ۵ کامیت آخر
```

---

<p align="center">
  <sub>Internet may be unstable. Your research doesn't have to be. 🛰️🔋</sub>
</p>
```