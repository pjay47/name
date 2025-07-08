[app]

# (str) Title of your application
title = VoiceFileLocker

# (str) Package name
package.name = voicefilelocker

# (str) Package domain
package.domain = org.shubham

# (str) Source code where the main.py is located
source.dir = .

# (str) The main .py file
source.main = main.py

# (list) Python packages your app needs
requirements = python3,kivy,pillow

# (list) Permissions
android.permissions = RECORD_AUDIO,CAMERA,SEND_SMS,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_SMS

# (str) Android NDK version
android.ndk = 25b

# (int) Target Android API
android.api = 31

# (int) Minimum Android API your APK will support
android.minapi = 21

# (bool) Copy library instead of linking
android.copy_libs = 1

# (str) Android entry point, do not change
android.entrypoint = org.kivy.android.PythonActivity

# (str) Orientation: portrait or landscape
orientation = portrait

# (bool) Enable fullscreen (0 = no, 1 = yes)
fullscreen = 1

# (str) Application versioning (used in APK)
version = 1.0

# (str) Android log level: 1 = error only, 2 = warning, 3 = info, 4 = debug
log_level = 2

# (str) Supported architectures
android.archs = armeabi-v7a, arm64-v8a

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Android bootstrap to use
bootstrap = sdl2

# (list) Additional Java .jar files
# android.add_jars =

# (list) Custom java source folders
# android.add_src =

# (list) Android AAR libraries to add
# android.gradle_dependencies =

# (str) Unique version code
android.version_code = 1

# (str) Enable Java debugging
# android.debug = 0

# (bool) Hide statusbar
# android.hide_statusbar = 1

# (bool) Add sqlite3 support
# android.sqlite3 = 1
