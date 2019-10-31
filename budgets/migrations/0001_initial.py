# Generated by Django 2.2.6 on 2019-10-31 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('purpose', models.CharField(max_length=50, verbose_name='Purpose')),
                ('date', models.DateField(verbose_name='Date')),
                ('amount', models.IntegerField(verbose_name='Amount (in rupees)')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vendors.Vendor', verbose_name='Vendor')),
            ],
            options={
                'verbose_name': 'Budget',
                'verbose_name_plural': 'Budgets',
            },
        ),
    ]
