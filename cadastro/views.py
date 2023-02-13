from django.shortcuts import render, get_object_or_404

from cadastro.forms import CidadeForm
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


def detalhecidades(request, id):

    # id_cidade = request.GET['id_cidade']

    cidade = get_object_or_404(Cidade, pk=id)

    context = {
        'cidade': cidade
    }

    return render(request, 'cadastro/detalhe_cidades.html', context)


def cadastracidades(request):

    form = CidadeForm()

    context = {
        'form': form
    }

    return render(request, 'cadastro/cadastra_cidades.html', context)

