from django.urls import path
from . import views

urlpatterns = [
    path('employee',views.home,name='employee home'),
    path('employee/login',views.adlogin,name='employee login'),
    path('employee/verify',views.verify,name='employee verification'),
    path('employee/menu',views.menu,name='employee menu'),
    path('employee/certificate-settings',views.certificate_settings,name='certificate settings'),
    path('employee/certificate-requests',views.ManageCertificateRequests,name='certificate requests'),
    path('employee/view-request/<str:pk>',views.ViewRequest,name='view request'),
    path('employee/add-certificate',views.add_certificate,name='add certificate'),
    path('employee/update-certificate',views.update_certificate,name='update certificate'),
]
