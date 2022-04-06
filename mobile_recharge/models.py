from pyexpat import model
from django.db import models

# Create your models here.

class recharge(models.Model):
    id=models.IntegerField(primary_key=True)
    number=models.CharField(max_length=10)
    provider=models.CharField(max_length=20)
    plans=models.CharField(max_length=100)


    def __str__(self):
        return self.id



