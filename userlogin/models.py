"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class offeringType(models.Model):
    # The different types of offerings
    # To be edited on the admin page
    offering_type=models.CharField(max_length=200)

class offers(models.Model):
    # Offerings of a person
    id_user=models.ForeignKey(User,on_delete=models.CASCADE)
    offering_text=models.CharField(max_length=500)
    offering_time=models.FloatField()
    offering_date=models.DateTimeField(auto_now_add=True)
    offering_buyers_id=models.IntegerField(default=0)
    offering_state=models.FloatField(default=0)
    # State: 0 = open, 1 = buyer interested, 2 = offer accepted on both sides, 3 = transaction finished


