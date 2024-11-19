from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Slider
from easy_thumbnails.files import get_thumbnailer


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail')

    def image_thumbnail(self, obj):
        """Функция для отображения миниатюр в админке."""

        if obj.image:
            thumbnailer = get_thumbnailer(obj.image)
            thumbnail = thumbnailer.get_thumbnail({
                'size': (100, 100),
                'crop': True,
                'upscale': True,
            })
            return format_html('<img src="{}" />', thumbnail.url)
        return 'No Image'
    image_thumbnail.short_description = 'Изображение'
