from django.shortcuts import render
from .models import drafts
# Create your views here.

def articledisp(request):
    draft = drafts.objects.filter(status = 4)

    return render(request, 'drafts/articledisp.html', {
        'docs' : draft
     })
    
def articleview(request,slug):
    d = drafts.objects.get(slug = slug)
    bodylist = list(d.body.split('\n'))
    return render(request,'drafts/articleview.html',{'doc' : d , 'body1' : bodylist})
