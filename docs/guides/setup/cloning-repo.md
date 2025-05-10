<!--

docs/
├── guides/                          	    # Guias práticos agrupados por domínio
│   ├── setup/                       	    # Passo-a-passo de ambiente
│   │   ├── 01-cloning-repo.md       	    # Clonagem do repositório
│   │   ├── 02-configure-start-ps1.md	    # Configurar PowerShell
│   │   ├── 03-postgresql-windows.md 	    # PostgreSQL no Windows
│   │   └── 04-docker-setup.md       	    # Ambiente Docker

# Clonagem do repositório

-->

# 📥 Clonagem do Repositório

## 🛠️ Pré-requisitos
- [Git instalado](https://git-scm.com/downloads) *(v2.40+ recomendado)*
- 📝 Conta no [GitHub](https://github.com/signup)

---

## 🚀 Passo a Passo 

### 1. 🍴 Fazer Fork do Repositório
1. Acesse o [repositório original](https://github.com/prfs91/VolunteerCodeCarajas)
2. Clique no botão **`Fork`** no canto superior direito
3. Selecione sua conta como destino

### Por que fazemos isso?

Ao fazer um fork, criamos uma cópia do repositório original na sua conta do GitHub. Clonando esse fork para sua máquina, você pode começar a trabalhar no código localmente, de maneira segura, sem afetar o repositório original.

---

### 2. 💻 Clonar para Sua Máquina

#### Para iniciantes (HTTPS) 🌐
```bash
git clone https://github.com/SEU-USERNAME/VolunteerCodeCarajas.git
```
#### Para avançados (SSH) 🔒
```bash
git clone git@github.com:SEU-USERNAME/VolunteerCodeCarajas.git
```
#### 2.2. Abrir o Terminal

> No Windows, você pode usar o **PowerShell** ou o **Git Bash**  
> No macOS/Linux, use o terminal padrão do sistema

#### 3. 📂 Navegar até a Pasta do Projeto
```bash
# Navegue para sua pasta de projetos
cd ~/Desktop/projetos

# Execute o clone
git clone git@github.com:SEU-USERNAME/VolunteerCodeCarajas.git
```
Por que fazemos isso?

Para poder executar os comandos do Git no repositório clonado, precisamos estar dentro da pasta do projeto. Isso permite que você realize ações como commits, pushes e fetches no diretório correto.

### 4. 🔍 Verificar o Status do Git
```
git status
```
Por que fazemos isso?


O comando git status é utilizado para verificar o estado atual do seu repositório. Ele mostra se há alterações não registradas ou pendentes, e também nos diz qual branch estamos trabalhando. Assim, garantimos que estamos prontos para a próxima etapa.


### 5. 🔄 Configurar Sincronização com o Original

```
git remote add upstream git@github.com:prfs91/VolunteerCodeCarajas.git

```
Por que fazemos isso?

Quando você faz um fork de um repositório, o GitHub cria uma cópia na sua conta. No entanto, você precisa acompanhar as atualizações feitas no repositório original (o "upstream"). Ao adicionar o repositório original como um "remote", você consegue trazer essas atualizações para o seu repositório local e manter o fork atualizado.

### 6. ⬇️ Buscar Atualizações do Repositório Original
```
git fetch upstream

```
Por que fazemos isso?

As mudanças feitas no repositório original (upstream) não aparecem automaticamente no seu fork. Com o comando git fetch, você traz as últimas atualizações do repositório original para o seu ambiente local. Isso é essencial para garantir que seu fork esteja atualizado e sincronizado com o trabalho de outros colaboradores.

### 7. 🔄 Mesclar as Atualizações na Sua Branch main

```
git merge upstream/main
```
Por que fazemos isso?

Agora que você tem as atualizações do repositório original, é hora de integrá-las ao seu fork. O comando git merge aplica as mudanças da branch main do repositório original (upstream) à sua branch main. Isso evita que seu fork fique desatualizado em relação ao código mais recente do projeto.

### 8. 🚀 Enviar as Atualizações para o Seu Fork

```
git push origin main
```

Por que fazemos isso?

Após mesclar as alterações da branch main do repositório original no seu repositório local, você precisa enviar essas alterações de volta para o seu repositório no GitHub. Isso garante que o seu repositório forkado esteja sincronizado com o repositório original e pronto para novas contribuições.

---

### ✅ Resultado Final

Ao concluir essas etapas, seu repositório estará sincronizado com o repositório original, garantindo que você tenha as últimas atualizações e esteja pronto para contribuir ou continuar desenvolvendo no projeto. Isso também facilita a colaboração, pois todos os envolvidos terão a mesma versão atualizada do código. 🎉

---
> ⚠️ **Aviso Importante:**
> 
> Esta documentação está em fase de desenvolvimento. 
> Algumas seções podem estar incompletas ou temporariamente indisponíveis.
> Atualizações estão sendo realizadas de forma contínua para aprimorar o conteúdo.

---

<p align="center">
  📚 Este documento integra a documentação oficial do projeto <strong>VolunteerCodeCarajas</strong>.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/robertaferreira91/" target="_blank"><img width="25" height="25" title="LinkedIn" src="https://img.icons8.com/?size=100&id=xuvGCOXi8Wyg&format=png&color=000000"/></a>
  <a href="mailto:pamellaferreira.si@gmail.com" target="_blank"><img width="25" height="25" title="Gmail" src="https://img.icons8.com/?size=100&id=P7UIlhbpWzZm&format=png&color=000000"/></a>
  <a href="https://wa.me/5594992797521?text=Ol%C3%A1%21%20Encontrei%20seu%20contato%20atrav%C3%A9s%20do%20GitHub%20e%20gostaria%20de%20conversar%20com%20voc%C3%AA.%20Podemos%20falar%20um%20pouquinho%3F" target="_blank"><img width="25" height="25" title="WhatsApp" src="https://img.icons8.com/?size=100&id=16713&format=png&color=000000"/></a>
  <a href="https://github.com/prfs91" target="_blank"><img width="25" height="25" title="GitHub" src="https://img.icons8.com/?size=100&id=bVGqATNwfhYq&format=png&color=000000"/></a><br>
  <strong>🔖 Licença:</strong> MIT License <br>
  © 2025 - Roberta Ferreira
</p>

---

<p align="right">
  <strong>📅 Última atualização:</strong> 09/05/2025
</p>
