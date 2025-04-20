import requests
from django.db import models
from django.utils import timezone
from validate_docbr import CPF

STATUS_CHOICES = [
    ('ativo', 'Ativo'),
    ('inativo', 'Inativo'),
    ('suspenso', 'Suspenso'),
]


# Upload dinâmico por associado
def upload_path(instance, filename):
    numero = instance.numero_associado or 'novo'
    return f'associados/{numero}/{filename}'


# Validador de CPF com segurança reforçada
def validar_cpf(value):
    if not value:
        return  # Ignora se estiver em branco

    cpf = CPF()
    cpf_num = value.replace('.', '').replace('-', '')

    if cpf_num == cpf_num[0] * len(cpf_num):
        raise ValidationError("CPF inválido: todos os dígitos são iguais.")

    if not cpf.validate(value):
        raise ValidationError("CPF inválido.")


# Modelo que representa um associado no sistema
class Associado(models.Model):
    numero_associado = models.CharField(max_length=20, unique=True, blank=True, db_index=True)

    # DADOS PESSOAIS
    nome = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100, blank=True)  # Para respeitar identidade de gênero
    data_nascimento = models.DateField(default='1900-01-01')
    cpf = models.CharField(max_length=14, unique=True, db_index=True,
                           validators=[validar_cpf]) # CPF do associado – precisa ser único
    rg = models.CharField(max_length=20, blank=True)
    orgao_emissor = models.CharField(max_length=20, blank=True)
    sexo = models.CharField(max_length=20, blank=True)
    estado_civil = models.CharField(max_length=20, blank=True)
    nacionalidade = models.CharField(max_length=50, blank=True)
    naturalidade = models.CharField(max_length=50, blank=True)

    # CONTATO E ENDEREÇO (Agora com campos separados)
    cep = models.CharField(max_length=10, default='00000-000')  # O CEP continua armazenado
    logradouro = models.CharField(max_length=100, blank=True)  # Rua, avenida, etc.
    complemento = models.CharField(max_length=100, blank=True)  # Complemento do endereço (se houver)
    bairro = models.CharField(max_length=100, blank=True)  # Bairro
    cidade = models.CharField(max_length=100, blank=True)  # Cidade
    uf = models.CharField(max_length=2, blank=True)  # Estado (UF)
    telefone = models.CharField(max_length=15, blank=True)  # Telefone
    email = models.EmailField()  # Email

    # INFORMAÇÕES SOBRE A DEFICIÊNCIA
    tipo_deficiencia = models.CharField(max_length=100, default="Não informado", blank=True)
    cid = models.CharField(max_length=20, blank=True)  # Classificação Internacional de Doenças
    laudo_medico = models.FileField(upload_to=upload_path, blank=True)
    necessidades_acessibilidade = models.TextField(blank=True)
    data_diagnostico = models.DateField(blank=True, null=True)

    # DOCUMENTAÇÃO LEGAL
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')  # Ativo, Inativo etc.
    comprovante_residencia = models.FileField(upload_to=upload_path, blank=True)
    autorizacao_uso_imagem = models.BooleanField(default=False)
    termo_adesao = models.FileField(upload_to=upload_path, blank=True)

    # RESPONSÁVEL LEGAL (CASO O ASSOCIADO NÃO SEJA MAIOR DE IDADE OU TENHA INTERDIÇÃO)
    responsavel_nome = models.CharField(max_length=100, blank=True)
    responsavel_parentesco = models.CharField(max_length=50, blank=True)
    responsavel_rg = models.CharField(max_length=20, blank=True)
    responsavel_cpf = models.CharField(max_length=14, blank=True, validators=[validar_cpf])
    responsavel_documento = models.FileField(upload_to=upload_path, blank=True)

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

    # Função para preencher o endereço automaticamente com base no CEP
    def preencher_endereco_via_cep(self):
        """Preenche automaticamente os campos de endereço usando a API ViaCEP"""
        if not self.cep:
            return  # Se o CEP estiver vazio, não faz nada

        # Limpeza do formato do CEP (remove pontos e traços)
        cep_limpo = self.cep.replace("-", "").strip()

        # Requisição para a API ViaCEP
        response = requests.get(f"https://viacep.com.br/ws/{cep_limpo}/json/")

        if response.status_code == 200:
            dados = response.json()

            # Verifica se o CEP não retornou erro
            if not dados.get("erro"):
                # Preenche os campos do endereço
                self.logradouro = dados.get("logradouro", "")
                self.bairro = dados.get("bairro", "")
                self.cidade = dados.get("localidade", "")
                self.uf = dados.get("uf", "")
                self.complemento = dados.get("complemento", "")

    # Sobrescrevendo o método save para preencher automaticamente o número do associado
    def save(self, *args, **kwargs):
        """Sobrescreve o método save para gerar automaticamente o número do associado"""
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

        # Chama a função para preencher o endereço automaticamente com o ViaCEP
        self.preencher_endereco_via_cep()

        super(Associado, self).save(*args, **kwargs)  # Chama o método save original

    # Representação do associado (exibido no admin e em listas)
    def __str__(self):
        return f"{self.nome} ({self.numero_associado or 'sem número'})"
