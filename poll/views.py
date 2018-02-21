from django.http import HttpResponse
from django.http import JsonResponse
from .models import Binance
def binance(request):
    new_records = Binance.get_records_for(request.GET['trading_pair'])
    return JsonResponse({'new_records_count': len(new_records)})
