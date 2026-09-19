[app]

# (str) Title of your application
title = MyChatApp

# (str) Package name
package.name = mychatapp

# (str) Package domain (needed for android packaging)
package.domain = org.chat

# (str) Source files where the application lives (relative to .spec file)
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Version of the application
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Set 1 to full screen, 0 to not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,CAMERA

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (str) Presplash background color
android.presplash_color = #2E3B4E

[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
