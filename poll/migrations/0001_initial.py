# Generated by Django 2.0.2 on 2018-02-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Binance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trading_pair', models.CharField(max_length=255)),
                ('open_at', models.DateTimeField(verbose_name='Open time')),
                ('open', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Open')),
                ('high', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='High')),
                ('low', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Low')),
                ('close', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Close')),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Volume')),
                ('close_at', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Close time')),
                ('quote_asset_volume', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Quote asset volume')),
                ('trades_count', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Number of trades')),
                ('taker_buy_base_asset_volume', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Taker buy base asset volume')),
                ('taker_buy_quote_asset_volume', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Taker buy quote asset volume')),
            ],
        ),
    ]
