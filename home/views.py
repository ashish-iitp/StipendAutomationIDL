from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'username already exists please login')
            return redirect('login')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email already exists please login')
            return redirect('login')

        else:
            if password1 == password2:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=fname, last_name=lname)
                user.save()
                messages.info(request, 'account created for' + ' '+username)
                return redirect('login')
            else:
                messages.info(request, 'password not matching')
                return redirect('register')
    elif request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect("login")
    else:
        return render(request, 'login.html')


def logout_user(req):
    logout(req)
    return redirect('login')
