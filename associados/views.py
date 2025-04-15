from django.shortcuts import render
from .forms import AssociadoForm
from .models import Associado

# Exibe o formulário e processa o cadastro de associado
def cadastrar_associado(request):
    if request.method == 'POST':
        form = AssociadoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo associado no banco
            return redirect('lista_associados')  # Redireciona após salvar
    else:
        form = AssociadoForm()
    return render(request, 'associados/cadastrar.html', {'form': form})

# Exibe uma lista com todos os associados cadastrados
def lista_associados(request):
    associados = Associado.objects.all()
    return render(request, 'associados/lista.html', {'associados': associados})