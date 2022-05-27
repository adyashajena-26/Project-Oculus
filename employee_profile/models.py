from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class EmpProfile(models.Model):
    profile_image = models.ImageField(upload_to = 'ProfileImages',null=True)
    Dob = models.DateField(default = datetime.date.today,max_length=8)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    attendance = models.IntegerField(default=0, blank = True, null=True)
