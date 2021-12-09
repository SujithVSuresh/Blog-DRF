from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import NewUser

@admin.register(NewUser)
class UserAdmin(ModelAdmin):
    list_display = ('email', 'id', 'user_name', 'first_name', 'is_active', 'is_staff')
 
