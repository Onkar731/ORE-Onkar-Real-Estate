from django.db import models
from realtors.models import Realtor
import uuid

class Address(models.Model):
    house_no = models.CharField(max_length=20, blank=True)
    building_name = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.building_name}, {self.house_no} {self.street}'
    
class Listing(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, related_name='realtors_listings')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.PositiveBigIntegerField()
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.PositiveSmallIntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    
    #address
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='listings_address')
    
    # house images
    photo_main = models.ImageField(upload_to='house_photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='house_photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='house_photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='house_photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='house_photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='house_photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='house_photos/%Y/%m/%d/', blank=True)
    
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    