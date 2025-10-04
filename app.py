#!/usr/bin/env python3
"""
Servidor Flask com Supabase
Aplicação completa com banco de dados na nuvem
"""

from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import json
from datetime import datetime
import time
from config import Config
from supabase_service import SupabaseService
from models import create_tables

# Criar a aplicação Flask
app = Flask(__name__)
CORS(app)  # Permitir CORS para desenvolvimento

# Configurações
app.config['SECRET_KEY'] = Config.SECRET_KEY
PORT = 8000

# Inicializar Supabase
try:
    supabase_service = SupabaseService()
    print("✅ Supabase conectado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao conectar com Supabase: {e}")
    supabase_service = None

# Criar tabelas no banco
try:
    create_tables()
    print("✅ Tabelas criadas com sucesso!")
except Exception as e:
    print(f"❌ Erro ao criar tabelas: {e}")

@app.route('/')
def home():
    """Página inicial"""
    return render_template('index.html')

@app.route('/api/info')
def api_info():
    """API - Informações do servidor"""
    return jsonify({
        'servidor': 'Flask com Supabase',
        'versao': '2.0.0',
        'porta': PORT,
        'timestamp': datetime.now().isoformat(),
        'diretorio': os.getcwd(),
        'python_version': os.sys.version,
        'flask_version': '2.3.3',
        'supabase_connected': supabase_service is not None
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
        'supabase_connected': supabase_service is not None,
        'uptime': 'N/A',
        'memoria': 'N/A'
    })

# ===== APIs DO SUPABASE =====

@app.route('/api/users', methods=['GET'])
def get_users():
    """API - Buscar todos os usuários"""
    if not supabase_service:
        return jsonify({'error': 'Supabase não conectado'}), 500
    
    users = supabase_service.get_users()
    return jsonify({
        'users': users,
        'total': len(users)
    })

@app.route('/api/users', methods=['POST'])
def create_user():
    """API - Criar novo usuário"""
    if not supabase_service:
        return jsonify({'error': 'Supabase não conectado'}), 500
    
    data = request.get_json()
    if not data or 'email' not in data or 'name' not in data:
        return jsonify({'error': 'Email e nome são obrigatórios'}), 400
    
    user = supabase_service.create_user(data['email'], data['name'])
    if user:
        return jsonify({'message': 'Usuário criado com sucesso', 'user': user}), 201
    else:
        return jsonify({'error': 'Erro ao criar usuário'}), 500

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """API - Buscar usuário por ID"""
    if not supabase_service:
        return jsonify({'error': 'Supabase não conectado'}), 500
    
    user = supabase_service.get_user_by_id(user_id)
    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'error': 'Usuário não encontrado'}), 404

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """API - Atualizar usuário"""
    if not supabase_service:
        return jsonify({'error': 'Supabase não conectado'}), 500
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados são obrigatórios'}), 400
    
    user = supabase_service.update_user(user_id, data)
    if user:
        return jsonify({'message': 'Usuário atualizado com sucesso', 'user': user})
    else:
        return jsonify({'error': 'Erro ao atualizar usuário'}), 500

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """API - Deletar usuário"""
    if not supabase_service:
        return jsonify({'error': 'Supabase não conectado'}), 500
    
    success = supabase_service.delete_user(user_id)
    if success:
        return jsonify({'message': 'Usuário deletado com sucesso'})
    else:
        return jsonify({'error': 'Erro ao deletar usuário'}), 500

@app.route('/api/posts', methods=['GET'])
def get_posts():
    """API - Buscar todos os posts"""
    if not supabase_service:
        return jsonify({'error': 'Supabase não conectado'}), 500
    
    posts = supabase_service.get_posts()
    return jsonify({
        'posts': posts,
        'total': len(posts)
    })

@app.route('/api/posts', methods=['POST'])
def create_post():
    """API - Criar novo post"""
    if not supabase_service:
        return jsonify({'error': 'Supabase não conectado'}), 500
    
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data or 'author_id' not in data:
        return jsonify({'error': 'Título, conteúdo e author_id são obrigatórios'}), 400
    
    post = supabase_service.create_post(data['title'], data['content'], data['author_id'])
    if post:
        return jsonify({'message': 'Post criado com sucesso', 'post': post}), 201
    else:
        return jsonify({'error': 'Erro ao criar post'}), 500

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """API - Buscar post por ID"""
    if not supabase_service:
        return jsonify({'error': 'Supabase não conectado'}), 500
    
    post = supabase_service.get_post_by_id(post_id)
    if post:
        return jsonify({'post': post})
    else:
        return jsonify({'error': 'Post não encontrado'}), 404

@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """API - Atualizar post"""
    if not supabase_service:
        return jsonify({'error': 'Supabase não conectado'}), 500
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados são obrigatórios'}), 400
    
    post = supabase_service.update_post(post_id, data)
    if post:
        return jsonify({'message': 'Post atualizado com sucesso', 'post': post})
    else:
        return jsonify({'error': 'Erro ao atualizar post'}), 500

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """API - Deletar post"""
    if not supabase_service:
        return jsonify({'error': 'Supabase não conectado'}), 500
    
    success = supabase_service.delete_post(post_id)
    if success:
        return jsonify({'message': 'Post deletado com sucesso'})
    else:
        return jsonify({'error': 'Erro ao deletar post'}), 500

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
    print("🚀 SERVIDOR FLASK COM SUPABASE")
    print("=" * 60)
    print(f"📁 Diretório: {os.getcwd()}")
    print(f"🌐 URL: http://localhost:{PORT}")
    print(f"📊 API: http://localhost:{PORT}/api/")
    print("=" * 60)
    print("📋 Rotas disponíveis:")
    print(f"   🏠 Página inicial: http://localhost:{PORT}/")
    print(f"   🧪 Página de teste: http://localhost:{PORT}/test")
    print(f"   📊 API Info: http://localhost:{PORT}/api/info")
    print(f"   👥 Usuários: http://localhost:{PORT}/api/users")
    print(f"   📝 Posts: http://localhost:{PORT}/api/posts")
    print("=" * 60)
    print("🛑 Para parar: Ctrl+C")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=PORT)