# Etapa 1: Construção da aplicação
FROM node:18-alpine AS build

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
COPY package.json package-lock.json ./

# Instala as dependências
RUN npm install

# Copia o restante dos arquivos do projeto
COPY . .

# Gera a build de produção
RUN npm run build

# Etapa 2: Servindo a aplicação com Nginx
FROM nginx:1.21.5-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
# Copia os arquivos da build para o diretório padrão do Nginx
COPY --from=build /app/dist /usr/share/nginx/html
# Adicione isso antes do CMD no seu Dockerfile
RUN chmod -R 755 /usr/share/nginx/html
# Remove a configuração padrão do Nginx

# Expondo a porta padrão do Nginx
EXPOSE 80

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]