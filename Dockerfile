# Usa a imagem slim (mais leve e com menos vulnerabilidades)
FROM python:3.13.3-slim-bullseye

# Evita criação de arquivos .pyc e ativa logs imediatos no console
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Cria um usuário não-root para segurança (evita rodar como root)
RUN addgroup --system django && adduser --system --ingroup django django

# Copia dependências antes do código para cache eficiente
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia os arquivos do projeto para o container
COPY . /app

# Permissão para o usuário não-root
RUN chown -R django:django /app

# Troca para o usuário de execução seguro
USER django

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
