from django.contrib import admin
from .models import Associado

# Classe que define como o modelo será exibido no admin
@admin.register(Associado)
class AssociadoAdmin(admin.ModelAdmin):
    # Campos exibidos na listagem do admin
    list_display = ('nome', 'cpf', 'email', 'telefone', 'ativo')

    # Permite buscar por esses campos no admin
    search_fields = ('nome', 'cpf', 'email')