from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('req',views.new_cert_req),
    path('track_req',views.track_cert_req),
]