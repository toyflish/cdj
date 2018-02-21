from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^api/worker/binance$', views.binance, name='binance')
]
