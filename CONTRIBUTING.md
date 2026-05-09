# 🤝 Contributing Guide | راهنمای مشارکت

![PR Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Code of Conduct](https://img.shields.io/badge/code%20of%20conduct-yes-blue.svg)

---

## 🌍 English
Thank you for wanting to contribute! This repository is built by students, for students. Whether you're fixing a typo, adding a new example, or sharing a complete project, your work helps the Iranian aerospace community grow.  
🔹 *No contribution is too small. Every commit counts.*

## 🇮🇷 فارسی
ممنون که می‌خوای مشارکت کنی! این مخزن توسط دانشجوها، برای دانشجوها ساخته شده. چه یه غلط املایی رو اصلاح کنی، چه یه مثال جدید اضافه کنی، یا کل یه پروژه‌ی کلاسی رو به‌اشتراک بذاری، کار تو به رشد جامعه‌ی هوافضای ایران کمک می‌کنه.  
🔹 *هیچ مشارکتی کوچیک نیست. هر کامیت ارزشمنده.*


## 🛠️ How to Contribute / مراحل مشارکت

1. **Fork & Clone**  
   روی دکمه‌ی `Fork` کلیک کن تا یه کپی شخصی داشته باشی. بعدش:
   ```bash
   git clone https://github.com/YourUsername/Starter-Kit.git
   cd Starter-Kit
   ```

2. **Create a Branch**  
   همیشه روی `main` کار نکن. یه شاخه‌ی جدید بساز:
   ```bash
   git checkout -b feat/my-new-example
   # یا: fix/bug-name, docs/update-readme
   ```

3. **Make Changes & Commit**  
   کد یا مستنداتت رو اضافه کن. کامیت‌ها باید کوتاه و واضح باشن:
   ```bash
   git add .
   git commit -m "feat: add orbit prediction example with skyfield"
   ```

4. **Push & Open Pull Request**  
   تغییرات رو آپلود کن و توی گیت‌هاب دکمه‌ی `Compare & Pull Request` رو بزن.  
   ✅ در توضیحات PR بنویس: چی اضافه کردی؟ چرا؟ چطور تستش کردی؟

5. **Review & Merge**  
   تیم نگهدارنده کد رو بررسی می‌کنه. اگر نیاز به تغییر بود، روی همون برنچ کامیت بزن تا PR آپدیت بشه. بعد از تأیید، ادغام می‌شه. 🎉

---

## 📐 Standards / استانداردهای پروژه

| مورد | قانون |
|:---|:---|
| 📁 **ساختار** | هر پروژه جدید باید یه پوشه‌ی مجزا + `README.md` + فایل وابستگی (`requirements.txt`/`environment.yml`) داشته باشه |
| 💻 **زبان کد** | متغیرها و کامنت‌ها ترجیحاً انگلیسی (برای سازگاری جهانی) |
| 📖 **مستندات** | توضیحات پروژه، نحوه اجرا و پیش‌نیازها حتماً در `README` نوشته بشه (فارسی/انگلیسی آزاد) |
| 📦 **حجم** | از آپلود فایل‌های سنگین (>10MB) خودداری کن. برای دیتاست یا مدل از لینک خارجی یا `Git LFS` استفاده کن |
| ✅ **تست** | کد باید بدون خطا روی یه سیستم استاندارد اجرا بشه. خروجی نمونه یا اسکرین‌شات اضافه کن |

---

## 📶 Working Offline & Syncing / کار آفلاین و همگام‌سازی
- می‌تونی مخزن رو یک‌بار دانلود کنی و ماه‌ها بدون اینترنت کار کنی.
- تغییرات رو به صورت محلی `commit` کن. هر وقت دسترسی داشتی، `git push` بزن.
- اگر فقط به بخش خاصی نیاز داری، از `git sparse-checkout` استفاده کن تا حجم دانلود کم بشه.
- ⚠️ قبل از `push`، حتماً `git pull origin main` بزن تا با تغییرات بقیه تداخل ایجاد نشه.

---

## ⚖️ Licensing & IP / لایسنس و مالکیت فکری
- تمام کدهای اضافه‌شده به این مخزن تحت [لایسنس MIT](LICENSE) منتشر می‌شن.
- 🔒 از انتشار داده‌های طبقه‌بندی‌شده، نتایج آزمایشگاهی محدودشده یا کدهای تحت قرارداد دانشگاهی خودداری کن.
- 📚 اگر از کد/دیتای شخص دیگری استفاده کردی، حتماً منبع رو در `README` و کد ذکر کن.
- 🤝 مشارکت تو به معنی موافقت با قوانین جامعه‌ی متن‌باز و احترام به حقوق نویسندگان اصلیه.

---

## 💬 Communication / ارتباط و پشتیبانی
- برای سوال، پیشنهاد یا گزارش باگ: یه `Issue` باز کن و از تگ‌های `#help`, `#bug`, `#project`, `#idea` استفاده کن.
- برای منتورینگ، بررسی کد یا همکاری بلندمدت: مستقیماً به [@PouyaLatifiyan](https://github.com/PouyaLatifiyan) پیام بده یا ایمیل بزن.
- 🌟 *ما اینجاییم تا یاد بگیریم، نه قضاوت کنیم. سوال پرسیدن بخشی از فرآینده، نه نقطه ضعف.*

---

<p align="center">
  <sub>Every line of code is a step forward. Let's build it together. 🛰️✨</sub>
</p>
```

### ✅ نکات نهایی:
- این فایل رو دقیقاً با نام `CONTRIBUTING.md` توی ریشه‌ی ریپازیتوری ذخیره کن. گیت‌هاب به صورت خودکار لینکش رو کنار دکمه‌ی `Issues` و `Pull Requests` نمایش می‌ده.
- اگر خواستی `docs/offline-git-guide.md` یا `templates/PROJECT_README.md` رو هم آماده‌ی کپی‌پیست برات بفرستم، فقط کافیه بگی.  
آماده‌ی قدم بعدی هستی؟ 🚀
