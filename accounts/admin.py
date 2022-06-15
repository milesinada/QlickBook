from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm 
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    
admin.site.register(CustomUser)