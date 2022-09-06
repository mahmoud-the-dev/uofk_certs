from django.shortcuts import render
from django.contrib.auth.decorators import login_required




def login(request):
    return render(request, 'employee/p2.html')

def verify(request):
    return render(request, 'employee/p1.html')

@login_required(login_url='employee login')
def home(request):
    return render(request, 'employee/p1.html')

@login_required(login_url='employee login')
def menu(request):
    return render(request, 'employee/p4.html')

@login_required(login_url='employee login')
def certificate_settings(request):
    return render(request, 'employee/p5.html')

@login_required(login_url='employee login')
def manage_certificate_requests(request):
    return render(request, 'employee/p6.html')

@login_required(login_url='employee login')
def add_certificate(request):
    return render(request, 'employee/p7.html')

@login_required(login_url='employee login')
def update_certificate(request):
    return render(request, 'employee/p8.html')

    
