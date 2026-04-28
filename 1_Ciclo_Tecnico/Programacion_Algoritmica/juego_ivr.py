import time
import random

def sistema_voz(mensaje):
    print(f"\n[SISTEMA]: {mensaje}")
    time.sleep(1.2)

def iniciar_mision():
    hp = 100
    enemigo_hp = 50
    print("\n" + "="*45)
    print("      🎮 IVR: OPERACIÓN BXZ-DRAGON 🐉")
    print("="*45)
    sistema_voz("Conexión establecida... Bienvenido Comandante Brian.")

    while hp > 0 and enemigo_hp > 0:
        print(f"\n❤️ Tu Vida: {hp} | 👾 Vida del Enemigo: {enemigo_hp}")
        print("-" * 35)
        print("1. Ataque Rápido (Dagas de Gusion)")
        print("2. Ataque Cargado (Habilidad Definitiva)")
        print("3. Reparación de Nanobots (Curar)")
        print("0. Salir del sistema")
        
        opcion = input("\n[MARQUE UNA OPCIÓN]: ")

        if opcion == "1":
            daño = random.randint(10, 18)
            enemigo_hp -= daño
            print(f"⚔️ ¡Impacto! Causaste {daño} de daño.")
        elif opcion == "2":
            if random.random() > 0.4:
                daño = random.randint(30, 45)
                enemigo_hp -= daño
                print(f"🔥 ¡CRÍTICO! Destrozaste al enemigo con {daño} de daño.")
            else:
                print("❌ ¡Fallaste! El enemigo esquivó tu ataque.")
        elif opcion == "3":
            cura = random.randint(15, 25)
            hp = min(100, hp + cura)
            print(f"🔧 Reparando... HP actual: {hp}")
        elif opcion == "0":
            print("Cerrando sesión del IVR...")
            break
        else:
            print("⚠️ Error: Opción no válida en el teclado.")

        if enemigo_hp > 0 and opcion in ["1", "2", "3"]:
            contra = random.randint(8, 18)
            hp -= contra
            print(f"💥 ¡Alerta! El enemigo te golpeó por {contra}.")

    if enemigo_hp <= 0:
        print("\n🏆 ¡VICTORIA! Has limpiado la zona, Comandante.")
    elif hp <= 0:
        print("\n💀 CONEXIÓN PERDIDA... El enemigo ha destruido tu base.")

if __name__ == "__main__":
    iniciar_mision()


