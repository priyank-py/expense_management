from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Vendor(models.Model):

    account_type_choices = (('current', 'Current'), ('savings', 'Savings'))

    name = models.CharField(_("Vendor name"), max_length=50)
    phone = models.CharField(_("Phone number"), max_length=50)
    alternate = models.CharField(_("Alternate number"), max_length=50, blank=True, null=True)
    address = models.TextField(_("Address"), blank=True, null=True)
    connection = models.CharField(_("Connection"), max_length=50, blank=True, null=True)
    
    account_name = models.CharField(_("Account Name"), max_length=50, blank=True, null=True)
    account_number = models.CharField(_("Account Number"), max_length=50, blank=True, null=True)
    bank_branch = models.CharField(_("Bank Branch"), max_length=50, blank=True, null=True)
    ifsc_code = models.CharField(_("IFSC code"), max_length=50, blank=True, null=True)
    gst = models.CharField(_("GST no."), max_length=50, blank=True, null=True)
    tan = models.CharField(_("TAN no."), max_length=50, blank=True, null=True)
    pan = models.CharField(_("PAN no."), max_length=50, blank=True, null=True)
    account_type = models.CharField(_("Account Type"), max_length=50, choices=account_type_choices, blank=True, null=True)

    class Meta:
        verbose_name = _("Vendor")
        verbose_name_plural = _("Vendors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Vendor_detail", kwargs={"pk": self.pk})


