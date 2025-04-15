from django.db import models

# Modelo que representa um associado no sistema
class Associado(models.Model):
    # Nome completo do associado
    nome = models.CharField(max_length=100)

    # CPF do associado – precisa ser único
    cpf = models.CharField(max_length=14, unique=True)

    # E-mail para contato
    email = models.EmailField()

    # Telefone é opcional (blank=True)
    telefone = models.CharField(max_length=15, blank=True)

    # Data de entrada é definida automaticamente na criação
    data_entrada = models.DateField(auto_now_add=True)

    # Se o associado está ativo ou não
    ativo = models.BooleanField(default=True)

    # Representação do associado (exibido no admin e em listas)
    def __str__(self):
        return self.nome
