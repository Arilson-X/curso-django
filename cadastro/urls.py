from django.urls import include, path

from cadastro.views import listacidades, detalhecidades, cadastracidades, removecidades

urlpatterns = [
    path('', listacidades, name='cidades-list'),
    path('detail/<int:id>/', detalhecidades, name='cidades-detalhe'),
    path('delete/<int:id>/', removecidades, name='cidades-remove'),
    path('create/', cadastracidades, name='cidades-cadastro')
]
