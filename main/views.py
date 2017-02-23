from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.forms.formsets import formset_factory
from .models import Apartment, Question, Answer
from .forms import ApartmentForm, AnswerForm
from django.core.urlresolvers import reverse


def index(request):
    apartments = get_list_or_404(Apartment)
    apartment_form = ApartmentForm
    if request.method == 'POST':
        apartment_id = request.POST.get('apartment_id')
        return redirect(reverse('index', args=(apartment_id,)))
    return render(request, 'main/main.html', {'apartments': apartments, 'apartment_form': apartment_form})


def questions_list(request, apartment_pk):
    apartment = get_object_or_404(Apartment, pk=apartment_pk)
    questions = get_list_or_404(Question)
    answer_form = AnswerForm
    answer_formset = formset_factory(AnswerForm)
    return render(request, 'main/questions.html',
                  {'questions': questions, 'apartment': apartment, 'answer_form': answer_form})


