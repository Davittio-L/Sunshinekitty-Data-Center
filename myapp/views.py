from django.shortcuts import render, redirect
from .utils import get_bitcoin_price
from django.http import JsonResponse
from .forms import ExpenseForm
from .models import Expense

# Create your views here.
def main(request):
    return render(request, 'myapp/main.html')

def bitcoin_price_view(request):
    price = get_bitcoin_price()
    return JsonResponse({'price': price})

def live_metrics(request):
    return render(request, 'myapp/live_metrics.html')

def index(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    expenses = Expense.objects.all()
    return render(request, 'main.html', {'form': form, 'expenses': expenses})