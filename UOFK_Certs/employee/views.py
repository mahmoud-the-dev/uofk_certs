from random import randint
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from certificates.models import *


def adlogin(request):
    return render(request, 'employee/second_login.html')

def verify(request):
    return render(request, 'employee/passcode.html')

# @login_required(login_url='employee login')
def home(request):
    return render(request, 'employee/first_login.html')

def menu(request):
    return render(request, 'employee/employee_menu.html')

# @login_required(login_url='employee login')
def certificate_settings(request):
    return render(request, 'employee/certificate_settings.html')

def ManageCertificateRequests(request):
    requests = CertificateRequest.objects.all()
    context = {'requests': requests}
    return render(request, 'employee/.html',context)


def ViewRequest(request):
    certs = CertificateItem.objects.get() 
    context = {
        'certs': certs
    }
    return render(request, 'employee/request.html',context)

# @login_required(login_url='employee login')
def add_certificate(request):
    return render(request, 'employee/new_certificate.html')

# @login_required(login_url='employee login')
def update_certificate(request):
    return render(request, 'employee/update_certificate.html')
