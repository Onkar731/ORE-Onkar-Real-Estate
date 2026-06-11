import django_filters
from django.db.models import Q
from .models import Listing

class FilteredListings(django_filters.FilterSet):
    keywords = django_filters.CharFilter(
        field_name="description",
        lookup_expr="icontains"
    )
    # search = django_filters.CharFilter(method="or_filter")
    
    price = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="lte"
    )
    
    bedrooms = django_filters.NumberFilter(
        field_name="bedrooms",
        lookup_expr="lte"
    )
    
    city = django_filters.CharFilter(
        field_name="address__city",
        lookup_expr="iexact"
    )
    
    state = django_filters.CharFilter(
        field_name="address__state",
        lookup_expr="iexact"
    )

    class Meta:
        model = Listing
        fields = []
        
    # def or_filter(self, queryset, name, value):
    #     return queryset.filter(
    #         Q(description__icontains=value) |
    #         Q(address__city__icontains=value) |
    #         Q(address__state__icontains=value)
    #     )