from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import CustomerUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )

 
admin.site.register(CustomUser, CustomUserAdmin)