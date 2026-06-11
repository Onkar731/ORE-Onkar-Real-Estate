from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, state_choices, bedroom_choices

def index(request):
    latest_listings = Listing.objects.order_by('-created_at').filter(is_published=True)[:3]
    
    context = {
        'listings': latest_listings,
        'bedrooms': bedroom_choices,
        'price': price_choices,
        'state': state_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # all realtors
    realtors = Realtor.objects.all()
    
    # fetching mvp realtors
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }
    
    return render(request, 'pages/about.html', context)
