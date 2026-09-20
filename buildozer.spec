[app]

# (str) عنوان التطبيق الذي سيظهر تحت الأيقونة في الهاتف
title = MyChatApp

# (str) اسم الحزمة البرمجية (بدون مسافات أو رموز خاصة)
package.name = mychatapp

# (str) النطاق الخاص بالحزمة (Domain)
package.domain = org.chat

# (str) المجلد المصدري الذي يحتوي على ملف main.py
source.dir = .

# (list) الامتدادات البرمجية والملفات المسموح بحزمها داخل الـ APK (تم إضافة ttf للخطوط و wav,mp3 للأصوات)
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,mp3

# (str) إصدار التطبيق الحالي
version = 0.2

# (list) المكتبات البرمجية المطلوبة للتشغيل (تتضمن مكتبات معالجة وتشكيل الحروف العربية)
requirements = python3,kivy,arabic-reshaper,python-bidi

# (str) وضع شاشة التطبيق (portrait تعني وضع طولي مستقر)
orientation = portrait

# (bool) تشغيل التطبيق بملء الشاشة وإخفاء شريط الإشعارات العلوي
fullscreen = 0

# (list) أذونات نظام أندرويد الصارمة والشاملة المطلوبة لتشغيل الكاميرا والميكروفون والإنترنت والاتصالات الحية
android.permissions = INTERNET,CAMERA,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,WAKE_LOCK

# (int) إصدار المستهدف لـ Android API (متوافق مع أندرويد 13 فما فوق)
android.api = 33

# (int) الحد الأدنى المدعوم من إصدارات أندرويد ليعمل التطبيق (أندرويد 5.0 فما فوق)
android.minapi = 21

# (str) إصدار الـ NDK المستقر والمطلوب للتجميع
android.ndk = 25b

# (str) إصدار أدوات البناء الرسمية المستقرة من أندرويد
android.build_tools_version = 33.0.0

# (list) المعمارية المستهدفة للبناء (تحديد معمارية واحدة حديثة لتسريع البناء وحماية الذاكرة من الانهيار)
android.archs = arm64-v8a

# (bool) الموافقة التلقائية على شروط وتراخيص أندرويد لتفادي توقف البناء في GitHub Actions
android.accept_sdk_license = True

# (str) لون شاشة البدء المؤقتة عند فتح التطبيق (Presplash background color)
android.presplash_color = #141B25


[buildozer]

# (int) مستوى سجل الأخطاء أثناء التجميع (2 تعني إظهار كافة التفاصيل البرمجية)
log_level = 2

# (bool) إظهار تحذير في حال تشغيل الأداة كمسؤول (Root)
warn_on_root = 1
