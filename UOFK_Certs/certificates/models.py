from django.db import models
import uuid
# Create your models here.

class Student(models.Model):
    university_number = models.CharField(max_length=25, unique=True,primary_key=True,editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    batch = models.IntegerField()
    level = models.CharField(max_length=255)
    stage = models.IntegerField()
    def __str__(self):
        return self.name


class Language(models.Model):
    language = models.CharField(max_length=255)
    def __str__(self):
        return self.language


class Level(models.Model):
    level = models.CharField(max_length=255)
    def __str__(self):
        return self.level


class CertificateType(models.Model):
    type = models.CharField(max_length=255)
    card_board = models.BooleanField()
    def __str__(self):
        return self.type


class CompletedLevel(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)# ForeignKey
    level = models.ForeignKey(Level,on_delete=models.CASCADE)#ForeignKey
    def __str__(self):
        return self.level


class CertificateRequest(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)# ForeignKey
    request_status = models.CharField(max_length=55)
    count = models.IntegerField(default=1)
    tracking_code = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    def __str__(self):
        return self.student


class Bill(models.Model):
    bill_code= models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    request = models.ForeignKey(CertificateRequest,on_delete=models.CASCADE)
    bill_price = models.FloatField()
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
    request = models.ForeignKey(CertificateRequest,on_delete=models.CASCADE)# ForeignKey
    level = models.ForeignKey(Level,on_delete=models.CASCADE)# ForeignKey
    certificate_type = models.ForeignKey('CertificateType',on_delete=models.CASCADE)# ForeignKey
    language = models.ForeignKey('Language',on_delete=models.CASCADE)# ForeignKey
    card_board = models.BooleanField(default=False)
    colored = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)


class LevelTypeLink(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)# ForeignKey
    certificate_type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)# ForeignKey
    price = models.DecimalField(max_digits=9, decimal_places=2)
    def __str__(self):
        return self.level + ' | | ' + self.certificate_type


class TypeLanguage(models.Model):
    certificate_type = models.ForeignKey(CertificateType,on_delete=models.CASCADE)# ForeignKey
    language = models.ForeignKey(Language,on_delete=models.CASCADE)# ForeignKey

