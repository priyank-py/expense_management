from django.contrib import admin
from .models import Expense, ExpenseInstallment
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.

class ExpenseInstallmentInline(admin.TabularInline):
    model = ExpenseInstallment
    extra = 1


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

    def get_date(self, instance):
        try:
            return instance.installments.last().date
        except:
            return None


    list_display = ['budget', 'purpose','vendor']
    list_display_links =  ['budget', 'purpose','vendor']
    list_filter = [('installments__date', DateRangeFilter),'purpose', 'vendor']
    inlines = (ExpenseInstallmentInline,)
    
