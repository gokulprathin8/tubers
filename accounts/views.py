from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, 'You are logged in')
            auth.login(request, user)
            print(user)
            return redirect('dashboard')
        else:

            messages.error(request, 'Invalid Credentials!')
            return redirect('login')
        
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        user_name = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        
        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'Username exists already!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error('Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=user_name,
                                                    email=email, password=password)
                    user.save()
                    messages.success(request, "User Created Successfully")
                    return redirect('login')
        else:
            messages.warning(request, 'Password does not match')
            return redirect('register')

    return render(request, 'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')