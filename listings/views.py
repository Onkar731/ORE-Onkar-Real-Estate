from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Listing
from .filters import FilteredListings
from listings.choices import bedroom_choices, price_choices, state_choices


def listings(request):
    listings = Listing.objects.order_by('-created_at').filter(is_published=True)
    
    paginator = Paginator(listings, 3)
    page = request.GET.get('p')
    paginated_listings = paginator.get_page(page)
    
    context = {
        'listings':paginated_listings
    }
    
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    requested_listing = get_object_or_404(Listing, pk=listing_id)
    
    house_photos = []
    
    for i in range(1, 7):
        photo = getattr(requested_listing, f'photo_{i}', None)
        
        if photo:
            house_photos.append(photo)
    # i = 1 
    # while True:
    #     photo = getattr(requested_listing, f'photo_{i}', None)
    #     if photo:
    #         house_photos.append(photo)
    #         print('inside if', i)
    #         i += 1
    #     print('outside if', i)      
    #     break
            
            
            
    context = {
        'listing':requested_listing,
        'house_photos': house_photos
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    listings = Listing.objects.order_by('-created_at')
    
    filtered_listings = FilteredListings(request.GET, listings)

    context = {
        'bedrooms': bedroom_choices,
        'price': price_choices,
        'state': state_choices,
        'listings': filtered_listings.qs,
        'values': request.GET
    }
    
    return render(request, 'listings/search.html', context)