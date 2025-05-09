import requests  # importa biblioteca para fazer requisições HTTP

# Define o proprietário e o nome do repositório
OWNER = "prfs91"
REPO = "VolunteerCodeCarajas"
LIMIT = 30  # Limita o número de contribuidores exibidos (pode ajustar)

# Faz a requisição para a API de contribuidores do GitHub
url = f"https://api.github.com/repos/{OWNER}/{REPO}/contributors"
res = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if res.status_code != 200:
    print("Erro ao buscar contribuidores")
    exit(1)

# Ordena os contribuidores pelo número de contribuições (commits), do maior para o menor
contributors = sorted(res.json(), key=lambda c: c["contributions"], reverse=True)

# Monta o bloco de markdown com as fotos e links dos contribuidores
bloco_contribuidores = "## 👥 Contribuidores\n\n"
for c in contributors[:LIMIT]:
    login = c["login"]
    avatar = c["avatar_url"]
    profile = c["html_url"]
    contribs = c["contributions"]
    bloco_contribuidores += f'[<img src="{avatar}" width="60px" title="{login} - {contribs} contribuições"/>]({profile})\n'

# Lê o conteúdo atual do README.md
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Procura pelos marcadores de início e fim onde será inserido o conteúdo
inicio = readme.find("<!-- INICIO-CONTRIBUIDORES -->")
fim = readme.find("<!-- FIM-CONTRIBUIDORES -->")

# Se encontrou os marcadores, substitui o conteúdo entre eles
if inicio != -1 and fim != -1:
    novo_readme = (
        readme[:inicio + len("<!-- INICIO-CONTRIBUIDORES -->")] +
        "\n\n" + bloco_contribuidores + "\n" +
        readme[fim:]
    )

    # Salva o novo README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(novo_readme)
else:
    print("Marcadores de contribuição não encontrados no README.")
    exit(1)
