from django.shortcuts import render, redirect
from .utils import get_bitcoin_price
import requests
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


def get_bitcoin_to_usd_rate():
    url = "https://bitpay.com/api/rates"
    response = requests.get(url)
    data = response.json()
    return data[2]["rate"]  # Index might change based on API response

def convert_usd_to_btc(request):
    usd_price = request.GET.get('usd_price', 10)
    usd_price = float(usd_price)
    rate = get_bitcoin_to_usd_rate()
    bitcoin_price = round(usd_price / rate, 8)
    return JsonResponse({'usd_price': usd_price, 'bitcoin_price': bitcoin_price})

def convert_btc_to_usd(request):
    btc_amount = request.GET.get('btc_amount', 0.1)
    btc_amount = float(btc_amount)
    rate = get_bitcoin_to_usd_rate()
    usd_price = round(btc_amount * rate, 2)
    return JsonResponse({'btc_amount': btc_amount, 'usd_price': usd_price})