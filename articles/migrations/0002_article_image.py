# Generated by Django 4.1.4 on 2023-01-23 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
