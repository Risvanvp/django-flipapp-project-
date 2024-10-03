from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pic/customerprofilepic/',null=True)
    address=models.CharField(max_length=40) 
    address=models.CharField(max_length=20,null=False) 

