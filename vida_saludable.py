import sqlite3
import urllib.parse
from http.server import SimpleHTTPRequestHandler, HTTPServer
from datetime import datetime

DATABASE = 'vida_saludable.db'

def obtener_conexion():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

class ServidorVidaSaludable(SimpleHTTPRequestHandler):
    def do_POST(self):
        # Capturamos si la página web envía datos a /registrar_perfil
        if self.path == '/registrar_perfil':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            datos = urllib.parse.parse_qs(post_data)

            # 1. Sacamos los datos del formulario
            nombre = datos.get('nombre', [''])[0]
            edad = int(datos.get('edad', [0])[0] or 0)
            grado = datos.get('grado', [''])[0]
            vasos = int(datos.get('vasos', [0])[0] or 0)
            fecha_hoy = datetime.now().strftime('%Y-%m-%d')

            # 2. Clasificación según la edad
            if edad <= 11:
                categoria = 'Infantil'
                actividad = 'Juegos activos y de flexibilidad'
            elif edad <= 14:
                categoria = 'Prejuvenil'
                actividad = 'Coordinación, juegos de equipo y velocidad'
            else:
                categoria = 'Juvenil'
                actividad = 'Resistencia cardiovascular y fuerza'

            # 3. Guardar directo en la Base de Datos SQLite
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            try:
                cursor.execute('''
                    INSERT OR REPLACE INTO perfiles (id_perfil, nombre, edad, grado, categoria, actividad_recomendada)
                    VALUES (1, ?, ?, ?, ?, ?)
                ''', (nombre, edad, grado, categoria, actividad))

                cursor.execute('''
                    INSERT OR REPLACE INTO hidratacion (vasos_tomados, fecha)
                    VALUES (?, ?)
                ''', (vasos, fecha_hoy))

                conexion.commit()
                print(f"¡Firme! Se guardó a {nombre} con {vasos} vasos de agua.")
            except Exception as e:
                print(f"Error en la base de datos: {e}")
            finally:
                conexion.close()

            # Redireccionamos de vuelta a la página para que se actualice
            self.send_response(303)
            self.send_header('Location', '/perfil.html')
            self.end_headers()
        else:
            super().do_POST()

# Ponemos a correr el servidor nativo en el puerto 5000
def run():
    print("Iniciando servidor nativo en http://127.0.0.1:5000 ...")
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, ServidorVidaSaludable)
    print("¡Servidor prendido firmito! Ya puedes abrir el navegador.")
    httpd.serve_forever()

if __name__ == '__main__':
    run()