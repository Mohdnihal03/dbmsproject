from django.urls import path
from .views import restaurant_view , booking_view, index

urlpatterns = [
    path('restaurant_view/', restaurant_view, name='restaurant_view'),
    path('', index, name='index'),
    # Other URL patterns for the restaurant app
    path('booking_view/', booking_view, name='booking_view'),

]