from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('contact/', views.contact,name='contact'),
    path('news/', views.news,name='news'),
    path('newproducts/', views.newproducts,name='newproducts'),
    path('myaccount/', views.myaccount,name='myaccount'),
    path('location/', views.location,name='location'),
    path('shoppingcart/', views.shoppingcart,name='shoppingcart'),
    path('specialoffer/', views.specialoffer,name='specialoffer'),
    path('faq/', views.faq,name='faq'),
]
