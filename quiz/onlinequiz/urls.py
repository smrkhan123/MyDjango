from django.urls import path
from .import views
urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('register/', views.register,name='register'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('manage_users/', views.manage_users,name='manage_users'),
    path('manage_questions/', views.manage_questions,name='manage_questions'),
    path('change_password/', views.change_password,name='change_password'),
    path('quiz/', views.quiz,name='quiz'),
    path('delete/<id>', views.delete,name='delete'),
    path('add_question/', views.add_question,name='add_question'),
    path('edit_question/<id>', views.edit_question,name='edit_question'),
    path('delete_question/<id>', views.delete_question,name='delete_question'),
    path('edit_user/<id>', views.edit_user,name='edit_user'),
    path('delete_user/<id>', views.delete_user,name='delete_user'),
    path('result/', views.result,name='result'),
]
