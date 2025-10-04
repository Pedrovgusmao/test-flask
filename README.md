# 🚀 Servidor Flask com Supabase

Um servidor Flask completo com integração ao Supabase (PostgreSQL na nuvem) e ambiente virtual isolado.

## ✨ Funcionalidades

- 🐍 **Flask 2.3.3** - Framework web moderno
- 🗄️ **Supabase** - Banco de dados PostgreSQL na nuvem
- 🔐 **APIs REST** - CRUD completo para usuários e posts
- 🎨 **Design Apple** - Interface moderna e responsiva
- 🔧 **Ambiente Virtual** - Isolamento completo de dependências
- 🐳 **Docker** - Containerização para produção

## 🚀 Setup Rápido

### **1. Configurar Supabase:**
1. Acesse [supabase.com](https://supabase.com)
2. Crie um novo projeto
3. Copie a URL e chave anônima
4. Crie arquivo `.env` com suas credenciais:

```bash
# .env
SUPABASE_URL=sua_url_aqui
SUPABASE_KEY=sua_chave_aqui
SECRET_KEY=sua_chave_secreta_aqui
```

### **2. Instalar dependências:**
```bash
# Ativar ambiente virtual
source first-server/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### **3. Executar servidor:**
```bash
python app.py
```

## 🌐 APIs Disponíveis

### **👥 Usuários:**
- `GET /api/users` - Listar usuários
- `POST /api/users` - Criar usuário
- `GET /api/users/{id}` - Buscar usuário
- `PUT /api/users/{id}` - Atualizar usuário
- `DELETE /api/users/{id}` - Deletar usuário

### **📝 Posts:**
- `GET /api/posts` - Listar posts
- `POST /api/posts` - Criar post
- `GET /api/posts/{id}` - Buscar post
- `PUT /api/posts/{id}` - Atualizar post
- `DELETE /api/posts/{id}` - Deletar post

### **📊 Sistema:**
- `GET /api/info` - Informações do servidor
- `GET /api/status` - Status do sistema
- `GET /api/time` - Hora atual
- `GET /api/files` - Lista arquivos

## 🗄️ Estrutura do Banco

### **Tabela Users:**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    is_active BOOLEAN DEFAULT TRUE
);
```

### **Tabela Posts:**
```sql
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    is_published BOOLEAN DEFAULT FALSE
);
```

## 🧪 Testando

### **1. Acesse as páginas:**
- **Página inicial:** http://localhost:8000
- **Página de teste:** http://localhost:8000/test

### **2. Teste as APIs:**
```bash
# Listar usuários
curl http://localhost:8000/api/users

# Criar usuário
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "João", "email": "joao@exemplo.com"}'

# Listar posts
curl http://localhost:8000/api/posts

# Criar post
curl -X POST http://localhost:8000/api/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "Meu Post", "content": "Conteúdo do post", "author_id": 1}'
```

## 🐳 Docker

### **Construir imagem:**
```bash
docker build -t meu-servidor-flask .
```

### **Executar container:**
```bash
docker run -p 8000:8000 meu-servidor-flask
```

### **Docker Compose:**
```bash
docker-compose up
```

## 📁 Estrutura do Projeto

```
primeiro-servidor/
├── first-server/           # Ambiente virtual
├── templates/             # Templates HTML
│   ├── index.html
│   └── test.html
├── static/                # Arquivos estáticos
├── app.py                 # Servidor Flask principal
├── config.py              # Configurações
├── models.py              # Modelos de dados
├── supabase_service.py    # Serviço Supabase
├── requirements.txt       # Dependências
├── Dockerfile            # Configuração Docker
├── docker-compose.yml    # Orquestração Docker
├── .dockerignore         # Ignorar arquivos Docker
├── .gitignore           # Ignorar arquivos Git
└── README.md            # Este arquivo
```

## 🔧 Configuração do Supabase

### **1. Criar projeto no Supabase:**
- Acesse [supabase.com](https://supabase.com)
- Clique em "New Project"
- Escolha organização e nome do projeto
- Aguarde a criação

### **2. Obter credenciais:**
- Vá em Settings → API
- Copie a URL e chave anônima
- Cole no arquivo `.env`

### **3. Criar tabelas:**
- Vá em Table Editor
- Crie as tabelas `users` e `posts`
- Ou use o SQL Editor para executar os scripts

## 🎯 Vantagens

### **✅ Supabase:**
- **PostgreSQL** na nuvem
- **APIs automáticas** geradas
- **Autenticação** integrada
- **Dashboard** visual
- **Escalabilidade** automática

### **✅ Flask:**
- **Framework** Python moderno
- **APIs REST** fáceis
- **Templates** HTML
- **Flexibilidade** total

### **✅ Ambiente Virtual:**
- **Isolamento** de dependências
- **Controle** de versões
- **Reproduzibilidade**
- **Limpeza** fácil

## 🚀 Deploy

### **Heroku:**
```bash
# Instalar Heroku CLI
# Criar Procfile
echo "web: python app.py" > Procfile

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### **Railway:**
```bash
# Conectar repositório
# Configurar variáveis de ambiente
# Deploy automático
```

### **DigitalOcean:**
```bash
# Criar droplet
# Instalar Docker
# Executar container
```

## 🛑 Parar o Servidor

Pressione `Ctrl+C` no terminal onde o servidor está rodando.

## 🎉 Próximos Passos

- [ ] Adicionar autenticação JWT
- [ ] Implementar upload de arquivos
- [ ] Criar dashboard administrativo
- [ ] Adicionar testes automatizados
- [ ] Implementar cache Redis
- [ ] Configurar CI/CD