[app]

title = MyChatApp
package.name = mychatapp
package.domain = org.chat
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,CAMERA
android.api = 33
android.minapi = 21
android.ndk = 25b

# قبول تراخيص الـ SDK تلقائياً لتفادي توقف البناء في GitHub Actions
android.accept_sdk_license = True

# (str) إجبار البناء على استخدام إصدار مستقر لا يتطلب تراخيص معقدة
android.build_tools_version = 33.0.0

android.presplash_color = #2E3B4E

[buildozer]
log_level = 2
warn_on_root = 1
