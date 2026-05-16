import sqlite3

def inicializar_base_de_datos():
    # Se conecta (y crea el archivo si no existe)
    conexion = sqlite3.connect('vida_saludable.db')
    cursor = conexion.cursor()

    # Activar el soporte para llaves foráneas en SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Tabla de Usuarios (Para el login.html)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 2. Tabla de Perfil (Para perfil.py y perfil.html - peso, altura, IMC)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS perfil_usuario (
            id_perfil INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            peso REAL NOT NULL,
            altura REAL NOT NULL,
            imc REAL,
            fecha_actualizacion TEXT NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
        )
    ''')

    # 3. Tabla de Hidratación (Para hidratacion.py - control de agua diaria)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hidratacion (
            id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            cantidad_ml INTEGER NOT NULL, -- Ejemplo: 500 para medio litro
            fecha_registro TEXT NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
        )
    ''')

    conexion.commit()
    conexion.close()
    print("¡Base de datos armada con éxito con sus tablas de Perfil e Hidratación!")

if __name__ == '__main__':
    inicializar_base_de_datos()