from django.urls import path
from . import views

urlpatterns = [
    path('addcus/',views.addcus,name="addcus"),
    path('cuslist/',views.cuslist,name="cuslist"),
    path('cusdetail/<str:u>/',views.cusdetail,name="cusdetail"),
]
