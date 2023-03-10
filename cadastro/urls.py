from django.contrib.auth.decorators import login_required
from django.urls import include, path

from cadastro.views import CidadeList, CidadeDetail, CidadeDelete, CidadeUpdate, CidadeCreate

urlpatterns = [
    path('', CidadeList.as_view(), name='cidades-list'),
    path('detail/<int:pk>/', CidadeDetail.as_view(), name='cidades-detalhe'),
    path('delete/<int:pk>/', login_required(CidadeDelete.as_view()), name='cidades-remove'),
    path('update/<int:pk>/', login_required(CidadeUpdate.as_view()), name='cidades-editar'),
    path('create/', login_required(CidadeCreate.as_view()), name='cidades-cadastro')
]
