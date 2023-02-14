from django import forms
from django.core.exceptions import ValidationError

from cadastro.models import Cidade


class TestForm(forms.Form):

    nome = forms.CharField(max_length=45,required=True)


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'

    def clean(self):

        nome = self.cleaned_data['nome']

        if nome == 'Itajuba':
            raise ValidationError({'nome':'Não podemos cadastrar a cidade de Itajubá no sistema'})
