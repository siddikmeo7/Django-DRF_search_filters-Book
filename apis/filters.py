from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from .models import *

# Book Filter
class BookFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte') 
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['author', 'min_price', 'max_price',]


class BookFilter(filters.FilterSet):
    published_after = filters.DateFilter(field_name="published_date", lookup_expr="gte")
    published_before = filters.DateFilter(field_name="published_date", lookup_expr="lte")

    class Meta:
        model = Book
        fields = ["published_after", "published_before"]


class BookFilter(filters.FilterSet):
    language = filters.CharFilter(field_name="language", lookup_expr="exact")

    class Meta:
        model = Book
        fields = ["language"]

class BookFilter(filters.FilterSet):
    author = filters.CharFilter(field_name="author", lookup_expr="icontains")  

    class Meta:
        model = Book
        fields = ["author"]

class BookFilter(filters.FilterSet):
    is_available = filters.BooleanFilter(field_name="is_active")

    class Meta:
        model = Book
        fields = ["is_active"]

class BookFilter(filters.FilterSet):
    price_min = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = filters.NumberFilter(field_name="price", lookup_expr="lte")
    author = filters.CharFilter(field_name="author", lookup_expr="icontains")
    language = filters.CharFilter(field_name="language", lookup_expr="exact")
    published_after = filters.DateFilter(field_name="published_date", lookup_expr="gte")
    published_before = filters.DateFilter(field_name="published_date", lookup_expr="lte")

    class Meta:
        model = Book
        fields = ["price_min", "price_max", "author", "language", "published_after", "published_before"]

