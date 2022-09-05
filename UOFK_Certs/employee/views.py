from django.shortcuts import render


def home(request):
    return render(request, 'employee/p1.html')



def login(request):
    return render(request, 'employee/p2.html')


def verify(request):
    return render(request, 'employee/p3.html')

    
def menu(request):
    return render(request, 'employee/p4.html')


def certificate_settings(request):
    return render(request, 'employee/p5.html')

def manage_certificate_requests(request):
    return render(request, 'employee/p6.html')

def add_certificate(request):
    return render(request, 'employee/p7.html')

def update_certificate(request):
    return render(request, 'employee/p8.html')

    
