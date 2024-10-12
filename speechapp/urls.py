from django.urls import path
from . import views  # Import the views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL to the 'home' view
]
