# Generated by Django 2.2.6 on 2019-11-12 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0010_auto_20191112_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseinstallment',
            name='payed',
            field=models.BooleanField(blank=True, choices=[('payed', 'Payment Cleared'), ('pending', 'Payment Pending')], default=False, verbose_name='Payment status'),
        ),
        migrations.AlterField(
            model_name='expenseinstallment',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('online', 'Online'), ('card', 'Credit/Debit Card'), ('DD', 'Demand Draft')], max_length=50, null=True, verbose_name='Payment Method'),
        ),
    ]
