from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'certificates/home.html')
# Create your views here.

def new_cert_req(request):
    return render(request, 'certificates/new_cert_req.html')

def track_cert_req(request):
    return render(request, 'certificates/track_cert_req.html')