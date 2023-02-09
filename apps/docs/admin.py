from django.contrib import admin

from .models import Doc


#admin.site = MyAdminSite(name='myadmin')
admin.site.register(Doc)

admin.site.site_header = "МигрантДок Admin"
admin.site.site_title = "МигрантДок Admin Portal"
admin.site.index_title = "Welcome to МигрантДок Portal"

