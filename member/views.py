from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            messages.warning(request,"username already exists!")
            return HttpResponseRedirect(request.path_info)
        

        user_obj = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user_obj.set_password(password)
        user_obj.save()
        print(user_obj.username, user_obj.password)
        user_auth = authenticate(username=user_obj.username, password=password)
        print(user_auth)
        if user_auth:
            login(request, user_auth)
            return redirect('home')

    return render(request,'member/register.html')


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            messages.warning(request,"Account not found!")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username=username, password=password)

        if user_obj:
            login(request,user_obj)
            return redirect(reverse('home'))
        
    return render(request, 'member/login.html')

@login_required
def user_logout(response):
    logout(response)
    return redirect(reverse('login'))

