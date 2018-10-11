from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Users,User
import django.contrib.auth as auth
# Create your views here.


def login(request):
    if request.method == "POST":
        print("Do something")
        u = Users()
        
        u = list(Users.objects.filter(username = request.POST.get('username')))[0]

        
        if u.check_password(request.POST.get('password')):
            #u.is_authenticated = True
            return HttpResponse('login is successful')#render(request, '/writer/homepage.html')
        

        else:
            return redirect('/users/login/')

        
    else:
        return render(request,'users/login.html')

def signup(request):
    if request.method == "POST":
        print("Do something")
        u = Users()
        users = Users.objects.filter(username = request.POST.get('username'))

        if users:
            return redirect('/users/login/')
        else:
            u.username = request.POST.get('username')
            u.set_password(request.POST.get('password'))
            u.first_name = request.POST.get('name')
            u.usertype = 'Writer'
            u.save()
            return redirect('/users/login/')
    else:
        return render(request,'users/signup.html')


def logout(request):
    return redirect('/users/login/')