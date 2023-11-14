from django.shortcuts import render
from .utils import get_bitcoin_price

# Create your views here.
def main(request):
    return render(request, 'myapp/main.html')

def bitcoin_price_view(request):
    price = get_bitcoin_price()
    return render(request, 'myapp/main.html', {'price': price})