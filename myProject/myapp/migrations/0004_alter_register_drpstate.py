# Generated by Django 5.1.4 on 2025-01-06 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='drpState',
            field=models.CharField(max_length=15),
        ),
    ]
