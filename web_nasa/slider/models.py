from django.db import models
from filer.fields.image import FilerImageField


class Slider(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    image = FilerImageField(
        verbose_name='Изображение',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    order = models.PositiveIntegerField(
        'Порядок',
        default=0,
        db_index=True
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
