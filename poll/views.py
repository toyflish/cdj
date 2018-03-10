from django.http import HttpResponse
from django.http import JsonResponse
from .models import Binance
def binance(request):
    # allow string with multiple tradingpairs
    trading_pairs = request.GET['trading_pair'].split(',')

    new_records = {}
    for pair in trading_pairs:
        records = Binance.get_records_for(pair)
        new_records[pair] = len(records)
    return JsonResponse(new_records)
