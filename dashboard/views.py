from django.shortcuts import render
from budgets.models import Budget
from expenses.models import Expense
import calendar 
from datetime import datetime, date, timedelta
from django.db.models import Sum


def dashboard(request):

    current_month = int(datetime.now().strftime('%m'))
    current_year = int(datetime.now().strftime('%Y'))
    first_day, last_day = calendar.monthrange(current_year, current_month)
    start_month_date = datetime.today().replace(day=1)
    end_month_date = datetime.today().replace(day=last_day)
    months_budget = Budget.objects.all().filter(date__gte=start_month_date).filter(date__lte=end_month_date)
    total_month = Budget.objects.all().filter(date__gte=start_month_date).filter(date__lte=end_month_date).aggregate(Sum('amount'))
    
    budget_next_seven_days = Budget.objects.all().filter(date__gte=date.today()).filter(date__lte=date.today() + timedelta(days=6)).aggregate(Sum('amount'))

    expenses_so_far = Expense.objects.all().filter(installments__date__gte=start_month_date).filter(installments__date__lte=date.today()).values_list('installments__amount_paid')

    expenses_so_far = sum([sum(i) for i in expenses_so_far])

    expenses_past_seven_days = Expense.objects.all().filter(installments__date__gte=date.today() - timedelta(days=6)).filter(installments__date__lte=date.today()).values_list('installments__amount_paid')
    expenses_past_seven_days = [sum(i) for i in expenses_past_seven_days]


    context = {
        'months_budget': months_budget,
        'total_month': total_month,
        'budget_next_seven_days': budget_next_seven_days,
        'expenses_so_far': expenses_so_far,
        'expenses_so_far': expenses_so_far,
        'expenses_past_seven_days': expenses_past_seven_days,
    }

    return render(request, 'main/index.html', context)