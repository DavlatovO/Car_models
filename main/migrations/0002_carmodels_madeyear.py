# Generated by Django 5.0.6 on 2024-05-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodels',
            name='madeyear',
            field=models.IntegerField(default=2017, verbose_name='Yili'),
            preserve_default=False,
        ),
    ]
