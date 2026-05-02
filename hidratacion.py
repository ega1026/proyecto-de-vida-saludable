# ============================================
# PROYECTO VIDA SALUDABLE - Módulo de Hidratación
# hidratacion.py
# ============================================

# --- FUNCIÓN: Registro de hidratación diaria ---
def registrar_hidratacion():
    META_VASOS = 8  # La meta son 8 vasos (equivale a 2 litros de agua)

    print("\n--- REGISTRO DE HIDRATACIÓN ---")
    vasos_tomados = int(input("¿Cuántos vasos de agua has tomado hoy? "))

    # Calculamos cuántos vasos le faltan para cumplir la meta
    vasos_faltantes = META_VASOS - vasos_tomados

    print()
    if vasos_faltantes <= 0:
        # El estudiante ya cumplió o superó la meta diaria
        print("  ¡Felicitaciones! Cumpliste tu meta de hidratación.")
        print("  Una mente hidratada rinde mejor académicamente.")
    else:
        # Le indicamos exactamente cuánto le falta para llegar a los 2 litros
        litros_faltantes = round(vasos_faltantes * 0.25, 2)
        print(f"  Llevas {vasos_tomados} de {META_VASOS} vasos.")
        print(f"  Te faltan {vasos_faltantes} vasos ({litros_faltantes} litros).")
        print("  ¡Recuerda: hidratarse mejora tu concentración!")
    print()