# Generated by Django 2.2.6 on 2020-01-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0005_auto_20191112_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='registered_on',
            field=models.DateField(blank=True, null=True, verbose_name='Registered on'),
        ),
    ]
