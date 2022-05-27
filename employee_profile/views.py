from django.shortcuts import render,redirect

from employee_profile.models import EmpProfile
from .models import EmpProfile
# Create your views here.
def profile_view(request):
    if request.user.is_authenticated:

        return render(request,"pages/profile.html")
    else:
        redirect("login")

def profile_image(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            image = request.FILES['emp_img']
            image_name = str(image)
            obj = EmpProfile(profile_image = image, user =request.user)
            obj.save()
            return redirect('profile')
        else:
            return redirect('profile')
    else:
        return redirect("login")