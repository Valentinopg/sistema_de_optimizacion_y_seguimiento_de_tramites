from consulta import Consulta
from gestion import GestionConsultas
from interfaz import InterfazUsuario

gestor_global = GestionConsultas()

def main():
    global gestor_global

    vista = InterfazUsuario()

    while True:
        vista.mostrar_menu()

        opcion = input("Ingrese una opción (1-8): ").strip()

        # OPCIÓN 1: REGISTRAR CONSULTA
        if opcion == "1":
            print("\n--- REGISTRAR CONSULTA ---")

            codigo = input("Ingrese código de estudiante o DNI: ").strip()

            if len(codigo) < 8:
                print("[ERROR] Datos inválidos. Ingrese un código/DNI válido (mínimo 8 dígitos).")
                continue

            if gestor_global.buscar_consulta(codigo) is not None:
                print("[ERROR] El código/DNI ya se encuentra registrado.")
                continue

            area = vista.solicitar_area()

            if not area:
                print("[ERROR] Opción de sede no válida.")
                continue

            motivo = vista.solicitar_motivo()

            if not motivo:
                print("[ERROR] Opción de motivo no válida.")
                continue

            horario = vista.solicitar_horario()

            if not horario:
                print("[ERROR] Horario no válido.")
                continue

            nueva = Consulta(codigo, motivo, area, horario)

            if gestor_global.registrar_consulta(nueva):
                print("[ÉXITO] Consulta registrada correctamente en la lista dinámica.")
                vista.imprimir_ticket(nueva)
            else:
                print("[ERROR] No se pudo registrar la consulta.")

        # OPCIÓN 2: BUSCAR CONSULTA
        elif opcion == "2":
            print("\n--- BUSCAR CONSULTA ---")

            codigo = input("Ingrese el código/DNI: ").strip()

            consulta = gestor_global.buscar_consulta(codigo)

            if consulta:
                vista.imprimir_ticket(consulta)
            else:
                print("[MENSAJE] Consulta no encontrada.")

        # OPCIÓN 3: MODIFICAR CONSULTA
        elif opcion == "3":
            print("\n--- MODIFICAR CONSULTA ---")

            codigo = input("Ingrese el código/DNI: ").strip()

            if gestor_global.buscar_consulta(codigo) is None:
                print("[MENSAJE] Consulta no encontrada.")
                continue

            nuevo_motivo = vista.solicitar_motivo()
            nueva_area = vista.solicitar_area()

            if nuevo_motivo and nueva_area:
                if gestor_global.modificar_consulta(
                    codigo, nuevo_motivo, nueva_area
                ):
                    print("[ÉXITO] Consulta modificada correctamente.")
                else:
                    print("[ERROR] Datos no válidos. No se realizaron cambios.")

        # OPCIÓN 4: ELIMINAR CONSULTA
        elif opcion == "4":
            print("\n--- ELIMINAR CONSULTA ---")

            codigo = input("Ingrese el código/DNI: ").strip()

            if gestor_global.eliminar_consulta(codigo):
                print("[ÉXITO] Consulta eliminada correctamente de la lista dinámica.")
            else:
                print("[MENSAJE] Consulta no encontrada.")

        # OPCIÓN 5: MOSTRAR TODAS LAS CONSULTAS
        elif opcion == "5":
            vista.mostrar_lista(
                gestor_global.obtener_arreglo(),
                gestor_global.obtener_cantidad()
            )

        # OPCIÓN 6: DERIVAR / ACTUALIZAR ESTADO
        elif opcion == "6":
            print("\n--- DERIVAR / ACTUALIZAR ESTADO ---")

            codigo = input("Ingrese el código/DNI: ").strip()

            if gestor_global.buscar_consulta(codigo) is None:
                print("[MENSAJE] Consulta no encontrada.")
                continue

            nueva_area = vista.solicitar_area()

            print("\nESTADOS DISPONIBLES:")
            print("1. Pendiente")
            print("2. En proceso")
            print("3. Atendida")

            op_est = input("Seleccione el estado: ").strip()

            estados = {
                "1": "Pendiente",
                "2": "En proceso",
                "3": "Atendida"
            }

            nuevo_estado = estados.get(op_est)

            if nueva_area and nuevo_estado:
                if gestor_global.derivar_consulta(
                    codigo, nueva_area, nuevo_estado
                ):
                    print("[ÉXITO] Seguimiento actualizado correctamente.")
                else:
                    print("[ERROR] Sede o estado no válido.")

        # OPCIÓN 7: ORDENAR POR BURBUJA
        elif opcion == "7":
            gestor_global.ordenar_consultas_burbuja()

            print("[ÉXITO] Consultas ordenadas por sede (Burbuja).")

            vista.mostrar_lista(
                gestor_global.obtener_arreglo(),
                gestor_global.obtener_cantidad()
            )

        # OPCIÓN 8: SALIR
        elif opcion == "8":
            print("Saliendo del sistema de Contacto UPN...")
            break

        else:
            print("[ERROR] Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()