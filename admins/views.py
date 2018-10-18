from django.shortcuts import render, redirect
from django.contrib.auth import get_user
from drafts.models import drafts
# Create your views here.
def approve(request):
    if request.method == 'POST':
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


def draftsview(request):
    return render(request, 'admins/draftview.html', {  'docs' : drafts.objects.filter(status = 3) })
        

def draftread(request):
    if request.method == 'POST':
        return render(request, '/admins/draftread.html', { 'doc' : drafts.objects.filter(id = request.POST.get('doc_id')) })