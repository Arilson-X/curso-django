from django.urls import include, path

from cadastro.views import listacidades,detalhecidades

urlpatterns = [
    path('', listacidades, name='cidades-list'),
    path('detalhe/', detalhecidades, name='cidades-detalhe')
]
