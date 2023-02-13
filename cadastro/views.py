from django.shortcuts import render, get_object_or_404, redirect

from cadastro.forms import CidadeForm
from cadastro.models import Cidade


# Create your views here.

# Functions based views -> fbv

def listacidades(request):

    qs = Cidade.objects.all().order_by('nome')
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


def removecidades(request, id):

    cidade = get_object_or_404(Cidade, pk=id)

    cidade.delete()

    return redirect("cidades-list")


def cadastracidades(request):

    if request.method == 'POST':
        form = CidadeForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("cidades-list")
    else:
        form = CidadeForm()


    context = {
        'form': form
    }

    return render(request, 'cadastro/cadastra_cidades.html', context)

