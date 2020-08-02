from django.contrib import admin

# Register your models here.
from .models import Criminal_Info, user_criminal_info

admin.site.register(Criminal_Info)
admin.site.register(user_criminal_info)