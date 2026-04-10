
# Dashboard de Monitoramento de VM

![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=flat&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/JefteSG/Dashboard_Monitor_VM)

**Dashboard de métricas de VMs com alertas em tempo real**

![Dashboard Preview](dashboard%20vm/src/assets/dashboard.png)

## 🚀 Como Rodar

```bash
git clone git@github.com:JefteSG/Dashboard_Monitor_VM.git
cd Dashboard_Monitor_VM
docker-compose up --build
```

Acesse em: **http://localhost:3000**

## 🎯 Decisões Técnicas

### Por que TypeScript?
- **Type safety** — erros capturados em tempo de compilação, não em produção
- **Melhor DX** — autocomplete e refatoração segura no VSCode
- **Manutenibilidade** — código autodocumentado com interfaces explícitas

### Por que FastAPI?
- **Performance** — async nativo e um dos frameworks Python mais rápidos
- **WebSockets out-of-the-box** — essencial para streaming de métricas em tempo real
- **Documentação automática** — Swagger/OpenAPI gerado automaticamente

### Stack Escolhida
- **Frontend**: React + TypeScript + Vite — build rápido e HMR instantâneo
- **Backend**: FastAPI + WebSockets — comunicação bidirecional para métricas em tempo real
- **Infraestrutura**: Docker Compose — ambiente reproduzível em qualquer máquina

## 📦 Funcionalidades

- Monitoramento em tempo real de CPU, memória e disco das VMs
- Alertas automáticos configuráveis por métrica
- Comunicação bidirecional via WebSockets
- Interface responsiva e intuitiva

## 📁 Estrutura do Projeto

```
├── backend/              # FastAPI + WebSockets
├── dashboard vm/         # React + TypeScript + Vite
└── docker-compose.yml    # Orquestração de serviços
```

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
