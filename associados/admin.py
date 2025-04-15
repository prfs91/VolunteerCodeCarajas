from django.contrib import admin
from .models import Associado

# Registrando o modelo Associado no admin com uma configuração personalizada
@admin.register(Associado)
class AssociadoAdmin(admin.ModelAdmin):
    # Define quais campos serão exibidos na listagem da área administrativa
    list_display = (
        'nome',               # Nome do associado
        'cpf',                # CPF
        'email',              # E-mail
        'telefone',           # Telefone
        'ativo',              # Se está ativo ou não
        'numero_associado',   # Código único do associado
        'data_entrada',       # Data em que foi cadastrado
        'tipo_deficiencia',   # Tipo de deficiência (se houver)
        'renda_familiar'      # Renda familiar declarada
    )

    # Campos pelos quais o administrador poderá buscar
    search_fields = (
        'nome',               # Permite buscar por nome
        'cpf',                # Permite buscar por CPF
        'email',              # Permite buscar por e-mail
        'numero_associado'    # Permite buscar pelo número/código do associado
    )

    # Filtros na lateral direita da interface do admin para facilitar a navegação
    list_filter = (
        'ativo',              # Filtra associados ativos/inativos
        'data_entrada',       # Filtra por data de entrada
        'tipo_deficiencia',   # Filtra por tipo de deficiência
        'sexo',               # Filtra por sexo
        'estado_civil'        # Filtra por estado civil
    )

    # Campos que não podem ser editados diretamente no admin
    readonly_fields = (
        'data_entrada',       # Mostra a data, mas não deixa editar
        'numero_associado'    # Número gerado automaticamente, também não pode ser editado
    )