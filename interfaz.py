from consulta import Consulta


class InterfazUsuario:
    """Clase encargada de mostrar menús y capturar entradas."""

    @staticmethod
    def mostrar_menu():
        print("\n========================================")
        print("      SISTEMA DE CONTACTO UPN          ")
        print("========================================")
        print("1. Registrar consulta")
        print("2. Buscar consulta")
        print("3. Modificar consulta")
        print("4. Eliminar consulta")
        print("5. Mostrar todas las consultas")
        print("6. Derivar / Actualizar estado")
        print("7. Ordenar consultas por área (Burbuja)")
        print("8. Salir")
        print("========================================")

    @staticmethod
    def imprimir_ticket(consulta: Consulta):
        print("\n========================================")
        print("          TICKET DE ATENCIÓN            ")
        print("========================================")
        print(f"Código/DNI:       {consulta.codigo}")
        print(f"Motivo:           {consulta.motivo}")
        print(f"Sede / Área:      {consulta.area}")
        print(f"Horario asignado: {consulta.horario}")
        print(f"Estado:           {consulta.estado}")
        print("========================================")
        print("Regrese en el horario indicado para ser atendido sin hacer filas.")

    @staticmethod
    def solicitar_area() -> str:
        print("\nSELECCIONE LA SEDE / ÁREA")
        print("1. Los Olivos")
        print("2. Breña")
        print("3. Comas")
        opcion = input("Ingrese una opción: ").strip()
        areas = {"1": "Los Olivos", "2": "Breña", "3": "Comas"}
        return areas.get(opcion)

    @staticmethod
    def solicitar_motivo() -> str:
        print("\nMOTIVO DE CONSULTA")
        print("1. Trámites Académicos / Matrícula")
        print("2. Consultas Financieras / Pensiones")
        print("3. Orientación y Soporte Técnico")
        opcion = input("Ingrese una opción: ").strip()
        motivos = {
            "1": "Trámites Académicos / Matrícula",
            "2": "Consultas Financieras / Pensiones",
            "3": "Orientación y Soporte Técnico"
        }
        return motivos.get(opcion)

    @staticmethod
    def solicitar_horario() -> str:
        print("\nHORARIOS DISPONIBLES")
        print("1. 08:30 AM")
        print("2. 10:45 AM")
        print("3. 02:15 PM")
        print("4. 04:45 PM")
        opcion = input("Seleccione un horario: ").strip()
        horarios = {"1": "08:30 AM", "2": "10:45 AM", "3": "02:15 PM", "4": "04:45 PM"}
        return horarios.get(opcion)

    @staticmethod
    def mostrar_lista(consultas: list, cantidad: int):
        print("\n--- CONSULTAS REGISTRADAS ---")
        if cantidad == 0:
            print("No hay consultas registradas.")
            return
        for i in range(cantidad):
            print(consultas[i].obtener_resumen())