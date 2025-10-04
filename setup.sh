#!/bin/bash

echo "🐍 Configurando Ambiente Virtual Python"
echo "========================================"

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Instale o Python primeiro."
    exit 1
fi

# Criar ambiente virtual
echo "📁 Criando ambiente virtual..."
python3 -m venv first-server

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source first-server/bin/activate

# Atualizar pip
echo "⬆️ Atualizando pip..."
pip install --upgrade pip

# Instalar dependências
echo "📦 Instalando dependências..."
pip install -r requirements.txt

echo ""
echo "✅ Ambiente configurado com sucesso!"
echo ""
echo "🚀 Para usar o servidor:"
echo "1. Ative o ambiente: source first-server/bin/activate"
echo "2. Execute o servidor: python app.py"
echo ""
echo "🛑 Para desativar: deactivate"
