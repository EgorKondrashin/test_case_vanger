# Generated by Django 4.1 on 2024-11-19 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['order'], 'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайды'},
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
