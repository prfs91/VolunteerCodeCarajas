from django import forms
from .models import Associado

# Formulário baseado no modelo Associado
class AssociadoForm(forms.ModelForm):
    class Meta:
        model = Associado
        fields = ['nome', 'cpf', 'email', 'telefone', 'ativo']  # Campos do formulário