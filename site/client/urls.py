from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),    
    url(r'^sheet/(?P<idx>\d+)/$', views.sheet, name='sheet'),    
    url(r'^stato/(?P<idx>\d+)/$', views.stato, name='stato'),  
] 


