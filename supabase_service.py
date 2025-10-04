from supabase import create_client, Client
from config import Config
import json

class SupabaseService:
    def __init__(self):
        self.url = Config.SUPABASE_URL
        self.key = Config.SUPABASE_KEY
        self.supabase: Client = create_client(self.url, self.key)
    
    def get_users(self):
        """Buscar todos os usuários"""
        try:
            response = self.supabase.table('users').select('*').execute()
            return response.data
        except Exception as e:
            print(f"Erro ao buscar usuários: {e}")
            return []
    
    def create_user(self, email, name):
        """Criar novo usuário"""
        try:
            response = self.supabase.table('users').insert({
                'email': email,
                'name': name
            }).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            return None
    
    def get_user_by_id(self, user_id):
        """Buscar usuário por ID"""
        try:
            response = self.supabase.table('users').select('*').eq('id', user_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
    
    def update_user(self, user_id, data):
        """Atualizar usuário"""
        try:
            response = self.supabase.table('users').update(data).eq('id', user_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            return None
    
    def delete_user(self, user_id):
        """Deletar usuário"""
        try:
            response = self.supabase.table('users').delete().eq('id', user_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            return False
    
    def get_posts(self):
        """Buscar todos os posts"""
        try:
            response = self.supabase.table('posts').select('*').execute()
            return response.data
        except Exception as e:
            print(f"Erro ao buscar posts: {e}")
            return []
    
    def create_post(self, title, content, author_id):
        """Criar novo post"""
        try:
            response = self.supabase.table('posts').insert({
                'title': title,
                'content': content,
                'author_id': author_id
            }).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao criar post: {e}")
            return None
    
    def get_post_by_id(self, post_id):
        """Buscar post por ID"""
        try:
            response = self.supabase.table('posts').select('*').eq('id', post_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao buscar post: {e}")
            return None
    
    def update_post(self, post_id, data):
        """Atualizar post"""
        try:
            response = self.supabase.table('posts').update(data).eq('id', post_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao atualizar post: {e}")
            return None
    
    def delete_post(self, post_id):
        """Deletar post"""
        try:
            response = self.supabase.table('posts').delete().eq('id', post_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao deletar post: {e}")
            return False
