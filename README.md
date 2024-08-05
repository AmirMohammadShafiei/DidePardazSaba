پروژه آزمایشی
شرکت دانا پرداز صبا اصفهان


**شرح پروژه آزمایشی**

هدف از این پروژه ذخیره و ثبت اطلاعات گوشی‌های همراه در انبار شرکت است. این اطلاعات برای مدیر انبار و مدیر پروژه ضروری است. نیازمندی‌های پروژه به شرح زیر است:

### بخش الف: ذخیره اطلاعات
1. **مدل و ذخیره اطلاعات**:
    - نام برند، ملیت برند، مدل، قیمت، رنگ، سایز صفحه نمایش، وضعیت موبایل.
2. **فرم‌های ذخیره‌سازی**:
    - استفاده از فرم‌های مناسب برای ذخیره‌سازی اطلاعات.
3. **گزارش‌ها**:
    - تهیه گزارشات از اطلاعات ذخیره شده.
4. **مسائل طراحی**:
    - در نظر گرفتن مسائل احتمالی که در طراحی در نظر گرفته نشده است.

### بخش ب: مدل پروژه
شرکت نیاز دارد که اطلاعات مربوط به هر گوشی موبایل که وارد انبار می‌شود ثبت و ذخیره گردد. اطلاعاتی که برای هر گوشی موبایل باید ذخیره شود شامل موارد زیر است:
- نام برند
- ملیت برند
- مدل
- قیمت
- رنگ
- سایز صفحه نمایش
- وضعیت موبایل 
- کشور سازنده

### بخش ج: فرم‌های ذخیره‌سازی
ایجاد فرم‌هایی برای ذخیره اطلاعات بالا در دیتابیس. این فرم‌ها باید اطلاعات را ارزیابی و در صورت صحیح بودن، آنها را در دیتابیس ذخیره کنند.

### بخش د: گزارشات
شرکت نیاز به تهیه گزارشات از انبار گوشی‌های موجود دارد. این گزارشات می‌تواند به شکل یک رشته ساده یا فایل JSON باشد. برای نمایش گزارشات می‌توان از لیست‌های زیر استفاده کرد:
1. لیست تمام برندهایی که ملیت آنها Korea است.
2. لیست تمام موبایل‌های ورودی یک برند خاص.
3. لیست تمام موبایل‌هایی که ملیت برند با کشور سازنده برابر است.
4. لیست مسائل و بهبود‌های احتمالی پروژه.

### جدول مدل گوشی‌های شرکت
| نام برند | ملیت برند | مدل گوشی | قیمت | رنگ | سایز صفحه نمایش | کشور سازنده | وضعیت |
|----------|-----------|-----------|-------|------|-------------------|--------------|--------|
| Samsung  | Korea     | Galaxy S20     | 700   | White | 6.5 | Korea | + |
| Samsung  | Korea     | Galaxy S20     | 650   | Black | 6.5 | Korea | + |
| Samsung  | Korea     | Galaxy S20+    | 750   | Black | 6.5 | China | + |
| Apple    | USA       | iPhone 12      | 1000  | Gold  | 6.1 | China | - |
| Apple    | USA       | iPhone 12 Pro  | 1100  | Silver| 6.1 | China | + |
| Xiaomi   | China     | Mi 11 Pro      | 850   | White | 6.5 | China | + |
| Xiaomi   | China     | Mi 11X         | 800   | Blue  | 6.5 | China | + |


----------------------------------------------------------------------------------------------------------------------
توضیحات اجرا :

ابتدا venv را فعال کنید :

.\venv\Scripts\activate

با دستور زیر پروژه را اجرا کیند :

py manage.py runserver

وارد url زیر شوید:

http://127.0.0.1:8000/phone/

