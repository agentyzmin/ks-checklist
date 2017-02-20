from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Apartment, Question, Answer
from .forms import ApartmentForm
from django.core.urlresolvers import reverse


def index(request):
    apartments = get_list_or_404(Apartment)
    apartment_form = ApartmentForm
    if request.method == 'POST':
        apartment_id = request.POST.get('apartment_id')
        return redirect(reverse('index', args=(apartment_id,)))
    return render(request, 'main/main.html', {'apartments': apartments, 'apartment_form': apartment_form})


def questions_list(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    questions = get_list_or_404(Question)
    return render(request, 'main/questions.html', {'questions': questions, 'apartment': apartment})