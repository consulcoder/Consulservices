from django.contrib import admin

from .models import Store

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'description')
    search_fields = ('name', 'number')
    list_filter = ('number',)
