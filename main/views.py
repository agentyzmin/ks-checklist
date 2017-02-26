from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Apartment, Question, Answer
from .forms import ApartmentForm, AnswerForm
from django.core.urlresolvers import reverse
from django.contrib import auth

def index(request):
    context = {}
    context['apartments'] = get_list_or_404(Apartment)
    context['apartment_form'] = ApartmentForm
    if request.method == 'POST':
        apartment_id = request.POST.get('apartment_id')
        return redirect(reverse('index', args=(apartment_id,)))
    return render(request, 'main/main.html', context)


def questions_list(request, apartment_pk):
    context = {}
    context['apartment'] = get_object_or_404(Apartment, pk=apartment_pk)
    context['questions'] = get_list_or_404(Question)
    context['answer_form'] = AnswerForm
    context['username'] = auth.get_user(request).username
    return render(request, 'main/questions.html', context)
