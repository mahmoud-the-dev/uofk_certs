from django.urls import path
from . import views

urlpatterns = [
    path('employee',views.home,name='employee home'),
    path('employee/login',views.login,name='employee login'),
    path('employee/verify',views.verify,name='employee verification'),
    path('employee/menu',views.menu,name='employee menu'),
    path('employee/certifcate-settings',views.certificate_settings,name='certificate settings'),
    path('employee/certificate-requests',views.manage_certificate_requests,name='certificate requests'),
    path('employee/add-certificate',views.add_certificate,name='add certificate'),
    path('employee/update-certificate',views.update_certificate,name='update certificate'),


]
