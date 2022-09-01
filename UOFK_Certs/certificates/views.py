from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<a href="create_certificate">create certificate</a> <a href="track_certificate"> or track certificate </a>')
# Create your views here.
