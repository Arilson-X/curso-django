from django.shortcuts import render

from cadastro.models import Cidade


# Create your views here.

# Functions based views -> fbv

def listacidades(request):

    qs = Cidade.objects.all()
    context = {
        'cidades': qs,
        'titulo': 'SIDIA'
    }
    return render(request, 'cadastro/lista_cidades.html', context)

def detalhecidades(request):

    id_cidade = request

    cidade = get_object_or_404(Cidade, pk=id_cidade)

    context = {
        'cidade': cidade
    }

    return render(request, 'cadastro/detelhe_cidades.html', context)


