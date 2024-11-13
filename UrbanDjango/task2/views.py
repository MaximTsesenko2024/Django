from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Class_wiew(TemplateView):
    template_name = 'class_template.html'


def func_wiew(request):
    return render(request, 'func_template.html')

