# Generated by Django 5.1.4 on 2025-01-07 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_register_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='profile_image',
            field=models.ImageField(default='', upload_to='media/profile_photos/'),
        ),
    ]
