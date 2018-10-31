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
    return render(request,'drafts/articleview.html',{'doc' : d})