[app]
title = ConsignorApp
package.name = consignor
package.domain = org.mohit

source.dir = .
source.include_exts = py,xlsx

requirements = python3,kivy,pandas,openpyxl

orientation = portrait

[buildozer]
log_level = 2

[android]
android.api = 33
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2

android.permissions = READ_EXTERNAL_STORAGE
