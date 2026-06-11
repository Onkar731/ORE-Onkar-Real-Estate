from django.urls import path
from .views import make_inquiry 

app_name = 'contacts'

urlpatterns = [
    path('', make_inquiry, name='inquiry'),
]
