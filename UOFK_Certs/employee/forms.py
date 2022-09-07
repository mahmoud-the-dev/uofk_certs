from django.forms import ModelForm
from certificates.models import Level

class CertificateForm (ModelForm):
    class Meta:
        model = Level
        fields = '__all__'


