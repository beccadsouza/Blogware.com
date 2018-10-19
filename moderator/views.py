from django.shortcuts import render,redirect
from drafts.models import drafts
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url = '/users/login/')

def draftsview(request):
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


def edit(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        d = drafts.objects.filter(id = request.POST.get('doc_id'))[0]
        d.title = request.POST.get('Title')
        print(request.POST.get('Title'))
        d.body = request.POST.get('Body')
        print(request.POST.get('Body'))
        d.save()
        return redirect('/moderator/draftsview')
        #return render(request, 'moderator/drafts.html', {'docs' : drafts.objects.filter(status = 2), 'user' : user})
