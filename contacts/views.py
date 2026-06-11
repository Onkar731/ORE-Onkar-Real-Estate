from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Contact
from listings.models import Listing


def make_inquiry(request):
    if "POST" == request.method:
        if not request.user.is_authenticated:
            messages.warning(request, 'Unauthenticated user. Kindly login to make an inquiry.')
            return redirect('accounts:login')
        
        user_id = request.POST.get('user_id', None)
        property_id = request.POST.get('property_object')
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        message = request.POST.get('message', None)
        
        if Contact.objects.filter(listing__id=property_id, user_id=user_id).exists():
            messages.info(request, 'You already made an inquiry for this property. A realtor will get back to you soon.')
            return redirect('/listings/' + property_id)
            
        property = get_object_or_404(Listing, pk=property_id)
        contact = Contact(user_id=user_id, listing=property, name=name, email=email, phone_number=phone, message=message)
        contact.save()
        
        messages.success(request, 'Your inquiry request has been submitted, a realtor will get back to you soon')
        
        return redirect('/listings/' + property_id)
    
    return redirect('listings:listings')
        
        
        