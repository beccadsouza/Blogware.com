from django.shortcuts import render,redirect,HttpResponse
from drafts.models import drafts
from users.models import Users
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
# Create your views here.


@login_required(login_url = '/users/login/')

def draftsview(request):
    if Users.objects.filter(username = get_user(request).username)[0].usertype != 'moderator':
        return HttpResponse('You are not authorised to access this page')
    else:
        d = drafts.objects.filter(status = 2)
        user  = request.POST.get('user')
        return render(request, 'moderator/drafts.html', {'docs' : d, 'user': user})

    
def draftdetails(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        d = drafts.objects.filter(id = request.POST.get('doc_id'))[0]
        if "edit" in request.POST:
            
            
            return render(request, 'moderator/editdraft.html', {'doc' : d, 'user' : user})
        else:
            
            d.status = 3
            d.save()
            return redirect('/moderator/draftsview')
            #return render(request,'moderator/drafts.html',{ 'docs' : drafts.objects.filter(status = 2), 'user' : user })
    else:
        return HttpResponse('Invalid Request Or You are not authorised to access this page')


def edit(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        d = drafts.objects.filter(id = request.POST.get('doc_id'))[0]
        if d.title != request.POST.get('Title'):
                temp = drafts.objects.filter(title = request.POST.get('Title')).order_by('-slug')
                snum = 1
                if temp:
                    slist = list(temp[0].slug.split('-'))
                    snum = int(slist[len(slist) - 1]) + 1
                d.slug = '-'.join(list(request.POST.get('Title').split())) + '-' + str(snum)
        d.title = request.POST.get('Title')
        print(request.POST.get('Title'))
        d.body = request.POST.get('Body')
        print(request.POST.get('Body'))
        d.save()
        return redirect('/moderator/draftsview')
        #return render(request, 'moderator/drafts.html', {'docs' : drafts.objects.filter(status = 2), 'user' : user})
    else:
        return HttpResponse('Invalid Request Or You are not authorised to access this page')
