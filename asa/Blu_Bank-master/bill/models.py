


from django.db import models
from home.models import Account
# Create your models here.


class Bill(models.Model):
     
     bill_number = models.IntegerField(unique=True)
     amount = models.FloatField()
     bill_types = [
         
         ("W","water"),
         ("C","cellphone"),
         ("E","Electicity"),
         ("G","Gas")
         
     ]
     title = models.CharField(max_length=10,choices=bill_types , default="C")
     phonenumber = models.CharField(max_length=10)
     date = models.DateTimeField(auto_created=True)
     account = models.ForeignKey(to=Account, on_delete=models.PROTECT , related_name="Account_Bill")
     



     