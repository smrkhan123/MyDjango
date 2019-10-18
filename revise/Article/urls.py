from django.conf.urls import url
from . import views

urlpatterns = [
   	url(r'^artlist/$',views.list,name='list'),
   	url(r'^detail(?P<pk>[\d]+)/$',views.detail, name='detail'),
   	url(r'^delete(?P<pk>[\d]+)/$',views.delete, name='delete'),
   	url(r'^create/$',views.create, name='create'),
   	url(r'^update(?P<pk>[\d]+)/$',views.update, name='update'),
]
