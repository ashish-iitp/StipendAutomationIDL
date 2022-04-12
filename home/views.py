from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import EmailMessage
import random
from home.models import *



sentOTP = 0
userEmail = ''


def home(req):
    return render(req, 'home.html')

def getOTP(req):
    if req.method == 'POST':
        global sentOTP, userEmail
        email = req.POST['email']
        otp = random.randint(100000, 999999)
        sentOTP = otp
        userEmail = email
        msg = EmailMessage('Reset OTP',
                           f'OTP is : {otp}', to=[email])
        msg.send()
        return redirect('changepasswd')

    return render(req, 'getotp.html')


def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['email']
        password1 = req.POST['password1']
        password2 = req.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(req, 'username already exists please login')
            return redirect('login')
        elif User.objects.filter(email=email).exists():
            messages.info(req, 'email already exists please login')
            return redirect('login')

        else:
            if password1 == password2:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=fname, last_name=lname)
                user.save()
                messages.info(req, 'account created for' + ' '+username)
                return redirect('login')
            else:
                messages.info(req, 'password not matching')
                return redirect('register')
    
    else:
        return render(req, 'register.html')


def login_user(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            messages.info(req, 'Username OR password is incorrect')
            return redirect("login")
    else:
        return render(req, 'login.html')


def logout_user(req):
    logout(req)
    return redirect('login')


def change_passwd(req):
    if req.method == 'POST':
        user_otp = int(req.POST['otp'])
        new_passwd = req.POST['newpasswd']
        print(userEmail)

        if User.objects.filter(email=userEmail).exists() and user_otp == sentOTP and new_passwd != '':
            user = User.objects.get(email__exact=userEmail)
            print(user)
            user.set_password(new_passwd)
            user.save()
            messages.info(req, 'Password Reset Successfully')
            return redirect("login")
        else:
            messages.info(req, 'wrong credentials properly')

    return render(req, 'changepasswd.html')


def add_emp(req):
    if req.method == 'POST':
        project = int(req.POST['project'])
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        bank_account = int(req.POST['bank_account'])
        phone = int(req.POST['phone'])
        email = req.POST['email']
        password=req.POST['password']
        from_date = req.POST['from_date']
        to_date = req.POST['to_date']
        new_emp=Employee(project=project,first_name=first_name,last_name=last_name,bank_account=bank_account,phone=phone,email=email,password=password,from_date=from_date,to_date=to_date)
        new_emp.save()
        return HttpResponse("Employee Added Succesfully!")
    else:
        return render(req, 'add_emp.html')



            