# Generated by Django 5.1.4 on 2025-01-11 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_register_email_alter_register_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
