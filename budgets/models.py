from django.db import models
from django.utils.translation import ugettext_lazy as _
from vendors.models import Vendor
# Create your models here.

class Budget(models.Model):

    title = models.CharField(_("Title"), max_length=50)
    purpose = models.CharField(_("Purpose"), max_length=50)
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
