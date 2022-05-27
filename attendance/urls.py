from django.urls import path
from .views import attendance_view, attendance_upload_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('attendance/', attendance_view, name="attendance"),
    path('attendance_upload/', attendance_upload_view, name="attendance_upload")
    
]