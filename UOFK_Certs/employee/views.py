from random import randint
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from certificates.models import *
from .forms import CertificateForm

def adlogin(request):
    if request.method == 'POST':
        req = request.POST
        return redirect('employee/passcode.html')
    return render(request, 'employee/second-login.html')

def verify(request):
    return render(request, 'employee/passcode.html')


def home(request):
    return render(request, 'employee/first_login.html')

def menu(request):
    return render(request, 'employee/employee_menu.html')


def certificate_settings(request):
    return render(request, 'employee/certificate_settings.html')

def ManageCertificateRequests(request):
    requests = CertificateRequest.objects.all().order_by('-created_at')
    context = {'requests': requests}
    return render(request, 'employee/requests.html',context)


def ViewRequest(request, pk):
    req = CertificateRequest.objects.get(pk=pk) 
    if request.method == 'POST':
        print (request)
        post= request.POST
        print (post.keys())
        if post['certificate_status']:
            for cert in req.certificateitem_set.all():
                cert.status = post['certificate_status']
                cert.save()
        if post['req_status']:
            req.request_status=post['req_status']
            req.save()
        return redirect(f'/employee/view-request/{pk}')
    context = {
        'req': req
    }
    return render(request, 'employee/request.html',context)


def add_certificate(request):
    form = CertificateForm()
    if request.method == 'POST':
        post = request.POST
        print(post)
    context = {'form':form}
    return render(request, 'employee/new_certificate.html',context)


def update_certificate(request):
    return render(request, 'employee/update_certificate.html')
