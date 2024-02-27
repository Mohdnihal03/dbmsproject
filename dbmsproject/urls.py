from django.contrib import admin
from django.urls import path, include
from loginpage.views import login_view  # Import the actual login view function
from restaurant import urls as restaurant_urls  # Import the restaurant app URLs
from django.conf import settings
from restaurant.views import restaurant_view
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'), 
    # path('restaurant/', include('restaurant.urls')),
  path('restaurant/', include(('restaurant.urls', 'restaurant'), namespace='restaurant')), # Include restaurant app URLs from its urls.py file
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
