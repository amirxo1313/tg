from django.db import models
from home.models import Account
# Create your models here.

class Transaction(models.Model):
    
    date = models.DateTimeField(auto_created=True)
    amount = models.FloatField()
    tranasction_types =[
        ('S','Store_shopping'),
        ('C','CardToCard'),
        ('Ch','Charge'),
        ('O','Online_shopping')
    ]
    
    account = models.ForeignKey(to=Account , on_delete=models.PROTECT , related_name="Account_Transaction")
    
    title = models.CharField(
        max_length=50,
        choices =tranasction_types,
        default='C')
    


