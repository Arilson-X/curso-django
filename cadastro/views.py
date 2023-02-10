from django.shortcuts import render

from cadastro.models import Cidade


# Create your views here.

# Functions based views -> fbv

def listacidades(request):

    qs = Cidade.objects.all()
    qs_capitais = Cidade.objects.filter(capital=True)



