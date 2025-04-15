from django.db import models

# Modelo que representa um associado no sistema
class Associado(models.Model):
    # DADOS PESSOAIS
    nome = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100, blank=True)  # Para respeitar identidade de gênero
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True) # CPF do associado – precisa ser único
    rg = models.CharField(max_length=20, blank=True)
    orgao_emissor = models.CharField(max_length=20, blank=True)
    sexo = models.CharField(max_length=20, blank=True)
    estado_civil = models.CharField(max_length=20, blank=True)
    nacionalidade = models.CharField(max_length=50, blank=True)
    naturalidade = models.CharField(max_length=50, blank=True)
    
    # CONTATO E ENDEREÇO
    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15, blank=True) # Telefone é opcional (blank=True)
    email = models.EmailField()

    # INFORMAÇÕES SOBRE A DEFICIÊNCIA
    tipo_deficiencia = models.CharField(max_length=100)
    cid = models.CharField(max_length=20, blank=True)  # Classificação Internacional de Doenças
    laudo_medico = models.FileField(upload_to='laudos/', blank=True)
    necessidades_acessibilidade = models.TextField(blank=True)
    data_diagnostico = models.DateField(blank=True, null=True)

    # DOCUMENTAÇÃO LEGAL
    numero_associado = models.CharField(max_length=20, unique=True)
    data_entrada = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='ativo')  # Ativo, Inativo etc.
    comprovante_residencia = models.FileField(upload_to='comprovantes/', blank=True)
    autorizacao_uso_imagem = models.BooleanField(default=False)
    termo_adesao = models.FileField(upload_to='termos/', blank=True)
    
    # RESPONSÁVEL LEGAL (CASO O ASSOCIADO NÃO SEJA MAIOR DE IDADE OU TENHA INTERDIÇÃO)
    responsavel_nome = models.CharField(max_length=100, blank=True)
    responsavel_parentesco = models.CharField(max_length=50, blank=True)
    responsavel_rg = models.CharField(max_length=20, blank=True)
    responsavel_cpf = models.CharField(max_length=14, blank=True)
    responsavel_documento = models.FileField(upload_to='responsaveis/', blank=True)
    
    # INFORMAÇÕES SOCIOECONÔMICAS
    escolaridade = models.CharField(max_length=100, blank=True)
    ocupacao = models.CharField(max_length=100, blank=True)
    renda_familiar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    recebe_beneficio = models.CharField(max_length=100, blank=True)
    participa_outros_programas = models.TextField(blank=True)
    
    # Se o associado está ativo ou não
    ativo = models.BooleanField(default=True)
    # Data de entrada é definida automaticamente na criação
    data_entrada = models.DateField(auto_now_add=True)

    # Representação do associado (exibido no admin e em listas)
    def __str__(self):
        return self.nome
