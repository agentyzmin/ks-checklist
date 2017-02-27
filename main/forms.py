from django.forms import ModelForm, ChoiceField, RadioSelect, Form, Select
from .models import Apartment, Answer

APARTMENTS = ()
for apartment in Apartment.objects.all():
    APARTMENTS += ((apartment.id, apartment.title),)

class ApartmentForm(Form):
    apartment = ChoiceField(label='', widget=Select, choices=APARTMENTS)

ANSWERS = (
    (0, 'Точно ні'),
    (1, 'Скоріше ні'),
    (2, 'Не можу відповісти'),
    (3, 'Скоріше так'),
    (4, 'Точно так'),
)


class AnswerForm(Form):
    answer = ChoiceField(label='', widget=RadioSelect, choices=ANSWERS)
