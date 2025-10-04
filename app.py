#!/usr/bin/env python3
"""
Servidor Flask Local
Ambiente isolado com todas as dependências
"""

from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import json
from datetime import datetime
import time

# Criar a aplicação Flask
app = Flask(__name__)
CORS(app)  # Permitir CORS para desenvolvimento

# Configurações
app.config['SECRET_KEY'] = 'desenvolvimento-local'
PORT = 8000

@app.route('/')
def home():
    """Página inicial"""
    return render_template('index.html')

@app.route('/api/info')
def api_info():
    """API - Informações do servidor"""
    return jsonify({
        'servidor': 'Flask Local',
        'versao': '1.0.0',
        'porta': PORT,
        'timestamp': datetime.now().isoformat(),
        'diretorio': os.getcwd(),
        'python_version': os.sys.version,
        'flask_version': '2.3.3'
    })

@app.route('/api/files')
def api_files():
    """API - Lista arquivos do diretório"""
    files = []
    for item in os.listdir('.'):
        item_path = os.path.join('.', item)
        if os.path.isfile(item_path):
            stat = os.stat(item_path)
            files.append({
                'nome': item,
                'tamanho': stat.st_size,
                'modificado': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'tipo': 'arquivo'
            })
        elif os.path.isdir(item_path):
            files.append({
                'nome': item,
                'tipo': 'diretorio'
            })
    
    return jsonify({
        'diretorio': os.getcwd(),
        'total': len(files),
        'arquivos': files
    })

@app.route('/api/time')
def api_time():
    """API - Hora atual"""
    now = datetime.now()
    return jsonify({
        'timestamp': now.isoformat(),
        'formato_brasileiro': now.strftime('%d/%m/%Y %H:%M:%S'),
        'unix_timestamp': int(time.time())
    })

@app.route('/api/status')
def api_status():
    """API - Status do servidor"""
    return jsonify({
        'status': 'online',
        'uptime': 'N/A',
        'memoria': 'N/A'
    })

@app.route('/test')
def test_page():
    """Página de teste"""
    return render_template('test.html')

# Servir arquivos estáticos
@app.route('/static/<path:filename>')
def static_files(filename):
    """Servir arquivos estáticos"""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 SERVIDOR FLASK LOCAL")
    print("=" * 60)
    print(f"📁 Diretório: {os.getcwd()}")
    print(f"🌐 URL: http://localhost:{PORT}")
    print(f"📊 API: http://localhost:{PORT}/api/")
    print("=" * 60)
    print("📋 Rotas disponíveis:")
    print(f"   🏠 Página inicial: http://localhost:{PORT}/")
    print(f"   🧪 Página de teste: http://localhost:{PORT}/test")
    print(f"   📊 API Info: http://localhost:{PORT}/api/info")
    print(f"   📁 Lista arquivos: http://localhost:{PORT}/api/files")
    print(f"   ⏰ Hora atual: http://localhost:{PORT}/api/time")
    print("=" * 60)
    print("🛑 Para parar: Ctrl+C")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=PORT)
