from django.db import models
from django.utils.translation import ugettext_lazy as _
from budgets.models import Budget
from vendors.models import Vendor

# Create your models here.
class Expense(models.Model):

    pay_status = ((True, 'Payed'), (False, 'Pending'))
    expense_types = (('personal', 'Personal'), ('corporate', 'Corporate'))

    budget = models.ForeignKey(Budget , verbose_name=_("Budget"), on_delete=models.CASCADE, blank=True, null=True)
    vendor = models.ForeignKey(Vendor , verbose_name=_("Vendor"), on_delete=models.CASCADE)
    purpose = models.CharField(_("Remarks"), max_length=50, blank=True, null=True)
    payed = models.BooleanField(_("Payment status"), choices=pay_status, default=False)
    expense_type = models.CharField(_("Expense Type"), max_length=50, choices=expense_types)


    class Meta:
        verbose_name = _("Expense")
        verbose_name_plural = _("Expenses")

    def __str__(self):
        return f'{self.budget} - {self.expense_type}'

    def get_absolute_url(self):
        return reverse("Expense_detail", kwargs={"pk": self.pk})

    


class ExpenseInstallment(models.Model):

    PAY_CHOICES = (
        ('cash', 'Cash'),
        ('cheque', 'Cheque'),
        ('online', 'Online'),
        ('DD', 'Demand Draft')
    )
    expense = models.ForeignKey(Expense, related_name="installments", on_delete=models.CASCADE)
    amount_paid = models.IntegerField(_("Amount Paid"), blank=True, null=True)
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False, blank=True, null=True)
    payment_method = models.CharField(_("Payment Method"), max_length=50)
    next_pay_date = models.DateField(_("Next Pay Date"), auto_now=False, auto_now_add=False, blank=True, null=True)


    class Meta:
        verbose_name = _("ExpenseInstallment")
        verbose_name_plural = _("ExpenseInstallments")

    def __str__(self):
        return f'{self.expense}'

    def get_absolute_url(self):
        return reverse("ExpenseInstallment_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.this_expense = Expense.objects.all().filter(id=expense.id)
        setattr(self.this_expense, f'amount{id}', self.amount_paid)
        print(self.this_expense._meta)
        
        super(Expense, self).save(*args, **kwargs)
