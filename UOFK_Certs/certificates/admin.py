from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Student)
admin.site.register(models.CompletedLevel)
admin.site.register(models.Notification)
admin.site.register(models.CertificateRequest)
admin.site.register(models.CertificateItem)
admin.site.register(models.Level)
admin.site.register(models.LevelTypeLink)
admin.site.register(models.CertificateType)
admin.site.register(models.Language)
admin.site.register(models.Bill)
admin.site.register(models.TypeLanguage)