
# Dashboard de Monitoramento de VM

Este projeto é um dashboard para monitoramento em tempo real de máquinas virtuais (VMs), construído com **FastAPI**, **WebSockets** no backend e **React com TypeScript** (Vite) no frontend.

![Dashboard Preview](/dashboard%20vm/src/assets/dashboard.png)

## Funcionalidades

- Monitoramento em tempo real de métricas das VMs.
- Interface interativa e responsiva para visualização de dados.
- Comunicação bidirecional utilizando **WebSockets** para dados em tempo real.

## Tecnologias Utilizadas

- **Backend**: FastAPI, WebSockets
- **Dashboard vm**: React, TypeScript, Vite
- **Docker**: Docker Compose para facilitar a configuração e execução do ambiente

## Como Rodar o Projeto

1. **Clone este repositório**:

   ```bash
   git clone https://link-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Configure o ambiente Docker**:

   Na raiz do projeto, existe um arquivo `docker-compose.yml` que configura todos os serviços necessários, incluindo o backend, o frontend e o Redis.

3. **Suba os containers com Docker Compose**:

   Execute o comando abaixo para iniciar o projeto:

   ```bash
   docker-compose up --build
   ```

   Este comando vai:

   - Criar e iniciar os containers para o frontend e backend.
   - Configurar o Redis para a comunicação entre o frontend e o backend.

4. **Acesse o projeto**:

   Após o Docker Compose iniciar todos os containers, você pode acessar o dashboard em:

   ```
   http://localhost:3000
   ```

   A interface estará disponível para você começar a interagir com os dados das VMs.

## Estrutura do Projeto

- **backend/**: Contém o código do servidor FastAPI com WebSockets e integração com Redis.
- **dashboard vm/**: Código do cliente React, construído com Vite e TypeScript, responsável pela interface de usuário.
- **docker-compose.yml**: Arquivo de configuração do Docker Compose para rodar todos os serviços.
- **.env**: Arquivo de variáveis de ambiente para configuração do backend e frontend (se necessário).

## Como Contribuir

Se você deseja contribuir para o projeto, fique à vontade para fazer um fork do repositório e enviar um pull request com suas melhorias. Para novos recursos ou correções de bugs, abra uma **issue**.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
