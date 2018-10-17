from django.shortcuts import render
from
# Create your views here.
def draft(request):
    if request.method == "POST":
        if "forward" in request.POST:
            print('Do something')
