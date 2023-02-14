from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from cadastro.forms import CidadeForm
from cadastro.models import Cidade


# Create your views here.

class SidiaBaseListView(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Projeto Sidia'
        return context


class CidadeList(SidiaBaseListView):

    queryset = Cidade.objects.all().order_by('nome')
    context_object_name = 'cidades'
    template_name = 'cadastro/lista_cidades.html'


class CidadeDetail(DetailView):

    context_object_name = 'cidade'
    queryset = Cidade.objects.all()
    template_name = 'cadastro/detalhe_cidades.html'


class CidadeDelete(DeleteView):

    context_object_name = 'cidade'
    queryset = Cidade.objects.all()
    template_name = 'cadastro/remove_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeCreate(CreateView):

    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastro/cadastra_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeUpdate(UpdateView, SuccessMessageMixin):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastro/edita_cidades.html'
    success_url = reverse_lazy('cidades-list')
    success_message = 'Cadas atualizado com sucesso!'

# Functions based views -> fbv

# def listacidades(request):
#
#     qs = Cidade.objects.all().order_by('nome')
#     context = {
#         'cidades': qs,
#         'titulo': 'SIDIA'
#     }
#     return render(request, 'cadastro/lista_cidades.html', context)
#
#
# def detalhecidades(request, id):
#
#     # id_cidade = request.GET['id_cidade']
#
#     cidade = get_object_or_404(Cidade, pk=id)
#
#     context = {
#         'cidade': cidade
#     }
#
#     return render(request, 'cadastro/detalhe_cidades.html', context)
#
#
# def removecidades(request, id):
#
#     cidade = get_object_or_404(Cidade, pk=id)
#
#     cidade.delete()
#
#     return redirect("cidades-list")
#
#
# def cadastracidades(request):
#
#     if request.method == 'POST':
#         form = CidadeForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#             return redirect("cidades-list")
#     else:
#         form = CidadeForm()
#
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'cadastro/cadastra_cidades.html', context)
#
#
# def editarcidades(request, id):
#
#     if request.method == "GET":
#         cidade_obj = get_object_or_404(Cidade, pk=id)
#         form = CidadeForm(instance=cidade_obj)
#
#     else:
#         pass
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'cadastro/edita_cidades.html',context)

