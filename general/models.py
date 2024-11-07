from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    mobile = models.CharField(max_length=40)
    query= models.CharField(max_length=200)


class loginModel(models.Model):
    aid=models.CharField(max_length=120)
    passwd=models.CharField(max_length=50)