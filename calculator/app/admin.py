from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import User, Calculator

admin.site.register(User, UserAdmin)
admin.site.register(Calculator)
