from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Users,User
import django.contrib.auth as auth
from drafts.models import drafts
from django.contrib.auth import login, logout
# Create your views here.


def login1(request):
    if request.method == "POST":
        print("Do something")
        u = Users()
        
        u = list(Users.objects.filter(username = request.POST.get('username')))[0]

        
        if u.check_password(request.POST.get('password')):
            #u.is_authenticated = True
            login(request,u)
            if u.usertype == 'Writer':
                return render(request, 'writer/draftsview.html', { 'docs' : drafts.objects.filter(author = request.POST.get('username'), status = 1), 'user' : request.POST.get('username') })
            elif u.usertype == 'moderator':
                return(render, '/moderator/drafts.html', { 'docs' : drafts.objects.filter(status = 2), 'user' : u.username })

        

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


def logout1(request):
    logout(request)
    return redirect('/users/login/')