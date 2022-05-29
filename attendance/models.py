from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmpAttendance(models.Model):
    date_taken = models.DateTimeField(auto_now_add=True)
    uploaded_pic = models.ImageField(upload_to = 'uploadedImages',null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    no_of_days = models.IntegerField(default=0,blank=True,null=True)