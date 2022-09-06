from multiprocessing import context
from os import name
from unicodedata import decimal
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import datetime
from decimal import Decimal

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


    if request.method == 'POST':
        post_data = request.POST
        req = CertificateRequest(student=student,count=post_data['quantity'])
        level = Level.objects.get(level=post_data['level'])

        lang = Language.objects.get(language=post_data['lang'])
        type = CertificateType.objects.get(type=post_data['type'])

        typelang= LevelTypeLink.objects.filter(certificate_type=type,level=level)

        price=typelang[0].price * Decimal(int(post_data['quantity']))

        item = CertificateItem(level=level,language=lang,certificate_type = type,request=req,price = price,quantity=post_data['quantity'])
        bill = Bill(request=req,bill_price=price)
        req.save()
        item.save()
        bill.save()
        request.session['bill_code'] = str(bill.bill_code)
        return (redirect ('/show_bill'))


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

def showBill(request):
    print (request.session['bill_code'])
    code = request.session['bill_code']

    price = Bill.objects.get(pk=code).bill_price
    context = {'code':code,'price':price}
    return render(request ,'certificates/bill.html',context=context)