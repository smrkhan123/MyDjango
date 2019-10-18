from django.urls import path
from . import views

urlpatterns = [
    path('addpay/',views.addpay,name="addpay"),
]
