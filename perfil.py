# ============================================
# PROYECTO VIDA SALUDABLE - Módulo de Perfil
# perfil.py
# ============================================

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

    # Guardamos todos los datos en un diccionario para usarlos después
    perfil = {
        "nombre"   : nombre,
        "edad"     : edad,
        "grado"    : grado,
        "categoria": categoria,
        "actividad": actividad
    }
    print(f"\n¡Perfil creado exitosamente, {nombre}!\n")
    return perfil

# --- FUNCIÓN 2: Ver perfil con recomendación de la Biblioteca de Movimientos ---
def ver_perfil(perfil):
    print("\n--- MI PERFIL ---")
    print(f"  Nombre   : {perfil['nombre']}")
    print(f"  Edad     : {perfil['edad']} años")
    print(f"  Grado    : {perfil['grado']}")
    print(f"  Categoría: {perfil['categoria']}")
    print()

    # Mostramos la recomendación según la Biblioteca de Movimientos del proyecto
    print("  RECOMENDACIÓN - Biblioteca de Movimientos:")
    if perfil["categoria"] == "Infantil":
        print("  → Categoría Infantil: Practica juegos motrices.")
        print("    Mejoran tu coordinación y concentración en clases.")
    else:
        print("  → Categoría Juvenil: Enfócate en resistencia y fuerza.")
        print("    Aumentan tu energía y rendimiento académico.")
    print()