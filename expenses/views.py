from django.shortcuts import render
from .models import Expense
from django.db.models import Sum
from datetime import date, datetime
import calendar
# Create your views here.

def upcomming_expenses(request):
    pass

def expenses(request):
    current_month = int(datetime.now().strftime('%m'))
    current_month_word = datetime.now().strftime('%B')
    current_year = int(datetime.now().strftime('%Y'))
    first_day, last_day = calendar.monthrange(current_year, current_month)
    start_month_date = datetime.today().replace(day=1)
    end_month_date = datetime.today().replace(day=last_day)
    start_date = request.GET.get('start')
    end_date = request.GET.get('end')
    
    
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()  
    except:
        start_date = start_month_date
    try:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date() 
    except:
        end_date = end_month_date

    all_expenses = Expense.objects.all().filter(budget__date__gte=start_date).filter(budget__date__lte=end_date)
    # all_expenses_budget = [i.budget.date for i in all_expenses]
    
    paid = [i.installments.aggregate(Sum('amount_paid'))['amount_paid__sum'] if i.installments.exists() else 0 for i in all_expenses]
    to_pay = [i.budget.amount - j if i.installments.exists() else i.budget.amount for i, j in zip(all_expenses, paid)]
    pay_for = [i.budget.title for i in all_expenses]
    # expense_data = list(zip(all_expenses, paid, to_pay))
    
    context = {
        'pay_for': pay_for,
        'paid': paid,
        'to_pay': to_pay,
        # 'expense_data': expense_data,
    }
    return render(request, 'expense/expenses.html', context)