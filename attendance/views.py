from django.shortcuts import render,redirect
from .models import EmpAttendance
import os
from django.http import JsonResponse
from .utils import compare_two_face, decodeDesignImage

# Create your views here.
def attendance_view(request):
    if request.user.is_authenticated:     
        return render(request,'pages/attendance.html')
    else:
        return redirect("login")


def attendance_upload_view(request):
    if request.user.is_authenticated:
        if request.is_ajax and request.method=='POST':
            print("asila")
            image_data = request.POST['imgBase64']
            if 'data:' in image_data and ';base64,' in image_data:
                _,data = image_data.split(';base64,')
            
            if len(list(request.user.empattendance_set.all())) > 0:
                profile = list(request.user.empattendance_set.all())[-1].uploaded_pic.url[1:]
            else:
                profile=request.user.empprofile_set.values()[0]['profile_image']
                
            img = decodeDesignImage(data)

            if compare_two_face(profile,"image.png")==1:
                print("matched")
                Attobj = EmpAttendance(uploaded_pic = img, user =request.user)
                Attobj.save()
                msg = {'out':"Attendance Taken"}
            else:
                msg = {'out':"Face doesnt match"}
                print("not matched")
            os.remove("image.png")
            return JsonResponse(msg)
        else:
            return redirect("profile")
    else:
        return redirect("login")
    