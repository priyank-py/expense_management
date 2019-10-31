from django.contrib import admin
from .models import Expense, ExpenseInstallment

# Register your models here.

class ExpenseInstallmentInline(admin.TabularInline):
    model = ExpenseInstallment
    extra = 1


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['budget', 'purpose','vendor']
    inlines = (ExpenseInstallmentInline,)
    

