from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^articlelist/$',views.artlist,name="artlist"),
   url(r'^artdetail(?P<pk>[\d]+)/$',views.artdetail,name="artdetail"),
   url(r'^artdelete(?P<pk>[\d]+)/$',views.artdelete,name="artdelete"),
   url(r'^artcreate/$',views.artcreate,name="artcreate"),
   url(r'^artupdate(?P<pk>[\d]+)/$',views.artupdate,name="artupdate"),

]
