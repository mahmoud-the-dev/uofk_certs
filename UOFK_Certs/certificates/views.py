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
        student= Student.objects.filter(university_number=uni_num).values()
        if (student):
            request.session['uni_num'] = int(uni_num)
            return redirect('/new_request',uni_num=uni_num)
        else:
            print('NOT FOUND')
    context = {'students': students}
    return render(request, 'certificates/new_cert_req.html',context=context)


def trackCertReq(request):
    return render(request, 'certificates/track_cert_req.html')


def createReq(request):
    uni_num= request.session['uni_num']
    student = Student.objects.get(pk=uni_num)


    completed_levels = student.completedlevel_set.all()

    levels = []

    for level in completed_levels:
        this_level=Level.objects.get(level=level.level)
        types = this_level.leveltypelink_set.all()
        this_types = []
        for type in types:
            this_type=CertificateType.objects.get(type=type.certificate_type)
            languages = this_type.typelanguage_set.all()
            this_languages = []
            for language in languages:
                this_language= language.language
                this_languages.append(this_language)
            dict1 =[this_type,this_languages]
            this_types.append(dict1)
        dict2 = [this_level,this_types]
        levels.append(dict2)

    context= {'levels':levels}
    return render(request,'certificates/req_form.html',context=context)