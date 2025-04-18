from django.test import TestCase
from django.urls import reverse

from .models import Associado


class AssociadoTests(TestCase):

    def setUp(self):
        # Dados válidos para os testes
        self.valid_data_1 = {
            'nome': 'Maria Silva',
            'nome_social': 'Maria',
            'data_nascimento': '1990-05-10',
            'cpf': '123.456.789-00',
            'rg': '1234567',
            'orgao_emissor': 'SSP',
            'sexo': 'Feminino',
            'estado_civil': 'Solteira',
            'nacionalidade': 'Brasileira',
            'naturalidade': 'Belém',
            'endereco': 'Rua das Flores, 123',
            'cep': '66000-000',
            'telefone': '(91)99999-0000',
            'email': 'maria@example.com',
            'tipo_deficiencia': 'Visual',
            'cid': 'H54',
            'necessidades_acessibilidade': 'Braille',
            'data_diagnostico': '2005-08-15',
            'numero_associado': 'A001',
            'status': 'ativo',
            'autorizacao_uso_imagem': True,
            'escolaridade': 'Ensino Médio',
            'ocupacao': 'Estudante',
            'renda_familiar': '1200.00',
            'recebe_beneficio': 'Sim',
            'participa_outros_programas': 'Programa X',
            'ativo': True,
        }

        self.valid_data_2 = {
            'nome': 'João Pereira',
            'nome_social': '',
            'data_nascimento': '1985-03-22',
            'cpf': '987.654.321-00',
            'rg': '7654321',
            'orgao_emissor': 'SSP',
            'sexo': 'Masculino',
            'estado_civil': 'Casado',
            'nacionalidade': 'Brasileiro',
            'naturalidade': 'São Paulo',
            'endereco': 'Avenida Brasil, 45',
            'cep': '01000-000',
            'telefone': '(11)98888-9999',
            'email': 'joao@example.com',
            'tipo_deficiencia': 'Auditiva',
            'cid': 'H91',
            'necessidades_acessibilidade': 'Libras',
            'data_diagnostico': '2010-09-20',
            'numero_associado': 'A002',
            'status': 'ativo',
            'autorizacao_uso_imagem': False,
            'escolaridade': 'Superior Completo',
            'ocupacao': 'Engenheiro',
            'renda_familiar': '5000.00',
            'recebe_beneficio': 'Não',
            'participa_outros_programas': 'Nenhum',
            'ativo': True,
        }

    def test_formulario_associado_valido_cria_objeto(self):
        response_1 = self.client.post(reverse('cadastrar_associado'), self.valid_data_1)
        response_2 = self.client.post(reverse('cadastrar_associado'), self.valid_data_2)

        self.assertEqual(response_1.status_code, 302)  # Redirecionamento após sucesso
        self.assertEqual(response_2.status_code, 302)  # Redirecionamento após sucesso

        # Verificar se os objetos foram criados no banco de dados
        self.assertEqual(Associado.objects.count(), 2)

        # Verificar os dados dos associados criados
        associado_1 = Associado.objects.get(cpf='123.456.789-00')
        associado_2 = Associado.objects.get(cpf='987.654.321-00')

        self.assertEqual(associado_1.nome, 'Maria Silva')
        self.assertEqual(associado_1.email, 'maria@example.com')
        self.assertEqual(associado_2.nome, 'João Pereira')
        self.assertEqual(associado_2.email, 'joao@example.com')

    def test_template_lista_renderiza_associados(self):
        # Criando dois associados
        Associado.objects.create(
            nome='Lucas Oliveira',
            data_nascimento='1992-07-15',
            cpf='111.222.333-44',
            endereco='Rua B, 456',
            cep='66000-002',
            email='lucas@example.com',
            tipo_deficiencia='Nenhuma',
            numero_associado='A003',
            status='ativo',
            ativo=True,
        )
        Associado.objects.create(
            nome='Ana Souza',
            data_nascimento='1988-10-20',
            cpf='555.666.777-88',
            endereco='Avenida X, 789',
            cep='66000-003',
            email='ana@example.com',
            tipo_deficiencia='Visual',
            numero_associado='A004',
            status='ativo',
            ativo=True,
        )

        # Verificando se a lista de associados está sendo renderizada corretamente
        response = self.client.get(reverse('lista_associados'))
        self.assertContains(response, 'Lucas Oliveira')
        self.assertContains(response, 'Ana Souza')
