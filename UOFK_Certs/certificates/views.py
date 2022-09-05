from multiprocessing import context
from os import name
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *


def home(request):
    return render(request, 'certificates/home.html')
# Create your views here.


def universityNumberCheck(request):
    students = Student.objects.all().values()
    if request.method == 'POST':
        uni_num = request.POST.get('uni_num')
        student1= Student.objects.filter(university_number=uni_num)
        if (student1):
            print('GET IT')
        else:
            print('NOT FOUND')
    context = {'students': students}
    return render(request, 'certificates/new_cert_req.html',context=context)


def trackCertReq(request):
    return render(request, 'certificates/track_cert_req.html')


def createReq(request,uni_num):

    student = Student.objects.get(university_number=uni_num)

    context= {'student':student}

    return render(request,'certificates/req_form.html')