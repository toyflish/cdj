from django.db import models, IntegrityError
from binance.client import Client
from django.utils.timezone import datetime as dt
import pytz
import logging
logger = logging.getLogger(__name__)

class Binance(models.Model):

    class Meta:
        unique_together = (('trading_pair', 'open_at', 'close_at'),)
        indexes = [
            models.Index(fields=['trading_pair']),
            models.Index(fields=['trading_pair', 'open_at'])
        ]

    trading_pair = models.CharField(max_length=255)
    open_at = models.DateTimeField('Open time')
    open = models.DecimalField('Open', max_digits=17, decimal_places=7)
    high = models.DecimalField('High', max_digits=17, decimal_places=7)
    low = models.DecimalField('Low', max_digits=17, decimal_places=7)
    close = models.DecimalField('Close', max_digits=17, decimal_places=7)
    volume = models.DecimalField('Volume', max_digits=17, decimal_places=7)
    close_at = models.DateTimeField('Close time')
    quote_asset_volume = models.DecimalField('Quote asset volume', max_digits=17, decimal_places=7)
    trades_count = models.IntegerField('Number of trades', default=0)
    taker_buy_base_asset_volume = models.DecimalField('Taker buy base asset volume', max_digits=17, decimal_places=7)
    taker_buy_quote_asset_volume = models.DecimalField('Taker buy quote asset volume', max_digits=17, decimal_places=7)

    def __str__(self):
        return ' '.join([
            self.trading_pair,
            str(self.open_at),
            str(self.open),
        ])

    @classmethod
    def load_klines(self, trading_pair='BTCUSDT'):
        binance_api_key = ''
        binance_api_secret = ''
        client = Client(binance_api_key, binance_api_secret)
        last_record = self.last_record_for(trading_pair=trading_pair)
        start_str = "4 month ago UTC+1" if last_record is None else str(last_record.open_at)
        klines = client.get_historical_klines(
            trading_pair, Client.KLINE_INTERVAL_15MINUTE, start_str)
        return klines

    @classmethod
    def micro_timestamp_datetime(self, ts):
        return dt.utcfromtimestamp(int(ts)/1000).replace(tzinfo=pytz.utc)


    @classmethod
    def get_records_for(self, trading_pair='BTCUSDT'):

        new_records = []
        klines = self.load_klines(trading_pair)

        # klines = [klines[0]]

        for r in klines:
            b = self(trading_pair=trading_pair,
                open_at=self.micro_timestamp_datetime(r[0]),
                open=r[1],
                high=r[2],
                low=r[3],
                close=r[4],
                volume=r[5],
                close_at=self.micro_timestamp_datetime(r[6]),
                quote_asset_volume=r[7],
                trades_count=r[8],
                taker_buy_base_asset_volume=r[9],
                taker_buy_quote_asset_volume=r[10])
            try:
                b.save()
                logger.info("Saved record successfully")
                new_records.append(b)
            except IntegrityError as e:
                logger.warning(f"Error: {e.__cause__}")
        return new_records

    @classmethod
    def last_record_for(self, trading_pair="BTCUSDT"):
        return self.objects.filter(trading_pair=trading_pair).order_by('-open_at').first()

