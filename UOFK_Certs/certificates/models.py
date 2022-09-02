from django.db import models

# Create your models here.

class Student(models.Model):
    university_number = models.IntegerField()
    name = models.CharField()
    email = models.EmailField()
    batch = models.CharField()
    level = models.CharField()
    stage = models.IntegerField()


class CompletedLevel(models.Model):
    completed_level_id = models.IntegerField()
    university_number = models.IntegerField()# ForeignKey
    
    level = models.CharField()


class Notifications(models.Model):
    notification_id = models.IntegerField()
    bill_id = models.IntegerField()# ForeignKey
    certificate_request_id = models.CharField()# ForeignKey
    title = models.CharField()
    email = models.EmailField()
    content = models.CharField()

class CertificateRequest(models.Model):
    certificate_request_id = models.CharField()
    university_number = models.CharField()# ForeignKey
    certificate_id = models.IntegerField()# ForeignKey
    request_status = models.CharField()
    count = models.IntegerField()
    tracking_code = models.CharField()



class CertificateItem(models.Model):
    certificate_item_id = models.IntegerField()
    certificate_level_id = models.IntegerField()# ForeignKey
    certificate_type_id = models.IntegerField()# ForeignKey
    language_id = models.IntegerField()# ForeignKey
    card_board = models.BooleanField()
    colored = models.BooleanField()
    price = models.DecimalField()
    

class CertificateLevel(models.Model):
    certificate_level_id = models.IntegerField()
    level = models.CharField()

class LevelTypeLink(models.Model):
    level_type_link_id = models.IntegerField()
    certificate_level_id = models.IntegerField()# ForeignKey
    certificate_type_id = models.IntegerField()# ForeignKey
    price = models.DecimalField()


class CertificateType(models.Model):
    certificate_level_id = models.IntegerField()
    type = models.CharField()
    card_board = models.BooleanField()



class TypeLanguage(models.Model):
    type_language_id = models.IntegerField()
    certificate_type_id = models.IntegerField()# ForeignKey
    language_id = models.IntegerField()# ForeignKey


class Langugae(models.Model):
    language_id = models.IntegerField()
    certificate_type_id = models.IntegerField()# ForeignKey
    language = models.CharField()

class Bill(models.Model):
    bill_id = models.IntegerField()
    certificate_request_id = models.CharField()# ForeignKey
    bill_price = models.FloatField()
    expiry_date = models.DateField()
    paid = models.BooleanField()
