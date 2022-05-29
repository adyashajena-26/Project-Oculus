from django.http import JsonResponse
from django.shortcuts import render , redirect
from attendance.utils import decodeDesignImage
from .utils import count_fingers, emotion
from datetime import datetime
import os
# Create your views here.
def survey_view(request):
    if request.user.is_authenticated:

        return render (request,'pages/survey.html')
    else:
        return render("login")

def survey_upload_view(request):
    if request.user.is_authenticated:
        if request.is_ajax and request.method=="POST":
            img = request.POST['imgBase64']
            
            _, file_path = decodeDesignImage(img,'survey_photos',request.user.username)
            count = count_fingers(file_path)
            emo = emotion(file_path)
            msg = {'count':count,'emotion':emo}
            
            return JsonResponse(msg)
        else:
            return redirect("login")
    else:
        return redirect("login")