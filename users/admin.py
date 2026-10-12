from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models  import User



@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets=UserAdmin.fieldsets+(
        ('Company',{'fields':('role','Department','manager')}),
)

    list_display=('Username','email','role','department')