from django.shortcuts import render
from .models import drafts
# Create your views here.

def articledisp(request):
    draft = drafts.objects.filter(status = 4)

    return render(request, 'drafts/articledisp.html', {
        'docs' : draft
     })
    
def articleview(request):
    print('This is ship')