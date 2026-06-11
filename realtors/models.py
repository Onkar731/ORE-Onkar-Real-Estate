from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Realtor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    phone_no = PhoneNumberField()
    email = models.EmailField()
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='realtors_photo/%Y/%m/%d/')
    
    def __str__(self):
        return self.name
