from django.contrib import admin
from django.urls import path,include
from users import urls
from  . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'caterreq/', views.caterreq),
    path(r'draft/',views.draft),
    path(r'newdraft/',views.newdraft),#draft Creation function
    path(r'viewdrafts/',views.viewdrafts),
    #path(r'')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
