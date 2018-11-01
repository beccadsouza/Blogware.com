from django.shortcuts import render,redirect
from drafts.models import drafts
from users.models import Users
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from .forms import Newform
from drafts.models import drafts
now  = datetime.datetime.now()
now = list(str(now).split())[0]
# Create your views here.
@login_required(login_url = '/users/login/')

def draft(request):
    if request.method == "POST":
        d = drafts.objects.filter(id = request.POST.get('doc_id'))[0]
        user = get_user(request)
        if "forward" in request.POST:
            print('Do something')
            d.status = 2
            d.save()
            return redirect('/writer/viewdrafts/')
            #return render(request, 'writer/draftsview.html/',{ 'docs': drafts.objects.filter(status = 1, author = user.username), 'user' : user.username})
        elif "edit" in request.POST:
            print('redirect to editing document')
            return render(request, 'writer/editdraft.html/',{ 'doc' : d , 'user' : user.username, 'stance' : "edit" })
        else:
            drafts.objects.filter(id = request.POST.get('doc_id')).delete()
            return redirect('/writer/viewdrafts')

def newdraft(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        return render(request, 'writer/editdraft.html',{ 'user' : user, 'stance' : "new" })


def caterreq(request):#addition and editing the drafts using html
    if request.method == 'POST':
        user = Users.objects.filter(username = get_user(request))[0]
        
        if request.POST.get('stance') == 'edit':
            d = drafts.objects.filter(id = request.POST.get('doc_id'))[0]
            if d.title != request.POST.get('Title'):
                temp = drafts.objects.filter(title = request.POST.get('Title')).order_by('-slug')
                snum = 1
                if temp:
                    slist = list(temp[0].slug.split('-'))
                    snum = int(slist[len(slist) - 1]) + 1
                d.slug = '-'.join(list(request.POST.get('Title').split())) + '-' + str(snum)
            d.title = request.POST.get('Title')
            d.body = request.POST.get('Body')
            d.date_of_update = now
            d.save()
        else:
            d = drafts()
            d.title = request.POST.get('Title')
            d.body = request.POST.get('Body')
            d.thumbnail = drafts.objects.filter(title = '2016130024')[0].thumbnail
            d.author = user.username
            d.status = 1
            d.date_of_update = now
            d.date_of_publish = now
            snum = 1
            temp = drafts.objects.filter(title = request.POST.get('Title')).order_by('-slug')
            if temp:
                slist = list(temp[0].slug.split('-'))
                snum = int(slist[len(slist) - 1]) + 1
            d.slug = '-'.join(list(d.title.split())) + '-' + str(snum)
            d.save()

        
        #return render(request, 'writer/draftsview.html',{ 'docs' : drafts.objects.filter(status = 1, author = user) , 'user' : user})
        return redirect('/writer/viewdrafts/')





def viewdrafts(request):
    return render(request, 'writer/draftsview.html', { 'docs' : drafts.objects.filter(author = get_user(request).username, status = 1), 'user' : request.POST.get('username') })


def new(request):#addition of new draft with Djangoforms
    if request.method == 'POST':
        print('do something')
        d = drafts()
        form = Newform(request.POST)
        d.title = form.title
        d.body = 'hfhdufghsudh'
        d.thumbnail = form.thumb
        d.slug = '-'.join(list(d.title.split()))
        d.author = get_user(request).username
        d.date_of_update = now
        d.date_of_publish = now
        d.save()
        return redirect('/writers/viewdrafts/')
        
    else:
        print('Working till here')
        form = Newform()
        return render(request,'writer/new.html/', { 'form': form })

