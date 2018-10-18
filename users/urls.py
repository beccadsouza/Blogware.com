from django.contrib import admin
from django.urls import path
from  . import views


urlpatterns = [
    path('login/', views.login1),
    path('signup/', views.signup),
    path('logout/',views.logout1),
    path('addmoderator/',views.addmoderator),
]
