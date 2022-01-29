from django.contrib import admin
from .models import CartItem


class SettingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CartItem._meta.get_fields()]


admin.site.register(CartItem, SettingAdmin)

# Register your models here.
