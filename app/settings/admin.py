from django.contrib import admin
from app.settings.models import Settings, Form
# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['id', 'title']
    search_fields = ['id', 'title']

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']
    list_editable = ['is_active']
    search_fields = ['id', 'name', 'is_active']