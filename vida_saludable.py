# ============================================
# PROYECTO VIDA SALUDABLE - Archivo Principal
# vida_saludable.py
# ============================================

# Importamos los módulos de nuestro proyecto
from perfil      import capturar_perfil, ver_perfil
from hidratacion import registrar_hidratacion
from menu        import mostrar_bienvenida, mostrar_menu

# ============================================================
# PROGRAMA PRINCIPAL - Aquí arranca todo el sistema
# ============================================================

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
        # Mensaje de despedida enfocado en el bienestar corporal
        print()
        print("  ¡Hasta pronto! Recuerda que un cuerpo")
        print("  activo e hidratado potencia tu bienestar")
        print("  y tu rendimiento en el colegio.")
        print("  — Proyecto Vida Saludable")
        ejecutando = False  # Cambiamos la variable para detener el ciclo

    else:
        print("  Opción no válida. Intenta con 1, 2 o 3.\n")