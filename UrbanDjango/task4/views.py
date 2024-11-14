from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class MainWiew(TemplateView):
    template_name = 'main.html'
    extra_context = {'title': 'Главная страница'}


class SelGame(TemplateView):
    list_ = ['Шахматы', 'Шашки', 'Бильярд']
    template_name = 'select_game.html'
    extra_context = {'title': 'Выбор игры', 'list_game': list_}


class Champion(TemplateView):
    template_name = 'champion.html'
    extra_context = {'title': 'Чемпионы', 'Шахматы': 'Денис', 'Шашки': 'Игорь', 'Бильярд': 'Эдуард'}