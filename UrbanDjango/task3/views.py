from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class MainWiew(TemplateView):
    template_name = 'main.html'


class SelGame(TemplateView):
    template_name = 'select_game.html'
    extra_context = {'list_game': ['Шахматы', 'Шашки', 'Бильярд']}


class Champion(TemplateView):
    template_name = 'champion.html'
    extra_context = {'Шахматы': 'Денис', 'Шашки': 'Игорь', 'Бильярд': 'Эдуард'}