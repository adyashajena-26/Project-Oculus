from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from attendance.views import attendance_upload_view
from attendance.utils import decodeDesignImage
from .utils import getFacesFromGroup, IdentifyFromGroup, produce_excel
from datetime import datetime
import os
# Create your views here.
attendance_dict = {}
def group_view(request):
    global attendance_dict
   
    users = []
    for u in User.objects.all():
        users.append(u)
    if request.user.is_authenticated:
        if request.is_ajax and request.method=="POST":
            group_image = request.POST['imgBase64']
            
            img, group_file_path = decodeDesignImage(group_image,'uploaded_group_photos',request.user.username)
            getFacesFromGroup(group_file_path, request.user.username)
            attendance_dict = IdentifyFromGroup("found_faces",users)
            return render(request,'pages/group.html',context={'users':users,'sent':True,'attendance': attendance_dict})
        elif attendance_dict!={}:
            present=[]
            absent=[]
            
            for key in attendance_dict:
                if attendance_dict[key]==1:
                    present.append(User.objects.get(username=key))
                else:
                    absent.append(User.objects.get(username=key))
            produce_excel(present,absent)
            return render(request,'pages/group.html',context={'users':users,'sent':True,'present': present,'absent':absent})
        else:
            print(attendance_dict)
            return render(request,'pages/group.html',context={'users':users})
    else:
        return redirect("login")

def clickgroup_view(request):
    if request.user.is_authenticated:
        return render(request,'pages/groupattendance.html')
    else:
        return  redirect("login")