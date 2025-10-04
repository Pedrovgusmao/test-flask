import http.server
import socketserver

PORT = 800

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"🚀 Servidor rodando em http://localhost:{PORT}")
    print(f"🛑 Para parar: Ctrl+C")
    httpd.serve_forever()