from django import forms
from .models import Associado

# Formulário baseado no modelo Associado
class AssociadoForm(forms.ModelForm):
    class Meta:
        model = Associado
        fields = [
            # DADOS PESSOAIS
            'nome', 
            'nome_social', 
            'data_nascimento', 
            'cpf', 
            'rg', 
            'orgao_emissor', 
            'sexo', 
            'estado_civil', 
            'nacionalidade', 
            'naturalidade',
            
            # CONTATO E ENDEREÇO
            'endereco', 
            'cep', 
            'telefone', 
            'email',
            
            # INFORMAÇÕES SOBRE A DEFICIÊNCIA
            'tipo_deficiencia', 
            'cid', 
            'laudo_medico', 
            'necessidades_acessibilidade', 
            'data_diagnostico',
            
            # DOCUMENTAÇÃO LEGAL
            'numero_associado', 
            'status', 
            'comprovante_residencia', 
            'autorizacao_uso_imagem', 
            'termo_adesao',
            
            # RESPONSÁVEL LEGAL
            'responsavel_nome', 
            'responsavel_parentesco', 
            'responsavel_rg', 
            'responsavel_cpf', 
            'responsavel_documento',
            
            # INFORMAÇÕES SOCIOECONÔMICAS
            'escolaridade', 
            'ocupacao', 
            'renda_familiar', 
            'recebe_beneficio', 
            'participa_outros_programas',
            
            # STATUS
            'ativo',
        ]  # Campos do formulário