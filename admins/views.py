from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import get_user
from drafts.models import drafts
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from users.models import Users

# Create your views here.
@login_required(login_url = '/users/login/')

def approve(request):
    if request.method == 'POST' and Users.objects.filter(username = get_user(request).username)[0].usertype == 'admin':
        d = drafts.objects.filter(id = request.POST.get('doc_id'))[0]
        if 'approve' in request.POST:
            d.status = 4
            d.save()
            print(request.POST.get('doc_id'))
            return redirect('/admins/draftsview/')
        else:
            d.status = 1
            d.save()
            return redirect('/admins/draftsview/')
    else:
        return HttpResponse('You are Not Authorised to view this page')


def draftsview(request):
    return render(request, 'admins/draftview.html', {  'docs' : drafts.objects.filter(status = 3) })
        

def draftread(request):
    if request.method == 'POST'  and Users.objects.filter(username = get_user(request).username).usertype == 'admin':
        return render(request, '/admins/draftread.html', { 'doc' : drafts.objects.filter(id = request.POST.get('doc_id')) })
