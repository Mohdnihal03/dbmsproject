# restaurant/views.py
from django.shortcuts import render
from django.http import HttpResponse

def restaurant_view(request):
    # Your logic for the restaurant view goes here
    #  return HttpResponse("This is the restaurant view")
      return render(request,'restaurant/index.html')

def booking_view(request):

      return render(request,'restaurant/about.html')