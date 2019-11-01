# Generated by Django 2.2.6 on 2019-10-31 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('budgets', '0001_initial'),
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('purpose', models.CharField(blank=True, max_length=50, null=True, verbose_name='Purpose')),
                ('payed', models.BooleanField(choices=[(True, 'Payed'), (False, 'Pending')], default=False, verbose_name='Payment status')),
                ('next_pay_date', models.DateField(blank=True, null=True, verbose_name='Next Payment Date')),
                ('expense_type', models.CharField(choices=[('personal', 'Personal'), ('corporate', 'Corporate')], max_length=50, verbose_name='Expense Type')),
                ('budget', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budgets.Budget', verbose_name='Budget')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.Vendor', verbose_name='Vendor')),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
            },
        ),
    ]