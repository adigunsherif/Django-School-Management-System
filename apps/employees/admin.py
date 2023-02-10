from django.contrib import admin

from .models import Employee


#admin.site = MyAdminSite(name='myadmin')
admin.site.register(Employee)

admin.site.site_header = "МигрантДок Admin"
admin.site.site_title = "МигрантДок Admin Portal"
admin.site.index_title = "Добро пожаловать в МигрантДок"

