from django.urls import path
from .views import group_view,clickgroup_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('groupattendance/', group_view, name="groupattendance"),
    path('clickgroup/',clickgroup_view, name="clickgroup")
    # path('image_upload/',profile_image,name="profile_filled")
    
]