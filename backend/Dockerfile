# Usar uma imagem base com Python
FROM python:3.9-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y gcc libpq-dev

# Criar um diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt
# COPY requirements.txt /app/

# Instalar as dependências do projeto

# Copiar todo o conteúdo da pasta 'app' para o contêiner
COPY ./app /app/
# Definir PYTHONPATH para garantir que o Python encontre o diretório 'app'
ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta que a aplicação vai rodar
EXPOSE 8000

# Comando para rodar o servidor FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
