from django.db import models
import uuid
# Create your models here.

class Level(models.Model):
    LEVELS = (
        ('DIP','دبلوم'),
        ('HD','دبلوم عالي'),
        ('BCH','بكلاريوس'),
        ('M','ماجستير'),
        ('PHD','دكتوراة'),
    )
    level = models.CharField(max_length=255,choices=LEVELS)
    def __str__(self):
        return self.level


class Student(models.Model):
    university_number = models.CharField( max_length=25, unique=True,primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    batch = models.IntegerField()
    last_level = models.ForeignKey(Level,on_delete=models.DO_NOTHING)
    stage = models.IntegerField()
    def __str__(self):
        return self.name


class Language(models.Model):
    language = models.CharField(max_length=255)
    def __str__(self):
        return self.language



class CertificateType(models.Model):
    type = models.CharField(max_length=255)
    card_board = models.BooleanField()
    def __str__(self):
        return self.type


class CompletedLevel(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)# ForeignKey
    level = models.ForeignKey(Level,on_delete=models.CASCADE)#ForeignKey
    def __str__(self):
        return str(self.level) + " " + str(self.student)


class CertificateRequest(models.Model):

    REQUEST_STATUS= (('wfp','waiting for payment'),('ip','in_process'),('rd','ready'),('rcv','received'))

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)# ForeignKey
    request_status = models.CharField(max_length=55, choices=REQUEST_STATUS, default=('wfp','waiting for payment'))
    count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    tracking_code = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    def __str__(self):
        return str(self.student)  + ' / ' +str(self.request_status) + ' /  '+str(self.count)+ ' /  ' +str(self.created_at)


class Bill(models.Model):
    bill_code= models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    request = models.ForeignKey(CertificateRequest,on_delete=models.CASCADE)
    bill_price =models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    paid = models.BooleanField(default=False)
    def __str__(self):
        return self.request



class Notification(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE, blank=True, null=True)# ForeignKey
    request = models.ForeignKey(CertificateRequest,on_delete=models.CASCADE,blank=True,null=True)# ForeignKey
    title = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.CharField(max_length=2000)
    def __str__(self):
        return self.title


class CertificateItem(models.Model):
    STATUS= (('wfp','waiting for payment'),('ip','in_process'),('rd','ready'),('rcv','received'))

    request = models.ForeignKey(CertificateRequest,on_delete=models.CASCADE)# ForeignKey
    status = models.CharField(max_length=55, choices=STATUS, default=('wfp','waiting for payment'))
    level = models.ForeignKey(Level,on_delete=models.DO_NOTHING)# ForeignKey
    certificate_type = models.ForeignKey('CertificateType',on_delete=models.DO_NOTHING)# ForeignKey
    language = models.ForeignKey('Language',on_delete=models.DO_NOTHING)# ForeignKey
    card_board = models.BooleanField(default=False)
    colored = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    def __str__(self):
        return self.level + ' | | ' + self.certificate_type +' || '+ self.request


class LevelTypeLink(models.Model):
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING)# ForeignKey
    certificate_type = models.ForeignKey(CertificateType, on_delete=models.DO_NOTHING)# ForeignKey
    price = models.DecimalField(max_digits=9, decimal_places=2)
    def __str__(self):
        return str(self.level) + ' | | ' + str(self.certificate_type)


class TypeLanguage(models.Model):
    certificate_type = models.ForeignKey(CertificateType,on_delete=models.CASCADE)# ForeignKey
    language = models.ForeignKey(Language,on_delete=models.CASCADE)# ForeignKey
    def __str__(self):
        return str(self.certificate_type) + ' | | ' + str(self.language)

