from django.contrib import admin
from .models import Vendor

# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'connection']
    search_fields = ['name', 'phone', 'connection']
    list_display_links =  ['name', 'phone',]

    
