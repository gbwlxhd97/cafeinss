from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib.auth.views import LogoutView
from django.conf import settings


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        email = request.POST['email']
        user = auth.authenticate(request, username=username, password=password, email=email)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorect'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password2'],
            )
            auth.login(request, user)
            return redirect('index')
    return render(request, 'signup.html')

class LogoutViews(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL



logout = LogoutViews.as_view()


