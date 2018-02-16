from django.db import models


class Binance(models.Model):
  trading_pair = models.CharField(max_length=255)
  open_at = models.DateTimeField('Open time')
  open = models.DecimalField('Open', max_digits=10, decimal_places=2)
  high = models.DecimalField('High', max_digits=10, decimal_places=2)
  low = models.DecimalField('Low', max_digits=10, decimal_places=2)
  close = models.DecimalField('Close', max_digits=10, decimal_places=2)
  volume = models.DecimalField('Volume', max_digits=10, decimal_places=2)
  close_at = models.DateTimeField('Close time')
  quote_asset_volume = models.DecimalField(
      'Quote asset volume', max_digits=10, decimal_places=2)
  trades_count = models.DecimalField(
      'Number of trades', max_digits=10, decimal_places=2)
  taker_buy_base_asset_volume = models.DecimalField(
      'Taker buy base asset volume', max_digits=10, decimal_places=2)
  taker_buy_quote_asset_volume = models.DecimalField(
      'Taker buy quote asset volume', max_digits=10, decimal_places=2)
