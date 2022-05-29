from django.urls import path
from .views import survey_view, survey_upload_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('survey/', survey_view, name="survey"),
    path('survey_upload/', survey_upload_view,name="survey_upload")
    # path('clickgroup/',clickgroup_view, name="clickgroup")
    # path('image_upload/',profile_image,name="profile_filled")
    
]