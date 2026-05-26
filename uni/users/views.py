from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import role_required

def login_view(request):
    if request.method == 'POST':
        # Your custom user uses phone_number instead of username!
        phone = request.POST.get('phone_number') 
        password = request.POST.get('password')
        
        user = authenticate(request, phone_number=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'error': 'Invalid phone number or password'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    return render(request, 'dashboard.html')