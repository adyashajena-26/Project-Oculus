from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from attendance.views import attendance_upload_view
from .utils import decodeDesignImage, getFacesFromGroup, IdentifyFromGroup, produce_excel
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
            if 'data:' in group_image and ';base64,' in group_image:
                _,data = group_image.split(';base64,')
            img, image_pil = decodeDesignImage(data)
            user_name = request.user.username 
            current_time = datetime.now().timestamp()
            group_file_path = os.path.join('uploaded_group_photos',str(user_name)+str(current_time)+'.png')
           
            print(group_file_path)
            image_pil.save(group_file_path,'PNG')
            getFacesFromGroup(group_file_path, request.user.username)
            attendance_dict = IdentifyFromGroup("found_faces",users)
            print(attendance_dict)
            print("yahan")
            return render(request,'pages/group.html',context={'users':users,'sent':True,'attendance': attendance_dict})
        elif attendance_dict!={}:
            present=[]
            absent=[]
            print("aya")
            
            for key in attendance_dict:
                if attendance_dict[key]==1:
                    present.append(User.objects.get(username=key))
                else:
                    absent.append(User.objects.get(username=key))
            print("hi")
            produce_excel(present,absent)
            return render(request,'pages/group.html',context={'users':users,'sent':True,'present': present,'absent':absent})
        else:
            print(attendance_dict)
            print("yahin")

            return render(request,'pages/group.html',context={'users':users})
    else:
        return redirect("login")

def clickgroup_view(request):
    if request.user.is_authenticated:
        return render(request,'pages/groupattendance.html')
    else:
        return  redirect("login")