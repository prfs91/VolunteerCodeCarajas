# Muda para o diretório onde o script está localizado (diretório do projeto)
# Isso é feito para garantir que o script sempre execute a partir do diretório correto, independentemente de onde o terminal esteja.
Set-Location -Path (Split-Path -Parent $MyInvocation.MyCommand.Definition)


# Verifica se o ambiente virtual (.venv) já existe no diretório atual.
# Caso não exista, ele irá criar um novo ambiente virtual usando o comando `python -m venv`.
if (-Not (Test-Path ".\.venv"))
{
    Write-Host "Criando o ambiente virtual..." # Informa ao usuário que o ambiente virtual está sendo criado
    python -m venv .venv # Cria o ambiente virtual .venv no diretório atual
}


# Ativa o ambiente virtual que foi criado ou já existia
# O comando abaixo executa o script de ativação do ambiente virtual no PowerShell.
# O operador & chama o script Activate.ps1, e as aspas são usadas para garantir que o caminho seja interpretado corretamente.
Write-Host "Ativando o ambiente virtual..." # Informa ao usuário que o ambiente virtual está sendo ativado
& ".\.venv\Scripts\Activate.ps1" # Ativa o ambiente virtual .venv no PowerShell


# Informa ao usuário que o script está verificando as dependências listadas no arquivo requirements.txt
Write-Host "Verificando dependências..."

# Cria uma variável que armazena a lista de pacotes instalados no ambiente virtual
# O comando `pip freeze` gera uma lista de todos os pacotes instalados e suas versões no formato "pacote==versão"
$installedPackages = pip freeze

# Cria uma variável que armazena o conteúdo do arquivo requirements.txt, que lista as dependências necessárias para o projeto
# O `Get-Content` lê as linhas do arquivo e armazena cada uma como uma string no array
$requiredPackages = Get-Content "requirements.txt"

# Inicializa uma lista vazia para armazenar pacotes faltantes ou desatualizados
$missingOrOutdated = @()

# Percorre cada linha do arquivo requirements.txt, onde cada linha representa uma dependência
foreach ($line in $requiredPackages) {

    # Usa uma expressão regular para separar o nome do pacote e a versão exigida no requirements.txt
    # Se a linha estiver no formato correto "pacote==versão", o nome e a versão serão extraídos
    if ($line -match "^(.*)==(.*)$") {
        $packageName = $matches[1]  # Armazena o nome do pacote (antes do '==')
        $requiredVersion = $matches[2]  # Armazena a versão requerida (após o '==')

        # Procura o pacote instalado que corresponde ao nome do pacote no requirements.txt
        # O `Where-Object` busca no array de pacotes instalados o nome que começa com o nome do pacote atual
        $installedPackage = $installedPackages | Where-Object { $_ -like "$packageName*" }

        # Se o pacote não foi encontrado na lista de pacotes instalados
        if ($installedPackage -eq $null) {
            # Adiciona o pacote à lista de pacotes faltantes
            $missingOrOutdated += $line
        }
        else {
            # Se o pacote foi encontrado, compara a versão instalada com a versão requerida
            $installedVersion = ($installedPackage -split "==")[1]  # Obtém a versão do pacote instalado

            # Se a versão instalada for diferente da versão exigida, adiciona o pacote à lista de pacotes desatualizados
            if ($installedVersion -ne $requiredVersion) {
                $missingOrOutdated += $line  # Adiciona à lista de pacotes desatualizados
            }
        }
    }
}

# Verifica se há pacotes faltantes ou desatualizados na lista
if ($missingOrOutdated.Count -gt 0) {
    # Informa ao usuário que as dependências serão instaladas ou atualizadas
    Write-Host "Instalando/Atualizando dependências..."

    # Instala os pacotes que estão faltando ou desatualizados
    # O `pip install` irá instalar ou atualizar os pacotes necessários
    pip install $missingOrOutdated
} else {
    # Informa ao usuário que todas as dependências estão instaladas e atualizadas
    Write-Host "Todas as dependências estão instaladas e atualizadas."
}

# Abre o projeto no Visual Studio Code (VS Code)
# O comando `code .` abre o diretório atual no VS Code para que você possa editar o código.
Write-Host "Abrindo VS Code..." # Informa ao usuário que o VS Code está sendo aberto
code . # Abre o diretório do projeto no VS Code
