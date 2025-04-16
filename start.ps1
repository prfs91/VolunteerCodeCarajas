# Muda para o diretório onde o script está localizado (diretório do projeto)
Set-Location -Path (Split-Path -Parent $MyInvocation.MyCommand.Definition)

# Verifica se o ambiente virtual existe, se não, cria
if (-Not (Test-Path ".\.venv"))
{
    Write-Host "Criando o ambiente virtual..."
    python -m venv venv
}

# Ativa o ambiente virtual
Write-Host "Ativando o ambiente virtual..."
.venv\Scripts\Activate.ps1

# Instala as dependências do requirements.txt
Write-Host "Instalando dependencias..."
pip install -r requirements.txt

# Abre o projeto no VS Code
Write-Host "Abrindo VS Code..."
code .