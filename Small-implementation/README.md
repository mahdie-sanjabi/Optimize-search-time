# سیستم مدیریت نام کاربری با استفاده از درخت B+ و پایگاه داده MySQL

این پروژه یک سیستم مدیریت نام کاربری است که از ترکیب دو فناوری اصلی استفاده می‌کند: درخت B+ برای ذخیره‌سازی و جستجو در میان نام‌های کاربری و پایگاه داده MySQL برای ذخیره‌سازی دائمی. هدف این پروژه مدیریت بهینه نام‌های کاربری در یک سیستم است.

## ساختار پروژه

### 1. **درخت B+ (BPlusTree)**
درخت B+ یک ساختار داده درختی است که برای انجام عملیات جستجو و درج با کارایی بالا طراحی شده است. ویژگی‌های این بخش از پروژه عبارتند از:

- **جستجو درخت B+**: امکان جستجوی نام کاربری در درخت با استفاده از الگوریتم جستجوی باینری فراهم شده است.
- **افزودن نام کاربری**: وقتی یک نام کاربری جدید وارد می‌شود، ابتدا در درخت جستجو می‌شود و اگر موجود نباشد، به درخت اضافه می‌شود.
- **ذخیره‌سازی درخت**: پس از هر تغییر در درخت، داده‌ها در یک فایل ذخیره می‌شوند تا در آینده قابل بارگذاری باشند.
- **بارگذاری درخت**: درخت از یک فایل بارگذاری می‌شود تا اطلاعات قبلی حفظ شوند.

### 2. **پایگاه داده MySQL**
پایگاه داده MySQL برای ذخیره‌سازی دائمی نام‌های کاربری استفاده می‌شود. ویژگی‌های این بخش شامل:

- **ایجاد پایگاه داده و جدول**: ابتدا پایگاه داده `user_search` ساخته شده و جدول `userconnect` برای ذخیره نام‌های کاربری ایجاد می‌شود.
- **افزودن نام کاربری به پایگاه داده**: زمانی که یک نام کاربری جدید وارد می‌شود، ابتدا در پایگاه داده جستجو می‌شود که آیا موجود است یا خیر. اگر نام جدید باشد، به جدول `userconnect` اضافه می‌شود.
- **درج از فایل**: نام‌های کاربری از فایل متنی خوانده شده و به پایگاه داده اضافه می‌شوند.

### 3. **رابط کاربری**
این پروژه دارای رابط کاربری خط فرمان است که به کاربران امکان انجام عملیات مختلف را می‌دهد:

- **اضافه کردن نام کاربری**: با وارد کردن علامت `+`، کاربر می‌تواند یک نام کاربری جدید را وارد کند.
- **بررسی وجود نام کاربری**: با وارد کردن علامت `c`، کاربر می‌تواند بررسی کند که آیا یک نام کاربری در سیستم موجود است یا خیر.
- **خروج و ذخیره‌سازی**: با وارد کردن `00`، برنامه از کاربر می‌خواهد که آیا تغییرات را ذخیره کند یا خیر.

## نحوه استفاده

1. **راه‌اندازی پایگاه داده**:
   برای شروع، ابتدا باید پایگاه داده و جدول مربوطه را ایجاد کنید. این کار به صورت خودکار هنگام اجرای پروژه انجام می‌شود.
   
2. **اضافه کردن و بررسی نام کاربری**:
   - برای اضافه کردن یک نام کاربری جدید، از گزینه `+` استفاده کنید.
   - برای بررسی وجود یک نام کاربری، از گزینه `c` استفاده کنید.
   - برای خروج و ذخیره یا عدم ذخیره تغییرات، از گزینه `00` استفاده کنید.

## ساختار فایل‌ها

1. **`BPTree.py`**: شامل کلاس‌های مربوط به درخت B+ و متدهای آن برای جستجو، درج و ذخیره‌سازی است.
2. **`create_database.py`**: شامل کدهای مربوط به ایجاد پایگاه داده MySQL، جدول‌ها و عملیات درج داده‌ها است.
3. **`main.py`**: نقطه شروع برنامه است که از کاربر می‌خواهد عملیات مورد نظر خود را انجام دهد.

## پیش‌نیازها

- **MySQL**: باید MySQL بر روی سیستم شما نصب و اجرا شود (می‌توانید از XAMPP برای راه‌اندازی استفاده کنید).
- **کتابخانه mysql-connector**: برای ارتباط با پایگاه داده MySQL نیاز به این کتابخانه دارید. می‌توانید آن را با استفاده از دستور زیر نصب کنید:
  

## نحوه راه‌اندازی

1. اطمینان حاصل کنید که **MySQL** در حال اجرا است.
2. ابتدا اسکریپت `create_database.py` را اجرا کنید تا پایگاه داده و جدول‌ها ایجاد شوند.
3. سپس فایل `main.py` را اجرا کنید و از رابط کاربری استفاده کنید.
