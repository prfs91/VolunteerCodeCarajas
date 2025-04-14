# Setup do Projeto - Passo a Passo 🚀

Este guia vai te ajudar a configurar o ambiente para rodar o projeto **VolunteerCodeCarajas** no seu computador, tanto no **Windows** quanto no **Linux**. Vamos fazer isso com o ambiente virtual e a instalação das dependências automaticamente! 💻

---

## 🪟 **Para Windows** (PowerShell)

### 1️⃣ **Verifique se o PowerShell está configurado para rodar scripts**

No Windows, a execução de scripts PowerShell pode ser bloqueada por segurança. Vamos liberar a execução para que o script funcione corretamente.

#### 🔑 **Permissões de Execução**

Abra o **PowerShell como administrador** (clique com o botão direito em "Windows PowerShell" e selecione **"Executar como administrador"**).

Execute o seguinte comando:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Isso permite que você execute scripts baixados, desde que tenham uma assinatura confiável.

### 2️⃣ **Baixe o Repositório**
Abra o **PowerShell** no diretório onde você quer salvar o projeto e execute o seguinte:

```powershell
git clone https://github.com/prfs91/VolunteerCodeCarajas.git
cd VolunteerCodeCarajas
```
### 3️⃣ **Criação e Ativação do Ambiente Virtual**
Agora vamos garantir que o ambiente virtual esteja configurado corretamente. No PowerShell, execute o script start.ps1.

Execute o seguinte comando:

```powershell
.\start.ps1
```
Isso irá:

- **Criar um ambiente virtual** se ele não existir ainda.

- **Ativar o ambiente virtual**.

- **Instalar as dependências** do requirements.txt.

### 4️⃣ **Abrir o Projeto no VS Code**
Agora, abra o projeto no VS Code diretamente do PowerShell:

```powershell
code .
```

Isso abrirá o **VS Code** com o ambiente virtual ativado e as dependências instaladas.

## 🐧 **Para Linux** (Terminal)
### 1️⃣ **Instalar Dependências do Sistema**
Antes de tudo, você pode precisar garantir que tem o Python, Git e pip instalados. No terminal, execute:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git
```

### 2️⃣ **Baixe o Repositório**
No terminal, navegue até o diretório onde você quer baixar o projeto e execute:

```bash
git clone https://github.com/prfs91/VolunteerCodeCarajas.git
cd VolunteerCodeCarajas
```

### 3️⃣ **Criação e Ativação do Ambiente Virtual**
Agora, vamos criar o ambiente virtual e ativá-lo. Execute:

```bash
python3 -m venv venv
source venv/bin/activate
```
Isso criará e ativará o ambiente virtual.

### 4️⃣ **Instalar as Dependências**
Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```
### 5️⃣ **Abrir o Projeto no VS Code**
Agora, abra o projeto no **VS Code** diretamente do terminal:

```bash
code .
```
Isso abrirá o **VS Code** com o ambiente virtual ativado e as dependências instaladas.

## 🚨 **Problemas Comuns**
### ❌ **Erro: Não é possível rodar o script no PowerShell**
Se ao rodar o start.ps1 você receber um erro dizendo que não tem permissões, execute o comando:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Isso deve corrigir o erro.
