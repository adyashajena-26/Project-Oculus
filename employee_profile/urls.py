from django.urls import path
from .views import profile_view,profile_image
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('profile/', profile_view, name="profile"),
    path('image_upload/',profile_image,name="profile_filled")
    
]