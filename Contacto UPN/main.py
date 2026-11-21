from consulta import Consulta
from gestion import GestionConsultas
from interfaz import InterfazUsuario

def main():

    gestor = GestionConsultas()
    vista = InterfazUsuario()   
    gestor.cargar_desde_txt()

    while True:
        vista.mostrar_menu()
        opcion = input("Ingrese una opción (1-10): ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR CONSULTA ---")

            
            while True:
                codigo = vista.solicitar_codigo()

                if gestor.buscar_consulta(codigo) is None:
                    break

                print("[ERROR] El código/DNI ya se encuentra registrado.")

            area = vista.solicitar_area()
            motivo = vista.solicitar_motivo()
            horario = vista.solicitar_horario()

            
            nueva_consulta = Consulta(codigo, motivo, area, horario)

            if gestor.registrar_consulta(nueva_consulta):
                gestor.guardar_en_txt()
                print("[ÉXITO] Consulta registrada correctamente en la lista dinámica.")
                vista.imprimir_ticket(nueva_consulta)
            else:
                print("[ERROR] No se pudo registrar la consulta.")

        elif opcion == "2":
            print("\n--- BUSCAR CONSULTA ---")
            codigo = vista.solicitar_codigo()
            consulta = gestor.buscar_consulta(codigo)

            if consulta is not None:
                vista.imprimir_ticket(consulta)
            else:
                print("[MENSAJE] Consulta no encontrada.")

        elif opcion == "3":
            print("\n--- MODIFICAR CONSULTA ---")
            codigo = vista.solicitar_codigo()
            consulta = gestor.buscar_consulta(codigo)

            if consulta is not None:
                nuevo_motivo = vista.solicitar_motivo()
                nueva_area = vista.solicitar_area()

                if gestor.modificar_consulta(codigo, nuevo_motivo, nueva_area):
                    gestor.guardar_en_txt()
                    print("[ÉXITO] Consulta modificada correctamente.")
            else:
                print("[MENSAJE] Consulta no encontrada.")

        elif opcion == "4":
            print("\n--- ELIMINAR CONSULTA ---")
            codigo = vista.solicitar_codigo()

            if gestor.eliminar_consulta(codigo):
                gestor.guardar_en_txt()
                print("[ÉXITO] Consulta eliminada correctamente de la lista dinámica.")
            else:
                print("[MENSAJE] Consulta no encontrada.")

        elif opcion == "5":
            vista.mostrar_lista(gestor.obtener_arreglo(), gestor.obtener_cantidad())

        elif opcion == "6":
            print("\n--- DERIVAR / ACTUALIZAR ESTADO ---")
            codigo = vista.solicitar_codigo()
            consulta = gestor.buscar_consulta(codigo)

            if consulta is not None:
                nueva_area = vista.solicitar_area()
                nuevo_estado = vista.solicitar_estado()

                if gestor.derivar_consulta(codigo, nueva_area, nuevo_estado):
                    gestor.guardar_en_txt()
                    print("[ÉXITO] Seguimiento actualizado correctamente.")
            else:
                print("[MENSAJE] Consulta no encontrada.")

        elif opcion == "7":
            gestor.ordenar_consultas_burbuja()
            gestor.guardar_en_txt()
            print("[ÉXITO] Consultas ordenadas por sede (Burbuja).")
            vista.mostrar_lista(gestor.obtener_arreglo(), gestor.obtener_cantidad())

        
        elif opcion == "8":
            print("\n--- ARREGLOS PARALELOS ---")
            gestor.mostrar_arreglos_paralelos()

        elif opcion == "9":
            print("\n--- CONTEO RECURSIVO ---")

            cantidad = gestor.contar_consultas_recursivo()

            print("Cantidad de consultas registradas:", cantidad)

        elif opcion == "10":
            print("Saliendo del sistema de Contacto UPN...")
            break

        else:
            print("[ERROR] Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
