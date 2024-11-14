from django.db import models
from filer.fields.image import FilerImageField


class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    order = models.PositiveIntegerField(
        default=0,
        db_index=True
    )

    class Meta:
        ordering = ['order']
