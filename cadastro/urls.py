from django.urls import include, path

from cadastro.views import listacidades,detalhecidades,cadastracidades

urlpatterns = [
    path('', listacidades, name='cidades-list'),
    path('detalhe/<int:id>/', detalhecidades, name='cidades-detalhe'),
    path('create/', cadastracidades, name='cidades-cadastro')
]
