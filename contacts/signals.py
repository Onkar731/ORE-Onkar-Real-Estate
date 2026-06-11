from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.shortcuts import redirect

import threading

from .models import Contact


# send emails
def send_inquiry_mails(instance):
    msg_for_user = f"""
Hi {instance.name},

Thank you for your interest in the property {instance.listing.address}.

This email is to confirm that we have received your inquiry. Our team is currently reviewing your request, and a realtor will contact you shortly to provide more details or schedule a viewing.

Inquiry Details:
- Property: {instance.listing.title}
- Date: {instance.inquiry_date.strftime('%B %d, %Y')}

If you have any urgent questions, please feel free to reply directly to this email.

Best regards,
ORE Team
"""
        
    msg_for_realtor = f"""
Hello {instance.listing.realtor.name},

A new inquiry has been submitted for one of your listed properties. Please log in to the admin panel to view the full details and follow up with the lead.

Lead Summary:
- Name: {instance.name}
- Property: {instance.listing.address}
- Email: {instance.email}
- Message: {instance.message}

View all inquiries here: http://127.0.0.1:8000

This is an automated notification from your Real Estate Portal.

Regards,
ORE Team
"""
    
    try:
        # email to realtor
        send_mail(
            subject=f'New Inquiry: {instance.listing.address}',
            message=msg_for_realtor,
            from_email=None,
            recipient_list=[instance.listing.realtor.email],
            fail_silently=False
        )
        
        # Confirmation mail to the user
        send_mail(
        subject=f"Confirmation: Received your inquiry for {instance.listing.address}",
        message=msg_for_user,
        from_email=None,
        recipient_list=[instance.email],
        fail_silently=False
    ) 
    except Exception as e:
        return redirect('/listing/' + instance.listing.id)  
    
          
@receiver(post_save, sender=Contact)
def notify_inquiry(sender, instance, created, **kwargs):
    if created:
        thread = threading.Thread(target=send_inquiry_mails, args=(instance,))
        thread.start()
        
        
      
