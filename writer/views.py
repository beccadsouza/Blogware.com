from django.shortcuts import render
from drafts.models import drafts
from users.models import Users
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

now  = datetime.datetime.now()
now = list(str(now).split())[0]
def draft(request):
    if request.method == "POST":
        d = drafts.objects.filter(id = request.POST.get('doc_id'))[0]
        user = Users.objects.filter(username = request.POST.get('user'))[0]
        if "forward" in request.POST:
            print('Do something')
            d.status = 2
            d.save()
            return render(request, 'writer/draftsview.html/',{ 'docs': drafts.objects.filter(status = 1, author = user.username), 'user' : user.username})
        elif "edit" in request.POST:
            print('redirect to editing document')
            return render(request, 'writer/editdraft.html/',{ 'doc' : d , 'user' : user.username, 'stance' : "edit" })


def newdraft(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        return render(request, 'writer/editdraft.html',{ 'user' : user, 'stance' : "new" })


def caterreq(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        
        if request.POST.get('stance') == 'edit':
            d = drafts.objects.filter(id = request.POST.get('doc_id'))[0]
            d.title = request.POST.get('Title')
            d.body = request.POST.get('Body')
            if request.POST.get('thumbnail'):
                thumb = request.FILES['thumbnail']
                fs = FileSystemStorage()
                filename  = fs.save(thumb.name, thumb)
                turl = fs.url(filename)
                d.thumbnail = turl
            d.date_of_update = now
            d.save()
        else:
            d = drafts()
            thumb = request.FILES['thumbnail']
            fs = FileSystemStorage()
            filename  = fs.save(thumb.name, thumb)
            turl = fs.url(filename)
            d.title = request.POST.get('Title')
            d.body = request.POST.get('Body')
            d.thumbnail.url = turl
            d.author = user
            d.status = 1
            d.date_of_update = now
            d.date_of_publish = now
            d.slug = '-'.join(list(d.title.split()))
            d.save()

        
        return render(request, 'writer/draftsview.html',{ 'docs' : drafts.objects.filter(status = 1, author = user) , 'user' : user})