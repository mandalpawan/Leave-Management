from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class employee(models.Model):
    content = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)


class leavetype(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class applyleave(models.Model):
    #==============================
    
    leave = models.ForeignKey(leavetype,on_delete=models.CASCADE)
    holidayfrom = models.DateField(auto_now_add = False,auto_now=False,blank=False,default=datetime.date.today)
    holidayto = models.DateField(auto_now_add = False,auto_now=False,blank=False,default=datetime.date.today)
    detail = models.TextField()
    publish_date = models.DateField(auto_now_add=True)
    varify = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.detail
    #====================================


    