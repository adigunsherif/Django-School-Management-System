from django.contrib import admin

from .models import Employee


#admin.site = MyAdminSite(name='myadmin')
admin.site.register(Employee)

admin.site.site_header = "МиграДок Admin"
admin.site.site_title = "МиграДок Admin Portal"
admin.site.index_title = "Welcome to МиграДок Portal"

