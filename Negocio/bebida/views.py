from django.shortcuts import render
from django.http import HttpResponse
from .models import Bebida

def bebida(request):
    bebida = Bebida.objects.all()
    return render(request, 'bebida.html',{'bebida': bebida})



def bebida(request):
    bebida = Bebida.objects.all()
    return render(request, 'bebida.html',{'bebida': bebida})