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

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Indicate whether the application should create a presplash or not
android.presplash_color = #2E3B4E

# (str) Supported orientations
orientation = portrait

# --- أضف هذه السطور لقبول التراخيص تلقائياً ---
[buildozer]
log_level = 2
warn_on_root = 1
