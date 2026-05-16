# ============================================
# PROYECTO VIDA SALUDABLE - Módulo de Perfil
# perfil.py
# ============================================
import sqlite3

# --- FUNCIÓN 1: Captura de datos del perfil ---
def capturar_perfil():
    print("--- REGISTRO DE PERFIL ---")
    nombre = input("Nombre: ")
    edad   = int(input("Edad: "))
    grado  = input("Grado: ")

    # Clasificamos la categoría según la edad del estudiante
    if edad < 12:
        categoria = "Infantil"
        actividad = "Juegos motrices"
    else:
        categoria = "Juvenil"
        actividad = "Resistencia y fuerza"

    # GUARDAR EN BASE DE DATOS SQLITE
    conexion = sqlite3.connect('vida_saludable.db')
    cursor = conexion.cursor()
    try:
        # Insertamos o actualizamos el perfil de prueba (id_usuario = 1)
        cursor.execute('''
            INSERT OR REPLACE INTO perfiles (id_perfil, nombre, edad, grado, categoria, actividad_recomendada)
            VALUES (1, ?, ?, ?, ?, ?)
        ''', (nombre, edad, grado, categoria, actividad))
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al guardar perfil: {e}")
    finally:
        conexion.close()

    perfil = {
        "nombre"   : nombre,
        "edad"     : edad,
        "grado"    : grado,
        "categoria": categoria,
        "actividad": actividad
    }
    print(f"\n¡Perfil creado exitosamente en la Base de Datos, {nombre}!\n")
    return perfil

# --- FUNCIÓN 2: Ver perfil con recomendación de la Biblioteca de Movimientos ---
def ver_perfil(perfil_temporal=None):
    print("\n--- MI PERFIL (Desde Base de Datos) ---")
    
    # Buscamos los datos reales guardados en la base de datos
    conexion = sqlite3.connect('vida_saludable.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT nombre, edad, grado, categoria, actividad_recomendada FROM perfiles WHERE id_perfil = 1')
    perfil_bd = cursor.fetchone()
    conexion.close()

    if perfil_bd:
        nombre, edad, grado, categoria, actividad = perfil_bd
    elif perfil_temporal:
        # Por si la base de datos falla, usamos el temporal
        nombre = perfil_temporal["nombre"]
        edad = perfil_temporal["edad"]
        grado = perfil_temporal["grado"]
        categoria = perfil_temporal["categoria"]
        actividad = perfil_temporal["actividad"]
    else:
        print("  Aún no hay ningún perfil registrado.\n")
        return

    print(f"  Nombre   : {nombre}")
    print(f"  Edad     : {edad} años")
    print(f"  Grado    : {grado}")
    print(f"  Categoría: {categoria}")
    print()

    # Mostramos la recomendación según la Biblioteca de Movimientos del proyecto
    print("  RECOMENDACIÓN - Biblioteca de Movimientos:")
    if categoria == "Infantil":
        print(f"  → Categoría Infantil: Practica {actividad}.")
        print("    Mejoran tu coordinación y concentración en clases.")
    else:
        print(f"  → Categoría Juvenil: Enfócate en {actividad}.")
        print("    Aumentan tu energía y rendimiento académico.")
    print()