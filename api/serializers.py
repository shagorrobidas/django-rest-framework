from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    # unit_display = serializers.CharField(
    #     source='get_unit_display', read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'quantity',
            'total_price',
            'unit',
            # 'unit_display',
        ]
        extra_kwargs = {
            'quantity': {'min_value': 0},
        }

    def get_total_price(self, obj):
        return float(obj.price)*(obj.quantity)
