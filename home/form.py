from django.forms import ModelForm
from .models import Company

class AddCompany(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
