# Generated by Django 4.1.1 on 2023-01-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_panelcarousel_autoplay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panelcarousel',
            name='autoplay',
        ),
        migrations.AddField(
            model_name='panel',
            name='autoplay',
            field=models.BooleanField(default=True, verbose_name='Autoplay (Només per Carousels)'),
        ),
    ]
