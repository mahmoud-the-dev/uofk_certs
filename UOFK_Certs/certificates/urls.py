from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('check_uni_num',views.universityNumberCheck,name='check uni-num'),
    path('check_tr-code',views.trackCertReq, name='check tr-code'),
    path('new_request',views.createReq, name='request form'),
]