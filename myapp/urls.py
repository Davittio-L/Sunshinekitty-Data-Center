from django.urls import path
from . import views
from .views import convert_usd_to_btc

urlpatterns = [
    path('', views.main, name='main'),
    path('bitcoin-price/', views.bitcoin_price_view, name='bitcoin_price'),
    path('live_metrics/', views.live_metrics, name='live_metrics'),
    path('convert-usd-to-btc/', convert_usd_to_btc, name='convert_usd_to_btc'),
]