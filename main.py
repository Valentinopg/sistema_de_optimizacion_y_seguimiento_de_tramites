from consulta import Consulta
from gestion import GestionConsultas
from interfaz import InterfazUsuario


def main():
    gestor = GestionConsultas(max_consultas=100)
    vista = InterfazUsuario()

    while True:
        vista.mostrar_menu()
        opcion = input("Ingrese una opción (1-8): ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR CONSULTA ---")
            codigo = input("Ingrese código de estudiante o DNI: ").strip()
            if len(codigo) < 8:
                print("[ERROR] Datos inválidos. Ingrese un código/DNI válido (mínimo 8 dígitos).")
                continue
            if gestor.buscar_consulta(codigo) is not None:
                print("[ERROR] Datos inválidos. Ingrese un código/DNI válido (mínimo 8 dígitos).")
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
            if gestor.registrar_consulta(nueva):
                print("[ÉXITO] Consulta registrada correctamente.")
                vista.imprimir_ticket(nueva)
            else:
                print("[ERROR] Se alcanzó el límite de 100 consultas.")

        elif opcion == "2":
            print("\n--- BUSCAR CONSULTA ---")
            codigo = input("Ingrese el código/DNI: ").strip()
            consulta = gestor.buscar_consulta(codigo)
            if consulta:
                vista.imprimir_ticket(consulta)
            else:
                print("[MENSAJE] Consulta no encontrada.")

        elif opcion == "3":
            print("\n--- MODIFICAR CONSULTA ---")
            codigo = input("Ingrese el código/DNI: ").strip()
            if gestor.buscar_consulta(codigo) is None:
                print("[MENSAJE] Consulta no encontrada.")
                continue

            nuevo_motivo = vista.solicitar_motivo()
            nueva_area = vista.solicitar_area()
            if nuevo_motivo and nueva_area:
                if gestor.modificar_consulta(codigo, nuevo_motivo, nueva_area):
                    print("[ÉXITO] Consulta modificada correctamente.")
            else:
                print("[ERROR] Datos no válidos. No se realizaron cambios.")

        elif opcion == "4":
            print("\n--- ELIMINAR CONSULTA ---")
            codigo = input("Ingrese el código/DNI: ").strip()
            if gestor.eliminar_consulta(codigo):
                print("[ÉXITO] Consulta eliminada correctamente.")
            else:
                print("[MENSAJE] Consulta no encontrada.")

        elif opcion == "5":
            vista.mostrar_lista(gestor.obtener_arreglo(), gestor.obtener_cantidad())

        elif opcion == "6":
            print("\n--- DERIVAR / ACTUALIZAR ESTADO ---")
            codigo = input("Ingrese el código/DNI: ").strip()
            if gestor.buscar_consulta(codigo) is None:
                print("[MENSAJE] Consulta no encontrada.")
                continue

            nueva_area = vista.solicitar_area()
            print("\nESTADOS DISPONIBLES: 1. Pendiente | 2. En proceso | 3. Atendida")
            op_est = input("Seleccione el estado: ").strip()
            estados = {"1": "Pendiente", "2": "En proceso", "3": "Atendida"}
            nuevo_estado = estados.get(op_est)

            if nueva_area and nuevo_estado:
                if gestor.derivar_consulta(codigo, nueva_area, nuevo_estado):
                    print("[ÉXITO] Seguimiento actualizado correctamente.")
            else:
                print("[ERROR] Sede o estado no válido.")

        elif opcion == "7":
            gestor.ordenar_consultas_burbuja()
            print("[ÉXITO] Consultas ordenadas por sede.")
            vista.mostrar_lista(gestor.obtener_arreglo(), gestor.obtener_cantidad())

        elif opcion == "8":
            print("Saliendo del sistema de Contacto UPN...")
            break
        else:
            print("[ERROR] Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
