from consulta import Consulta

class GestionConsultas:
    
    def __init__(self):
        self.consultas = []

    
    def buscar_indice(self, codigo):
        for i in range(len(self.consultas)):
            if self.consultas[i].codigo == codigo:
                return i
        return -1


    def buscar_consulta(self, codigo):
        indice = self.buscar_indice(codigo)

        if indice != -1:
            return self.consultas[indice]

        return None

    
    def registrar_consulta(self, nueva_consulta):
        if self.buscar_indice(nueva_consulta.codigo) != -1:
            return False

        self.consultas.append(nueva_consulta)
        return True

    
    def modificar_consulta(self, codigo, nuevo_motivo, nueva_area):
        consulta = self.buscar_consulta(codigo)

        if consulta is not None:
            consulta.modificar_datos(nuevo_motivo, nueva_area)
            return True

        return False

    
    def eliminar_consulta(self, codigo):
        indice = self.buscar_indice(codigo)

        if indice != -1:
            self.consultas.pop(indice)
            return True

        return False

    
    def derivar_consulta(self, codigo, nueva_area, nuevo_estado):
        consulta = self.buscar_consulta(codigo)

        if consulta is not None:
            consulta.derivar_consulta(nueva_area)
            consulta.actualizar_estado(nuevo_estado)
            return True

        return False

    
    def ordenar_consultas_burbuja(self):
        cantidad = len(self.consultas)

        for i in range(cantidad - 1):
            for j in range(cantidad - i - 1):
                if self.consultas[j].area.lower() > self.consultas[j + 1].area.lower():
                    temporal = self.consultas[j]
                    self.consultas[j] = self.consultas[j + 1]
                    self.consultas[j + 1] = temporal

    
    def obtener_arreglo(self):
        return self.consultas

    
    def obtener_cantidad(self):
        return len(self.consultas)

    def obtener_arreglos_paralelos(self):
        codigos = []
        motivos = []
        areas = []
        horarios = []
        estados = []

        for consulta in self.consultas:
            codigos.append(consulta.codigo)
            motivos.append(consulta.motivo)
            areas.append(consulta.area)
            horarios.append(consulta.horario)
            estados.append(consulta.estado)

        return codigos, motivos, areas, horarios, estados

    def mostrar_arreglos_paralelos(self):
        codigos, motivos, areas, horarios, estados = self.obtener_arreglos_paralelos()

        print("\n--- DATOS EN ARREGLOS PARALELOS ---")

        if len(codigos) == 0:
            print("No hay consultas registradas.")
        else:
            for i in range(len(codigos)):
                print("\nÍndice:", i)
                print("Código:", codigos[i])
                print("Motivo:", motivos[i])
                print("Área:", areas[i])
                print("Horario:", horarios[i])
                print("Estado:", estados[i])

    def guardar_en_txt(self, ruta="consultas.txt"):
        with open(ruta, "w", encoding="utf-8") as archivo:
            for consulta in self.consultas:
                archivo.write(
                    consulta.codigo + "|" +
                    consulta.motivo + "|" +
                    consulta.area + "|" +
                    consulta.horario + "|" +
                    consulta.estado + "\n"
                )

    def contar_consultas_recursivo(self, indice=0):

        if indice >= len(self.consultas):
            return 0

        return 1 + self.contar_consultas_recursivo(indice + 1)            
    
    def cargar_desde_txt(self, ruta="consultas.txt"):
        self.consultas = []

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                
                contenido = archivo.read()

                
                archivo.seek(0)

                
                if contenido != "":
                    for linea in archivo:
                        datos = linea.strip().split("|")

                        
                        if len(datos) == 5:
                            nueva_consulta = Consulta(
                                datos[0], datos[1], datos[2], datos[3], datos[4]
                            )

                            
                            if self.buscar_indice(nueva_consulta.codigo) == -1:
                                self.consultas.append(nueva_consulta)

        except FileNotFoundError:
            
            pass