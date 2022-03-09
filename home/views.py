from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import EmailMessage
import random



sentOTP=0
userEmail=''

def home(req):
    return render(req, 'home.html')

def getOTP(req):
    if req.method == 'POST':
        email = req.POST['email']
        otp = random.randint(100000, 999999)
        sentOTP=otp
        userEmail=email
        # msg = EmailMessage('Reset OTP',
        #                    f'OTP is : {otp}', to=[email])
        # msg.send()
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
    elif req.user.is_authenticated:
        return redirect('home')
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
        print(sentOTP)

        # if User.objects.filter(email=userEmail).exists() and user_otp == sentOTP and new_passwd != '':
        #     user = User.objects.get(email__exact=userEmail)
        #     print(user)
        #     user.set_password(new_passwd)
        #     user.save()
        #     messages.info(req, 'Password Reset Successfully')
        #     return redirect("login")
        # else:
        #     messages.info(req, 'wrong credentials properly')

    return render(req, 'changepasswd.html')
