from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('bitcoin-price/', views.bitcoin_price_view, name='bitcoin_price'),
    path('live_metrics/', views.live_metrics, name='live_metrics'),
]