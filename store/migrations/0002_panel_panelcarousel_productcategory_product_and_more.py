# Generated by Django 4.1.1 on 2023-01-09 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nom del panell')),
                ('order', models.IntegerField(default=0, verbose_name='Ordre')),
                ('type', models.IntegerField(choices=[(1, 'CAROUSEL'), (2, 'PRODUCT CATEGORY'), (3, 'PRODUCT')], default=1, verbose_name='Tipus de panell')),
            ],
        ),
        migrations.CreateModel(
            name='PanelCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Títol')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='Descripció')),
                ('image', models.ImageField(blank=True, null=True, upload_to='carousel/', verbose_name='Imatge')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nom')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_category/', verbose_name='Imatge')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nom')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripció')),
                ('pvp', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Preu venta públic')),
                ('discount_percentage', models.IntegerField(default=0, verbose_name='Desconte (%)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Imatge')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='PanelProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.panel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='PanelCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.panel')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productcategory')),
            ],
        ),
    ]
