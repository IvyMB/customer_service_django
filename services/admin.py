from django.contrib import admin
from .models import Service, Status, Type


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'client')
    search_fields = ('client',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)