from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
def checklist(request):
    questions = Question.objects.all()
    return render(request, 'list/list.html', {'questions': questions})