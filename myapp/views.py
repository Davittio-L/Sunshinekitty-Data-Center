from django.shortcuts import render
from .utils import get_bitcoin_price
from django.http import JsonResponse

# Create your views here.
def main(request):
    return render(request, 'myapp/main.html')

def bitcoin_price_view(request):
    price = get_bitcoin_price()
    return JsonResponse({'price': price})

def live_metrics(request):
    return render(request, 'myapp/live_metrics.html')