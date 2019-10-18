from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sam/$',views.sam,name="sam"),
   
]
