from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'myauth/login.html', {'login_error': 'Користувача не знайдено'})
    else:
        return render(request, 'myauth/login.html', {})


def logout(request):
    auth.logout(request)
    return redirect('/')


def registration(request):
    context = {}
    context['registration_form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect('/')
        else:
            context['registration_form'] = new_user_form
    return render(request, 'myauth/registration.html', context)

