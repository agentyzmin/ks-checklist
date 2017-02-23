from django.forms import ModelForm, ChoiceField, RadioSelect, Form
from .models import Apartment, Answer


class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ['title']

ANSWERS = (
    (0, 'Точно ні'),
    (1, 'Скоріше ні'),
    (2, 'Не можу відповісти'),
    (3, 'Скоріше так'),
    (4, 'Точно так'),
)


class AnswerForm(Form):
    answer = ChoiceField(label='', widget=RadioSelect, choices=ANSWERS)
