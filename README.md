# 🎬 CRUD de Filmes - FastAPI + PostgreSQL

Um projeto simples para aprender FastAPI, Docker e banco de dados relacional. Esta API permite gerenciar um catálogo de filmes com operações CRUD básicas e integração com a API pública OMDb.

## 🚀 Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para Python
- **PostgreSQL** - Banco de dados relacional
- **Docker & Docker Compose** - Containerização
- **Requests** - Para consumir API externa

## 📁 Estrutura do Projeto

```
crud_filmes/
│
├── main.py           # Rotas da API FastAPI
├── models.py         # Modelos SQLAlchemy
├── database.py       # Configuração do banco
├── schemas.py        # Schemas Pydantic
├── crud.py           # Operações CRUD
├── requirements.txt  # Dependências Python
├── docker-compose.yml# Configuração Docker
├── Dockerfile        # Imagem da aplicação
└── README.md         # Este arquivo
```

## 🎯 Funcionalidades da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/` | Página inicial da API |
| `GET` | `/filmes` | Lista todos os filmes |
| `POST` | `/filmes` | Adiciona um novo filme |
| `GET` | `/filmes/{id}` | Busca filme por ID |
| `PUT` | `/filmes/{id}` | Atualiza um filme existente |
| `DELETE` | `/filmes/{id}` | Remove um filme |
| `POST` | `/importar/{titulo}` | Importa filme da OMDb API |

## 🎭 Modelo de Dados

Cada filme possui os seguintes campos:

```json
{
  "id": 1,
  "titulo": "Matrix",
  "ano": "1999",
  "genero": "Action, Sci-Fi",
  "nota": 8.7
}
```

## 🐳 Como Executar

### Pré-requisitos
- Docker
- Docker Compose

### Passo a passo

1. **Clone ou baixe o projeto**
   ```bash
   cd crud_filmes
   ```

2. **Suba os containers**
   ```bash
   docker-compose up --build
   ```

3. **Acesse a API**
   - API: http://localhost:8000
   - Documentação interativa: http://localhost:8000/docs
   - Banco PostgreSQL: localhost:5432

## 📝 Exemplos de Uso

### 1. Listar todos os filmes
```bash
curl http://localhost:8000/filmes
```

### 2. Adicionar um filme
```bash
curl -X POST "http://localhost:8000/filmes" \
     -H "Content-Type: application/json" \
     -d '{
       "titulo": "Inception",
       "ano": "2010",
       "genero": "Action, Sci-Fi, Thriller",
       "nota": 8.8
     }'
```

### 3. Buscar filme por ID
```bash
curl http://localhost:8000/filmes/1
```

### 4. Atualizar um filme
```bash
curl -X PUT "http://localhost:8000/filmes/1" \
     -H "Content-Type: application/json" \
     -d '{
       "titulo": "The Matrix",
       "ano": "1999",
       "genero": "Action, Sci-Fi, Thriller",
       "nota": 8.9
     }'
```

### 5. Importar filme da OMDb
```bash
curl -X POST "http://localhost:8000/importar/Matrix"
```

### 6. Deletar um filme
```bash
curl -X DELETE "http://localhost:8000/filmes/1"
```

## 🌐 Integração com OMDb API

A rota `/importar/{titulo}` busca informações de filmes na [OMDb API](http://www.omdbapi.com/) e salva automaticamente no banco de dados.

**Nota**: Para usar a OMDb API em produção, você precisa de uma chave gratuita. Substitua a chave no arquivo `crud.py`.

## 🗄️ Banco de Dados

- **Nome**: `filmesdb`
- **Usuário**: `postgres`
- **Senha**: `postgres`
- **Porta**: `5432`

O banco é criado automaticamente pelo Docker Compose e as tabelas são geradas na primeira execução da API.

## 🛠️ Desenvolvimento

### Estrutura simples para aprendizado

Este projeto foi desenvolvido com foco na simplicidade e clareza, ideal para quem está aprendendo:

- **Arquivos únicos**: Cada responsabilidade em um arquivo específico
- **Código direto**: Sem abstrações complexas
- **Comentários explicativos**: Para facilitar o entendimento
- **Docker**: Para evitar problemas de ambiente

### Para modificar o código

1. Faça as alterações nos arquivos Python
2. O container da API tem volume mapeado, então as mudanças são refletidas automaticamente
3. Se alterar dependências, reconstrua: `docker-compose up --build`

## 🚦 Status da API

Quando tudo estiver funcionando, você verá:

```
✅ API rodando em: http://localhost:8000
✅ Documentação em: http://localhost:8000/docs  
✅ PostgreSQL conectado
✅ Tabelas criadas automaticamente
```

## 📚 Próximos Passos

Ideias para expandir o projeto:

- [ ] Adicionar autenticação JWT
- [ ] Implementar paginação
- [ ] Adicionar filtros de busca
- [ ] Criar testes automatizados
- [ ] Adicionar cache com Redis
- [ ] Interface web simples

---

**Feito com ❤️ para aprender FastAPI, Docker e PostgreSQL**
