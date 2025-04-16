# Usa a imagem slim (mais leve e com menos vulnerabilidades)
FROM python:3.13.3-slim-bullseye

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Instala dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]