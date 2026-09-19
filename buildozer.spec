[app]

# (str) Title of your application
title = MyChatApp

# (str) Package name
package.name = mychatapp

# (str) Package domain (needed for android packaging)
package.domain = org.chat

# (str) Source files where the application lives (relative to .spec file)
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Set 1 to full screen, 0 to not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,CAMERA

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use (السطر المسؤول عن حل مشكلة الخطأ)
android.ndk = 25b

# (str) Presplash background color
android.presplash_color = #2E3B4E

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
