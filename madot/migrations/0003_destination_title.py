# Generated by Django 5.1.2 on 2024-11-08 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madot', '0002_remove_dayitinerary_accommodation_dayitinerary_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='title',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
