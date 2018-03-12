import http.server
import socketserver

# -- Puerto donde lanzar el servidor
PORT = 8001

# -- Establecer como manejador el propio de la biblioteca http
# -- Es el objeto que se invocará cuando haya peticiones web
Handler = http.server.SimpleHTTPRequestHandler

# Bucle principal. Esperar conexiones web y atenderlas
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)

    # Entrar en el bucle principal
    # Las peticiones se atienden desde el manejador
httpd.serve_forever()
