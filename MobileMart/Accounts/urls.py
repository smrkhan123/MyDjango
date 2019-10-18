from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginview,name="login"),
    path('signup/',views.signupview,name="signup"),
    path('editpro/',views.editpro,name="editpro"),
    path('logout/',views.logoutview,name="logout"),
]
