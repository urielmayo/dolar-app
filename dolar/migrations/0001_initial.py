# Generated by Django 4.1.1 on 2023-05-16 01:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Dolar',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=70)),
                ('slug', models.CharField(max_length=100)),
                ('description', models.TextField()),
                (
                    'sell_price',
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=5
                    ),
                ),
                (
                    'buy_price',
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=5
                    ),
                ),
            ],
            options={
                'verbose_name': 'Dolar',
                'verbose_name_plural': 'Dolars',
            },
        ),
    ]