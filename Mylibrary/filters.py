import django_filters
from .models import *


class BookFilters(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['publication_date']
