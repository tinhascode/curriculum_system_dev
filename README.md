# Curriculo ATS API

Backend em FastAPI para montagem, visualização e exportação de currículos otimizados para sistemas ATS (Applicant Tracking Systems).

## Stack

- **Linguagem & Runtime:** Python 3.13+
- **Framework Web:** FastAPI
- **Configurações:** Pydantic Settings
- **Gerenciador de Dependências:** `uv`
- **Qualidade de Código:** Ruff (linter e formatador)
- **Testes:** Pytest + HTTPX (`TestClient`)
- **CI:** GitHub Actions

## Como Começar

### Pré-requisitos

- [uv](https://docs.astral.sh/uv/) instalado.
- Python 3.13+.

### Instalação

```bash
# Sincroniza o ambiente e instala dependências
make install
# ou: uv sync
```

### Configuração do Ambiente

Copie o arquivo de exemplo de variáveis:

```bash
cp .env.example .env
```

### Executando em Modo Desenvolvimento

```bash
make dev
# ou: uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Acesse:
- **Health check:** [http://localhost:8000/health](http://localhost:8000/health)
- **Documentação Swagger (OpenAPI):** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Documentação ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Comandos Úteis

```bash
make test    # Executa a suíte de testes com pytest
make lint    # Roda o ruff check
make format  # Formata o código com ruff
make check   # Executa lint e testes
```

## Licença

Este projeto está sob a licença [MIT](LICENSE).
