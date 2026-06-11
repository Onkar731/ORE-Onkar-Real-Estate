from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from contacts.models import Contact

def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"{username} has logged in successfully!")
            return redirect('accounts:dashboard')

        messages.error(request, "Invalid credentials")
        return redirect('accounts:login')

    return render(request, 'accounts/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 != password2:
            messages.error(request, "Password does not match")
            return redirect('accounts:register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username not available")
            return redirect('accounts:register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email not available")
            return redirect('accounts:register')
        
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
        
        if user:
            messages.success(request, f"{username} has been registered successfully!")
            return redirect('accounts:login')

    return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        user = request.user
        auth_logout(request)
        messages.success(request, f"{user} has logged out!")
        return redirect('accounts:login')

def dashboard(request):
    inquired_listings = Contact.objects.filter(user_id=request.user.id)

    context = {
        'inquired_listings': inquired_listings
    }
    return render(request, 'accounts/dashboard.html', context)