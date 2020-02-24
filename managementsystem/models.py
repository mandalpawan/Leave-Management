from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class catagory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class department(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class college(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class extendemp(models.Model):
    
    catagory = models.ForeignKey(catagory,on_delete=models.CASCADE)
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    

    
