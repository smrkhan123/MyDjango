from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('destinations',views.destinations,name='destinations'),
    path('elements',views.elements,name='elements'),
    path('news',views.news,name='news'),
    path('contact',views.contact,name='contact'),
    path('update/<id>',views.update,name='update'),
    path('delete/<id>',views.delete,name='delete'),
    path('insert',views.insert,name='insert'),
]
