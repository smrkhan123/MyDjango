from django.urls import path
from . import views

urlpatterns = [
    path('addcom/',views.addcom,name="addcom"),
    path('addmob/',views.addmob,name="addmob"),
    path('moblist/',views.moblist,name="moblist"),
    path('mobdet/<int:id>/',views.mobdet,name="mobdet"),
    path('filmob/',views.filmob,name="filmob"),
    path('cfilmob/',views.cfilmob,name="cfilmob"),
    path('addcart/<int:id>/',views.addcart,name="addcart"),
    path('cartrem/<int:id>/',views.cartrem,name="cartrem"),
    path('viewcart/',views.viewcart,name="viewcart"),
]
