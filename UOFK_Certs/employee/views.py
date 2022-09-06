from random import randint
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import View
from UOFK_Certs.certificates.models import CertificateItem, CertificateRequest






def home(request):
    return render(request, 'employee/p1.html')



def adlogin(request):
    return render(request, 'employee/p2.html')
  

def verify(request):
    return render(request, 'employee/p3.html')
  
def menu(request):
    return render(request, 'employee/p4.html')


def certificate_settings(request):
    return render(request, 'employee/p5.html')

class ManageCertificateRequests(View):
    requests = CertificateRequest.objects.get()
    context = {
        'object':requests
    }
    def get(self):
        return render(self.request, 'employee/p6.html',self.context)


class ViewRequest(View):
    certs = CertificateItem.objects.get() 
    context = {
        'object': certs
    }
    def get(self):
        return render(self.request, 'employee/p6_2.html',self.context)

def add_certificate(request):
    return render(request, 'employee/p7.html')

def update_certificate(request):
    return render(request, 'employee/p8.html')

    
