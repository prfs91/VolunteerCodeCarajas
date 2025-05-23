# Generated by Django 5.2 on 2025-04-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("associados", "0002_associado_autorizacao_uso_imagem_associado_cep_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="associado",
            name="endereco",
        ),
        migrations.AddField(
            model_name="associado",
            name="bairro",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="associado",
            name="cidade",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="associado",
            name="complemento",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="associado",
            name="logradouro",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="associado",
            name="uf",
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
