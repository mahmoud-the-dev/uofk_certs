from django.urls import path
from .views import *

urlpatterns = [
    path('employee',home,name='employee home'),
    path('employee/login',adlogin,name='employee login'),
    path('employee/verify',verify,name='employee verification'),
    path('employee/menu',menu,name='employee menu'),
    path('employee/certifcate-settings',certificate_settings,name='certificate settings'),
    path('employee/certificate-requests',ManageCertificateRequests.as_view,name='certificate requests'),
    path('employee/view-request',ViewRequest.as_view(),name='view request'),
    path('employee/add-certificate',add_certificate,name='add certificate'),
    path('employee/update-certificate',update_certificate,name='update certificate'),


]
