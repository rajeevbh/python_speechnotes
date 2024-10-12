from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('speechapp.urls')),  # Map the app's URLs to the root
]
