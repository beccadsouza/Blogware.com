from django.shortcuts import render,redirect
from django.http import HttpResponse


def red(request):
    return redirect('/drafts/articledisp')