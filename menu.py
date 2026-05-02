# ============================================
# PROYECTO VIDA SALUDABLE - Módulo de Menú
# menu.py
# ============================================

# --- FUNCIÓN 1: Bienvenida al sistema ---
def mostrar_bienvenida():
    print("=" * 50)
    print("  PROYECTO VIDA SALUDABLE")
    print("  Comunidad Educativa - Bienestar Integral")
    print("=" * 50)
    print("Combatimos el sedentarismo para alcanzar")
    print("el éxito integral de nuestra comunidad.")
    print()

# --- FUNCIÓN 2: Menú principal ---
def mostrar_menu():
    print("  ¿Qué deseas hacer?")
    print("  1. Ver Perfil")
    print("  2. Registro de Hidratación")
    print("  3. Salir")
    opcion = input("  Elige una opción (1-3): ")
    return opcion