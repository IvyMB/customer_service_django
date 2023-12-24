from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'telephone', 'gender', 'birthday', 'address', 'country', 'state',
                    'hiring_date', 'deactivate_date', 'created_at')
    search_fields = ('username', 'email')
