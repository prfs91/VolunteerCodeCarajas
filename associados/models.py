from django.db import models
from django.utils import timezone


# Modelo que representa um associado no sistema
class Associado(models.Model):
    # DADOS PESSOAIS
    nome = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100, blank=True)  # Para respeitar identidade de gênero
    data_nascimento = models.DateField(default='1900-01-01')
    cpf = models.CharField(max_length=14, unique=True) # CPF do associado – precisa ser único
    rg = models.CharField(max_length=20, blank=True)
    orgao_emissor = models.CharField(max_length=20, blank=True)
    sexo = models.CharField(max_length=20, blank=True)
    estado_civil = models.CharField(max_length=20, blank=True)
    nacionalidade = models.CharField(max_length=50, blank=True)
    naturalidade = models.CharField(max_length=50, blank=True)

    # CONTATO E ENDEREÇO
    endereco = models.CharField(max_length=200, default='Endereço não informado')
    cep = models.CharField(max_length=10, default='00000-000')
    telefone = models.CharField(max_length=15, blank=True) # Telefone é opcional (blank=True)
    email = models.EmailField()

    # INFORMAÇÕES SOBRE A DEFICIÊNCIA
    tipo_deficiencia = models.CharField(max_length=100, default="Não informado", blank=True)
    cid = models.CharField(max_length=20, blank=True)  # Classificação Internacional de Doenças
    laudo_medico = models.FileField(upload_to='laudos/', blank=True)
    necessidades_acessibilidade = models.TextField(blank=True)
    data_diagnostico = models.DateField(blank=True, null=True)

    # DOCUMENTAÇÃO LEGAL
    numero_associado = models.CharField(max_length=20, unique=True, blank=True, null=True)
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

    def save(self, *args, **kwargs):
        if not self.numero_associado:  # Se o número do associado não foi preenchido
            ano_atual = str(timezone.now().year)  # Ano da data de entrada (você pode ajustar conforme necessário)
            ultimo_numero = Associado.objects.filter(
                data_entrada__year=timezone.now().year).order_by('numero_associado').last()

            if ultimo_numero and ultimo_numero.numero_associado:
                # Se houver um registro, pega o último número do associado e incrementa
                ultimo_codigo = int(ultimo_numero.numero_associado.split('-')[1]) + 1
            else:
                # Caso não haja registros, inicia o código a partir de 1
                ultimo_codigo = 1

            numero_associado = f"ASSOC-{ano_atual}-{ultimo_codigo:04d}"
            self.numero_associado = numero_associado

        super(Associado, self).save(*args, **kwargs)  # Chama o método save original

    # Representação do associado (exibido no admin e em listas)
    def __str__(self):
        return self.nome
