# Generated by Django 5.0.6 on 2024-05-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_category_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
