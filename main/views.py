from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Apartment, Question, Answer
from .forms import ApartmentForm, AnswerForm
from django.core.urlresolvers import reverse
from django.contrib import auth

def index(request):
    context = {}
    context['apartments'] = get_list_or_404(Apartment)
    if request.method == 'POST':
        form = ApartmentForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data.get('apartment', '')
            return redirect('apartments/{}'.format(id))
    else:
        context['apartment_form'] = ApartmentForm
        return render(request, 'main/main.html', context)


def questions_list(request, apartment_pk):
    context = {}
    context['apartment'] = get_object_or_404(Apartment, pk=apartment_pk)
    context['questions'] = get_list_or_404(Question)
    context['answer_form'] = AnswerForm
    context['username'] = auth.get_user(request).username
    return render(request, 'main/questions.html', context)
