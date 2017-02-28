from django.shortcuts import redirect, render
from django.contrib import auth

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
