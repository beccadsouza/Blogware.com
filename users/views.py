from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Users,User
import django.contrib.auth as auth
from drafts.models import drafts
from django.contrib.auth import login, logout,get_user
from .models import Users
# Create your views here.


def login1(request):
    if request.method == "POST":
        
        u = Users()
        print("The code runs well")
        u = list(Users.objects.filter(username = request.POST.get('username')))[0]
        print("The code runs well")
        
        if u.check_password(request.POST.get('password')):
            #u.is_authenticated = True
            print("Do something")
            login(request,u)
            print("The code runs well")
            if u.usertype == 'Writer':
                return render(request, 'writer/draftsview.html', { 'docs' : drafts.objects.filter(author = request.POST.get('username'), status = 1), 'user' : request.POST.get('username') })
            elif u.usertype == 'moderator':
                print("The code runs well")
                return render(request, 'moderator/drafts.html', { 'docs' : drafts.objects.filter(status = 2), 'user' : u.username })
            else:
                return redirect('/admins/draftsview')

        

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


def addmoderator(request):
    if Users.objects.filter(username = get_user(request).username)[0].usertype != 'admin':
        return redirect('/drafts/articleview/')
    else:
        if request.method == "POST":
            print("Do something")
            u = Users()
            users = Users.objects.filter(username = request.POST.get('username'))

            if users:
                return redirect('/admin/draftsview/')
            else:
                u.username = request.POST.get('username')
                u.set_password(request.POST.get('password'))
                u.first_name = request.POST.get('name')
                u.usertype = 'moderator'
                u.save()
                return redirect('/admins/draftsview/')
        else:
            return render(request,'users/modsignup.html')

def logout1(request):
    logout(request)
    return redirect('/users/login/')