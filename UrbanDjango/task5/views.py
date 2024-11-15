from django.shortcuts import render
from django.http import HttpResponse
from .forms import Registation

# Create your views here.
users = ['Max', 'Denis', 'Jon']


def sign_up_by_html(request):
    info = {'title': 'Регистрация пользователя'}
    if request.method == 'POST':
        if 'error' in info.keys():
            info.pop('error')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if username in users:
            info['error'] = f'Пользователь {username} уже существует!'
        elif password != repeat_password:
            info['error'] = f'Пароли не совпадают!'
        elif age < 18:
            info['error'] = f'Вы должны быть старше 18'
        else:
            users.append(username)
            return HttpResponse(f'Приветствуем, {username}!')
        return render(request, 'registration_page.html', context=info)

    return render(request, 'registration_page.html', context=info)

def sign_up_by_django(request):
    info = {'title': 'Регистрация пользователя'}
    if request.method == 'POST':
        form = Registation(request.POST)
        if form.is_valid():
            if 'error' in info.keys():
                info.pop('error')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if username in users:
                info['error'] = f'Пользователь {username} уже существует!'
            elif password != repeat_password:
                info['error'] = f'Пароли не совпадают!'
            elif age < 18:
                info['error'] = f'Вы должны быть старше 18'
            else:
                users.append(username)
                return HttpResponse(f'Приветствуем, {username}!')
            form = Registation()
            info['form'] = form
            return render(request, 'registration_page.html', context=info)
    else:
        form = Registation()
        info['form'] = form
    return render(request, 'registration_page.html', context=info)
