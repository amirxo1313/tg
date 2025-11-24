from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)


class Account(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=10)
    amount = models.FloatField(default=0)



class Profit(models.Model):
    PROFIT_TYPE_CHOICES = [
        ('monthly', 'Monthly'),
        ('annually', 'Annually'),
    ]
    date = models.DateField(auto_now=True)
    account = models.ForeignKey(
        to=Account, on_delete=models.CASCADE, related_name="Account_Profit"
    )
    profit_type = models.CharField(max_length=10, choices=PROFIT_TYPE_CHOICES, default='monthly')
    


