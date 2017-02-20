from django.forms import ModelForm
from .models import Apartment


class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ['title']