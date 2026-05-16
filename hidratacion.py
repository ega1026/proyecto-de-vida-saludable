# ============================================
# PROYECTO VIDA SALUDABLE - Módulo de Hidratación
# hidratacion.py
# ============================================
import sqlite3
from datetime import datetime

# --- FUNCIÓN: Registro de hidratación diaria ---
def registrar_hidratacion():
    META_VASOS = 8  # La meta son 8 vasos (equivale a 2 litros de agua)
    fecha_hoy = datetime.now().strftime('%Y-%m-%d')

    print("\n--- REGISTRO DE HIDRATACIÓN ---")
    vasos_nuevos = int(input("¿Cuántos vasos de agua te tomaste justo ahora? "))

    conexion = sqlite3.connect('vida_saludable.db')
    cursor = conexion.cursor()

    try:
        # Buscamos si ya tomó agua hoy
        cursor.execute('SELECT vasos_tomados FROM hidratacion WHERE fecha = ?', (fecha_hoy,))
        resultado = cursor.fetchone()

        if resultado:
            # Si ya existe, sumamos los vasos nuevos a los que ya llevaba
            vasos_totales = resultado[0] + vasos_nuevos
            cursor.execute('UPDATE hidratacion SET vasos_tomados = ? WHERE fecha = ?', (vasos_totales, fecha_hoy))
        else:
            # Si es el primer registro del día, lo insertamos
            vasos_totales = vasos_nuevos
            cursor.execute('INSERT INTO hidratacion (vasos_tomados, fecha) VALUES (?, ?)', (vasos_totales, fecha_hoy))
        
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al registrar hidratación: {e}")
        vasos_totales = vasos_nuevos
    finally:
        conexion.close()

    # Calculamos cuántos vasos le faltan para cumplir la meta
    vasos_faltantes = META_VASOS - vasos_totales

    print()
    if vasos_faltantes <= 0:
        print("  ¡Felicitaciones! Cumpliste tu meta de hidratación diaria.")
        print(f"  Llevas un total de {vasos_totales} vasos tomados hoy. ¡Excelente!")
        print("  Una mente hidratada rinde mejor académicamente.")
    else:
        litros_faltantes = round(vasos_faltantes * 0.25, 2)
        print(f"  Hoy llevas acumulados {vasos_totales} de {META_VASOS} vasos.")
        print(f"  Te faltan {vasos_faltantes} vasos ({litros_faltantes} litros) para la meta.")
        print("  ¡Recuerda: hidratarse mejora tu concentración!")
    print()