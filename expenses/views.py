from django.shortcuts import render

# Create your views here.

def upcomming_expenses(request):
    pass

def expenses(request):
    return render(request, 'expense/expenses.html')