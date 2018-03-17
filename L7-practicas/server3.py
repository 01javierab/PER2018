import http.server
import socketserver

# -- Puerto donde lanzar el servidor
PORT = 8000


# Clase con nuestro manejador. Es una clase derivada de BaseHTTPRequestHandler
# Esto significa que "hereda" todos los metodos de esta clase. Y los que
# nosotros consideremos los podemos reemplazar por los nuestros
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    # GET. Este metodo se invoca automaticamente cada vez que hay una
    # peticion GET por HTTP. El recurso que nos solicitan se encuentra
    # en self.path
    def do_GET(self):

        # La primera linea del mensaje de respuesta es el
        # status. Indicamos que OK
        self.send_response(200)

        # En las siguientes lineas de la respuesta colocamos las
        # cabeceras necesarias para que el cliente entienda el
        # contenido que le enviamos (que sera HTML)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if self.path == "/":
            filename = "green.html"
        else:
            if self.path == "/blue":
                filename = "blue.html"
            else:
                filename = "pink.html"

        print("File to send: {}".format(filename))

        with open(filename, "r") as f:
            content = f.read()

        # Este es el mensaje que enviamos al cliente: un texto y
        # el recurso solicitado
        #message = "Hello world! " + self.path

        # Enviar el mensaaje completo
        self.wfile.write(bytes(content, "utf8"))
        print("File served!")
        return


# ----------------------------------
# El servidor comienza a aqui
# ----------------------------------
# Establecemos como manejador nuestra propia clase
Handler = testHTTPRequestHandler


httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print("")
print("Server stopped!")













