from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home,name="home"),
    url(r'^about/$', views.about,name="about"),
    url(r'^article/', include('Article.urls')),
]