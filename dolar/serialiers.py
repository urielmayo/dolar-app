from rest_framework import serializers
from dolar.models import Dolar


class DolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dolar
        fields = ('name', 'buy_price', 'sell_price', )
