# Generated by Django 5.0.6 on 2024-05-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_carmodels_madeyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodels',
            name='description',
            field=models.TextField(default=12, verbose_name='Tavsif'),
            preserve_default=False,
        ),
    ]