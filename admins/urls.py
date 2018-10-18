from django.contrib import admin
from django.urls import path
from  . import views


urlpatterns = [
    path('draftsview/', views.draftsview),
    path('draftread/', views.draftsview),
    path('approve/',views.approve),
    #path('reject/',views.reject),
]
