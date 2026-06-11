from django.contrib import admin
# from django import forms
# from phonenumber_field.modelfields import PhoneNumberField
# from phonenumber_field.formfields import SplitPhoneNumberField
# from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Realtor



@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name','phone_no','email', 'is_mvp', 'hire_date')
    list_display_links = ('name', 'phone_no', 'email')
    list_editable = ('is_mvp',)