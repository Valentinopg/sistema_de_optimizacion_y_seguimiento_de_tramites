from consulta import Consulta

class InterfazUsuario:
    
    def mostrar_menu(self):
        print("\n========================================")
        print("        SISTEMA DE CONTACTO UPN         ")
        print("========================================")
        print("1. Registrar consulta")
        print("2. Buscar consulta")
        print("3. Modificar consulta")
        print("4. Eliminar consulta")
        print("5. Mostrar todas las consultas")
        print("6. Derivar / Actualizar estado")
        print("7. Ordenar consultas por área (Burbuja)")
        print("8. Mostrar datos en arreglos paralelos")
        print("9. Contar consultas mediante recursividad")
        print("10. Salir")
        print("========================================")


    def validar_codigo(self, codigo):
        codigo = codigo.strip().upper()

        
        if len(codigo) == 8:
            valido = True

            for digito in codigo:
                if digito not in "0123456789":
                    valido = False

            if valido:
                return True

        
        if len(codigo) == 9 and codigo[0] == "N":
            valido = True

            for digito in codigo[1:]:
                if digito not in "0123456789":
                    valido = False

            if valido:
                return True

        return False

    
    def solicitar_codigo(self):
        while True:
            codigo = input("Ingrese código de estudiante o DNI: ").strip().upper()

            if self.validar_codigo(codigo):
                return codigo

            print("[ERROR] Datos inválidos. Ingrese un código/DNI válido .")

    
    def solicitar_area(self):
        while True:
            print("\nSELECCIONE LA SEDE / ÁREA")
            print("1. Los Olivos")
            print("2. Breña")
            print("3. Comas")
            opcion = input("Ingrese una opción: ").strip()

            if opcion == "1":
                return "Los Olivos"
            elif opcion == "2":
                return "Breña"
            elif opcion == "3":
                return "Comas"
            else:
                print("[ERROR] Opción de sede no válida.")

    
    def solicitar_motivo(self):
        while True:
            print("\nMOTIVO DE CONSULTA")
            print("1. Trámites Académicos / Matrícula")
            print("2. Consultas Financieras / Pensiones")
            print("3. Orientación y Soporte Técnico")
            opcion = input("Ingrese una opción: ").strip()

            if opcion == "1":
                return "Trámites Académicos / Matrícula"
            elif opcion == "2":
                return "Consultas Financieras / Pensiones"
            elif opcion == "3":
                return "Orientación y Soporte Técnico"
            else:
                print("[ERROR] Opción de motivo no válida.")

    
    def solicitar_horario(self):
        while True:
            print("\nHORARIOS DISPONIBLES")
            print("1. 08:30 AM")
            print("2. 10:45 AM")
            print("3. 02:15 PM")
            print("4. 04:45 PM")
            opcion = input("Seleccione un horario: ").strip()

            if opcion == "1":
                return "08:30 AM"
            elif opcion == "2":
                return "10:45 AM"
            elif opcion == "3":
                return "02:15 PM"
            elif opcion == "4":
                return "04:45 PM"
            else:
                print("[ERROR] Horario no válido.")

    
    def solicitar_estado(self):
        while True:
            print("\nESTADOS DISPONIBLES")
            print("1. Pendiente")
            print("2. En proceso")
            print("3. Atendida")
            opcion = input("Seleccione el estado: ").strip()

            if opcion == "1":
                return "Pendiente"
            elif opcion == "2":
                return "En proceso"
            elif opcion == "3":
                return "Atendida"
            else:
                print("[ERROR] Estado no válido.")

    
    def imprimir_ticket(self, consulta):
        print("\n========================================")
        print("           TICKET DE ATENCIÓN           ")
        print("========================================")
        print("Código/DNI:      " + consulta.codigo)
        print("Motivo:          " + consulta.motivo)
        print("Sede / Área:     " + consulta.area)
        print("Horario asignado:" + consulta.horario)
        print("Estado:          " + consulta.estado)
        print("========================================")
        print("Regrese en el horario indicado para ser atendido sin hacer filas.")

    
    def mostrar_lista(self, consultas, cantidad):
        print("\n--- CONSULTAS REGISTRADAS ---")

        if cantidad == 0:
            print("No hay consultas registradas.")
        else:
            for i in range(cantidad):
                print(consultas[i].obtener_resumen())
