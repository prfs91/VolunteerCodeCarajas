from django.contrib import messages  # Para exibir mensagens no template
from django.shortcuts import redirect, render

from .forms import AssociadoForm
from .models import Associado


# Exibe o formulário e processa o cadastro de associado
def cadastrar_associado(request):
    if request.method == 'POST':
        # Inclui request.FILES para lidar com uploads de arquivos
        form = AssociadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Salva o novo associado no banco de dados
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('lista_associados')  # Redireciona para a lista após salvar
    else:
        form = AssociadoForm()

    return render(request, 'associados/cadastrar.html', {'form': form})


# Exibe uma lista com todos os associados cadastrados
def lista_associados(request):
    associados = Associado.objects.all()
    return render(request, 'associados/lista.html', {'associados': associados})
