# Generated by Django 2.0.2 on 2018-02-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binance',
            name='close_at',
            field=models.DateTimeField(verbose_name='Close time'),
        ),
    ]
