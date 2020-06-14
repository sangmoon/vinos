from django.contrib import admin
from app.models import Wine


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_ko', 'reduced_price', 'official_price', 'location', 'extra_info', 'shop', 'created_at')
    search_fields = ('name', 'name_ko')
    ordering = ('-created_at',)
