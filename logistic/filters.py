import django_filters

from logistic.models import Stock

class StockFilter(django_filters.FilterSet):
    product = django_filters.NumberFilter(
        field_name='positions__product_id', 
        lookup_expr='exact'
    )
    class Meta:
        model = Stock
        fields = ['products']