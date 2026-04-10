# ================================
# SIMULADOR DE BASE DISTRIBUIDA
# MOVEFAST (TIPO UBER)
# ================================

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.activo = True

    def caer(self):
        self.activo = False

    def levantar(self):
        self.activo = True

    def estado(self):
        return "ACTIVO" if self.activo else "CAIDO"


class Region:
    def __init__(self, nombre):
        self.nombre = nombre
        self.primario = Nodo(f"{nombre}-Primario")
        self.replica = Nodo(f"{nombre}-Replica")
        self.particion = False  # Simula fallo de red

    def activar_particion(self):
        self.particion = True

    def desactivar_particion(self):
        self.particion = False

    def estado_region(self):
        return {
            "region": self.nombre,
            "primario": self.primario.estado(),
            "replica": self.replica.estado(),
            "particion": "SI" if self.particion else "NO"
        }

    def procesar_solicitud(self):
        # Simulación CAP
        if self.particion:
            return f"[{self.nombre}] ERROR: Partición de red (CAP activo)"

        if self.primario.activo:
            return f"[{self.nombre}] OK → Atendido por PRIMARIO"
        elif self.replica.activo:
            return f"[{self.nombre}] FAILOVER → Atendido por RÉPLICA"
        else:
            return f"[{self.nombre}] ERROR TOTAL → Sin nodos disponibles"


# ================================
# FUNCIONES DEL SISTEMA
# ================================

def mostrar_estados(regiones):
    print("\n==============================")
    print("   ESTADO DEL SISTEMA")
    print("==============================")

    for r in regiones:
        e = r.estado_region()
        print(f"\nREGIÓN: {e['region']}")
        print(f"  Primario : {e['primario']}")
        print(f"  Réplica  : {e['replica']}")
        print(f"  Partición: {e['particion']}")

    print("\n==============================\n")


def menu():
    guatemala = Region("Guatemala")
    mexico = Region("Mexico")
    usa = Region("USA")

    regiones = [guatemala, mexico, usa]

    while True:
        mostrar_estados(regiones)

        print("1. Solicitud Guatemala")
        print("2. Solicitud México")
        print("3. Solicitud USA")

        print("\n--- FALLAS ---")
        print("4. Caer Primario Guatemala")
        print("5. Caer Primario México")
        print("6. Caer Primario USA")

        print("7. Levantar Primario Guatemala")
        print("8. Levantar Primario México")
        print("9. Levantar Primario USA")

        print("\n--- RÉPLICAS ---")
        print("10. Caer Réplica Guatemala")
        print("11. Caer Réplica México")
        print("12. Caer Réplica USA")

        print("\n--- RED (CAP) ---")
        print("13. Activar Partición Guatemala")
        print("14. Desactivar Partición Guatemala")

        print("\n0. Salir")

        opcion = input("\nSeleccione opción: ")

        # SOLICITUDES
        if opcion == "1":
            print(guatemala.procesar_solicitud())
        elif opcion == "2":
            print(mexico.procesar_solicitud())
        elif opcion == "3":
            print(usa.procesar_solicitud())

        # FALLAS PRIMARIO
        elif opcion == "4":
            guatemala.primario.caer()
            print("Primario Guatemala caído")
        elif opcion == "5":
            mexico.primario.caer()
            print("Primario México caído")
        elif opcion == "6":
            usa.primario.caer()
            print("Primario USA caído")

        # LEVANTAR PRIMARIO
        elif opcion == "7":
            guatemala.primario.levantar()
        elif opcion == "8":
            mexico.primario.levantar()
        elif opcion == "9":
            usa.primario.levantar()

        # FALLAS RÉPLICA
        elif opcion == "10":
            guatemala.replica.caer()
        elif opcion == "11":
            mexico.replica.caer()
        elif opcion == "12":
            usa.replica.caer()

        # PARTICIÓN (CAP)
        elif opcion == "13":
            guatemala.activar_particion()
            print("Partición de red ACTIVADA en Guatemala")
        elif opcion == "14":
            guatemala.desactivar_particion()
            print("Partición de red DESACTIVADA en Guatemala")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


# ================================
# EJECUCIÓN
# ================================

if __name__ == "__main__":
    menu()
    
