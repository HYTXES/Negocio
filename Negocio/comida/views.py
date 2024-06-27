from django.shortcuts import render
from django.http import HttpResponse
from .models import Comida

def home(request):
    comida = Comida.objects.all()
    return render(request, 'home.html',{'comida': comida})
from django.shortcuts import render

def bebida(request):
    return render(request, 'bebida.html')

def drinks_mexicanos(request):
    return render(request, 'drinks_mexicanos.html')

def postres_mexicanos(request):
    return render(request, 'postres_mexicanos.html')

