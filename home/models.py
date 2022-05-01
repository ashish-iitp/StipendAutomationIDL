import email
from tkinter import CASCADE
from click import password_option
from django.db import models
from django.forms import EmailField
from django.contrib.auth.models import User

PROFRSSOR_CHOICES = (
        ("test1@gmail.com","test1@gmail.com"),
        ("test2@gmail.com","test2@gmail.com"),
        ("test3@gmail.com","test3@gmail.com"),
        ("test4@gmail.com","test4@gmail.com")
    )
# Create your models here.
class Faculty(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.email

class Employee(models.Model):
   
    project = models.IntegerField(default=0)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bank_account = models.IntegerField(default=0)
    ifsc = models.CharField(max_length=30)
    phone = models.IntegerField(default=0)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    from_date=models.DateField()
    to_date=models.DateField()
    professors = models.CharField(max_length=50,choices=PROFRSSOR_CHOICES)
    # a=(("1","one" ),("2","two"),("3","three"))
    # prof=models.ChoiceField(choices=a)
    salary=models.IntegerField(default=0)

    approve = models.CharField(max_length=20,default="Hold")
    # faculty_email = models.ForeignKey(Faculty, on_delete= CASCADE, null= True, blank= True)

    def __str__(self):
        return str(self.first_name)

class RndAdmin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=30)


# class Faculty(models.Model):
#     id = models.AutoField()
#     email = models.EmailField()
#     password = models.CharField(max_length=50)

    # def __str__(self) -> str:
    #     return super().__str__()