from django.shortcuts import render,redirect
from .models import EmpAttendance
import os
from django.http import JsonResponse
from .utils import compare_two_face, decodeDesignImage
from .utils import check_spoof, give_excel
from datetime import datetime
from attendance.models import EmpAttendance
# Create your views here.
def attendance_view(request):
    
    if request.user.is_authenticated:     
        return render(request,'pages/attendance.html')
    else:
        return redirect("login")

def download_view(request):
    if request.user.is_authenticated:
        return render(request,"pages/download.html")
    else:
        return redirect("login")
        
def download_attendance_view(request):
    if request.user.is_authenticated:  
        attendance = EmpAttendance.objects.values_list()
        if request.method == 'POST':
            date = request.POST['date']
            
            d = date[8:]
            m = date[5:-3]
            
            print(d,m)
            give_excel(d,m,attendance)
            msg = {"d":True}
            return render(request,"pages/download.html",context=msg)
    else:
        return redirect("login")


def attendance_upload_view(request):
    if request.user.is_authenticated:
        if request.is_ajax and request.method=='POST':
            image_data = request.POST['imgBase64']

            if len(list(request.user.empattendance_set.all())) > 0:
                profile = list(request.user.empattendance_set.all())[-1].uploaded_pic.url[1:]
            else:
                profile = request.user.empprofile_set.values()[0]['profile_image']
    
            img, new_image_path = decodeDesignImage(image_data,'attendance_images', request.user.username)
            print(profile, new_image_path)
            face_verify = compare_two_face(profile, new_image_path)
            print(face_verify)
            real = check_spoof(new_image_path)
            if real==False:
                msg={'out': "Spoof image uploaded"}
            

            elif face_verify==1:
                Attobj = EmpAttendance(uploaded_pic = img, user =request.user)
                Attobj.save()

                msg = {'out':"Attendance Taken"}
            elif face_verify==0:
                msg = {'out':"Face doesnt match"}
            else:
                msg = {'out': "Go to a lighted area"}
               
            os.remove(new_image_path)
            return JsonResponse(msg)
        else:
            return redirect("profile")
    else:
        return redirect("login")
    