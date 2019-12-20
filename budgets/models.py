from django.db import models
from django.utils.translation import ugettext_lazy as _
from vendors.models import Vendor
# Create your models here.

class Budget(models.Model):

    budget_type_choices = (('personal', 'Personal'), ('corporate', 'Corporate'))

    title = models.CharField(_("Title"), max_length=50)
    budget_type = models.CharField(_("Budget Type"), choices=budget_type_choices, max_length=20, blank=True, null=True)
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    amount = models.IntegerField(_("Amount (in rupees)"))
    vendor = models.ForeignKey(Vendor , verbose_name=_("Vendor"), on_delete=models.DO_NOTHING)
    

    class Meta:
        verbose_name = _("Budget")
        verbose_name_plural = _("Budgets")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Budget_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        try:
            msg = EmailMessage(f'Budget for {self.budget.title} is added!', f'Budget for {self.budget_type} have set to be due on {self.date} to our vendor named {self.vendor.name}\n\nRemarks:{self.purpose}', 'factscred@gmail.com', ['priyank7137@gmail.com'])
            msg.content_subtype = "html" 
            msg.send()

            super(Expense, self).save(*args, **kwargs)
        except:
            super(Expense, self).save(*args, **kwargs)
