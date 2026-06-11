from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from listings.models import Listing


# Create your models here.
class Contact(models.Model):
    user_id = models.IntegerField()
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING, related_name='listing')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    message = models.TextField(blank=True)
    inquiry_date = models.DateTimeField(auto_now_add=True)
    
    