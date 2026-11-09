from consulta import Consulta

class GestionConsultas:
    def __init__(self):
        self.consultas = []


    def buscar_indice(self, codigo: str) -> int:
        for i in range(len(self.consultas)):
            if self.consultas[i] is not None and self.consultas[i].codigo == codigo:
                return i
        return -1


    def buscar_consulta(self, codigo: str) -> Consulta:
        idx = self.buscar_indice(codigo)
        if idx != -1:
            return self.consultas[idx]
        return None


    def registrar_consulta(self, nueva_consulta: Consulta) -> bool:
        if self.buscar_indice(nueva_consulta.codigo) != -1:
            return False
        self.consultas.append(nueva_consulta)
        return True


    def modificar_consulta(self, codigo: str, nuevo_motivo: str, nueva_area: str) -> bool:
        consulta = self.buscar_consulta(codigo)
        if consulta is not None:
            consulta.motivo = nuevo_motivo
            consulta.area = nueva_area
            return True
        return False


    def eliminar_consulta(self, codigo: str) -> bool:
        idx = self.buscar_indice(codigo)
        if idx != -1:
            self.consultas.pop(idx)
            return True
        return False


    def derivar_consulta(self, codigo: str, nueva_area: str, nuevo_estado: str) -> bool:
        consulta = self.buscar_consulta(codigo)
        if consulta is not None:
            consulta.area = nueva_area
            consulta.estado = nuevo_estado
            return True
        return False


    def ordenar_consultas_burbuja(self):
        n = len(self.consultas)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.consultas[j].area.lower() > self.consultas[j + 1].area.lower():
                    temporal = self.consultas[j]
                    self.consultas[j] = self.consultas[j + 1]
                    self.consultas[j + 1] = temporal


    def obtener_arreglo(self) -> list:
        return self.consultas


    def obtener_cantidad(self) -> int:
        return len(self.consultas)

    def guardar_en_txt(self, ruta: str = "consultas.txt"):
        with open(ruta, "w", encoding="utf-8") as archivo:
            for c in self.consultas:
                archivo.write(f"{c.codigo}|{c.motivo}|{c.area}|{c.horario}|{c.estado}\n")


    def cargar_desde_txt(self, ruta: str = "consultas.txt"):
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    partes = linea.strip().split("|")
                    if len(partes) == 5:
                        self.consultas.append(Consulta(partes[0], partes[1], partes[2], partes[3], partes[4]))
        except FileNotFoundError:
            pass
