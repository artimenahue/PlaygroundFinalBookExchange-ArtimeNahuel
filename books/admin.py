from django.utils.html import format_html
from django.contrib import admin
from .models import Book, ExchangeRequest

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description', 'thumbnail')
    readonly_fields = ('user',)

    def thumbnail(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.photo.url)

    thumbnail.short_description = 'Imagen'

@admin.register(ExchangeRequest)
class ExchangeRequestAdmin(admin.ModelAdmin):
    list_display = ('book', 'requester', 'created_at')
    list_filter = ('created_at',)