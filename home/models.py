from django.db import models

# Create your models here.
class Employee(models.Model):
    project = models.IntegerField(default=0)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bank_account = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    from_date=models.DateField()
    to_date=models.DateField()

class RndAdmin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=30)