from django.contrib import admin
from .models import Listing, Address

admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Real Estate | Admin"
admin.site.index_title = "Real Estate Management Dashboard"


@admin.register(Listing)
class ListingModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'sqft', 'lot_size', 'price', 'get_realtor_name', 'is_published', 'updated_at', 'address')
    list_display_links = ('title', 'sqft', 'lot_size', 'price', 'get_realtor_name', 'updated_at', 'address')
    list_editable = ('is_published',)
    list_filter = ('sqft', 'lot_size', 'price','is_published', 'updated_at')
    search_fields = ('title', 'realtor', 'description', 'price', 'address', 'sqft', 'lot_size',)
    
    def get_realtor_name(self, obj):
        return obj.realtor.name
    
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('house_no', 'building_name', 'city', 'state', 'zipcode')
    list_display_links = list_display