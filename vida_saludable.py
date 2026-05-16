# ============================================
# PROYECTO VIDA SALUDABLE - Archivo Principal
# vida_saludable.py
# ============================================
import sqlite3

# Importamos los módulos de nuestro proyecto
from perfil      import capturar_perfil, ver_perfil
from hidratacion import registrar_hidratacion
from menu        import mostrar_bienvenida, mostrar_menu

# --- FUNCIÓN INTERNA: Crear las tablas si no existen ---
def verificar_base_de_datos():
    conexion = sqlite3.connect('vida_saludable.db')
    cursor = conexion.cursor()
    
    # Creamos la tabla de perfiles si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS perfiles (
            id_perfil INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            grado TEXT NOT NULL,
            categoria TEXT NOT NULL,
            actividad_recomendada TEXT NOT NULL
        )
    ''')
    
    # Creamos la tabla de hidratación con el campo 'fecha' exacto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hidratacion (
            id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
            vasos_tomados INTEGER NOT NULL,
            fecha TEXT UNIQUE NOT NULL
        )
    ''')
    
    conexion.commit()
    conexion.close()

# ============================================================
# PROGRAMA PRINCIPAL - Aquí arranca todo el sistema
# ============================================================

# 1. Aseguramos que la base de datos esté creada antes de iniciar
verificar_base_de_datos()

mostrar_bienvenida()

# Primero capturamos el perfil antes de entrar al menú
perfil_usuario = capturar_perfil()

# El ciclo while mantiene el menú activo hasta que el usuario elija Salir
ejecutando = True
while ejecutando:
    opcion = mostrar_menu()

    if opcion == "1":
        ver_perfil(perfil_usuario)

    elif opcion == "2":
        registrar_hidratacion()

    elif opcion == "3":
        print()
        print("  ¡Hasta pronto! Recuerda que un cuerpo")
        print("  activo e hidratado potencia tu bienestar")
        print("  y tu rendimiento en el colegio.")
        print("  — Proyecto Vida Saludable")
        ejecutando = False  # Cambiamos la variable para detener el ciclo

    else:
        print("  Opción no válida. Intenta con 1, 2 o 3.\n")