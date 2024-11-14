from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Slider


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail')

    def image_thumbnail(self, obj):
        """Функция для отображения миниатюр в админке."""

        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return 'No Image'
    image_thumbnail.short_description = 'Image'
