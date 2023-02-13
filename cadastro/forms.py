from django import forms

from cadastro.models import Cidade


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome', 'capital']
