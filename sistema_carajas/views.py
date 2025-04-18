# sistema_carajas/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
