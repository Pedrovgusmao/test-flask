# 🐍 Servidor Flask Local com Ambiente Virtual

Um servidor Flask completo com ambiente virtual isolado para desenvolvimento.

## 🚀 Setup Rápido

### Opção 1: Script Automático
```bash
# Execute o script de setup
./setup.sh
```

### Opção 2: Manual
```bash
# 1. Criar ambiente virtual
python3 -m venv first-server

# 2. Ativar ambiente virtual
source first-server/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar servidor
python app.py
```

## 🔧 Como usar

### 1. Ativar o ambiente virtual
```bash
source first-server/bin/activate
```

### 2. Executar o servidor
```bash
python app.py
```

### 3. Acessar no navegador
- **Página inicial**: http://localhost:5000
- **Página de teste**: http://localhost:5000/test

### 4. Desativar o ambiente (quando terminar)
```bash
deactivate
```

## 📦 Dependências

- **Flask 2.3.3** - Framework web
- **Flask-CORS 4.0.0** - CORS para desenvolvimento
- **python-dotenv 1.0.0** - Variáveis de ambiente
- **pytest 7.4.2** - Testes
- **black 23.7.0** - Formatação de código
- **flake8 6.0.0** - Linting

## 🌐 APIs Disponíveis

- **`/api/info`** - Informações do servidor
- **`/api/files`** - Lista arquivos do diretório
- **`/api/time`** - Hora atual
- **`/api/status`** - Status do servidor

## 📁 Estrutura do Projeto

```
primeiro-servidor/
├── first-server/           # Ambiente virtual
├── templates/             # Templates HTML
│   ├── index.html
│   └── test.html
├── static/                  # Arquivos estáticos
├── app.py                   # Servidor Flask
├── requirements.txt         # Dependências
├── setup.sh                # Script de setup
└── README.md               # Este arquivo
```

## 🎯 Vantagens do Ambiente Virtual

- ✅ **Isolamento**: Bibliotecas não conflitam com o sistema
- ✅ **Controle de versões**: Cada projeto tem suas dependências
- ✅ **Reproduzibilidade**: Mesmo ambiente em qualquer máquina
- ✅ **Limpeza**: Fácil de remover quando não precisar

## 🧪 Testando

1. **Execute o servidor:**
   ```bash
   source venv/bin/activate
   python app.py
   ```

2. **Teste as APIs:**
   ```bash
   curl http://localhost:5000/api/info
   curl http://localhost:5000/api/files
   curl http://localhost:5000/api/time
   ```

3. **Acesse no navegador:**
   - http://localhost:5000 (página inicial)
   - http://localhost:5000/test (página de teste)

## 🔄 Comandos Úteis

```bash
# Ativar ambiente
source first-server/bin/activate

# Desativar ambiente
deactivate

# Instalar nova dependência
pip install nome-da-biblioteca

# Salvar dependências
pip freeze > requirements.txt

# Remover ambiente virtual
rm -rf first-server
```

## 🛑 Parar o Servidor

Pressione `Ctrl+C` no terminal onde o servidor está rodando.

## 🎉 Próximos Passos

- [ ] Adicionar banco de dados
- [ ] Criar autenticação
- [ ] Adicionar upload de arquivos
- [ ] Implementar WebSocket
- [ ] Criar dashboard
