from django.http import JsonResponse
from django.shortcuts import render , redirect
from groupattendance.utils import decodeDesignImage
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
            group_image = request.POST['imgBase64']
            if 'data:' in group_image and ';base64,' in group_image:
                _,data = group_image.split(';base64,')
            img, image_pil = decodeDesignImage(data)
            user_name = request.user.username 
            current_time = datetime.now().timestamp()
            file_path = os.path.join('survey_photos',str(user_name)+str(current_time)+'.png')
            image_pil.save(file_path,'PNG')
            count = count_fingers(file_path)
            emo = emotion(file_path)
            msg = {'count':count,'emotion':emo}
            
            return JsonResponse(msg)
        else:
            return redirect("login")
    else:
        return redirect("login")