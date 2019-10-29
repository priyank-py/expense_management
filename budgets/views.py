from django.shortcuts import render

# Create your views here.
def create_budget(request):
    return render(request, 'budget/index.html')
