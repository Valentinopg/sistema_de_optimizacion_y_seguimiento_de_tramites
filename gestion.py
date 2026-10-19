from consulta import Consulta


class GestionConsultas:
    """Clase encargada de la lógica y la administración de los registros."""

    def __init__(self, max_consultas: int = 100):
        self.MAX_CONSULTAS = max_consultas
        self.consultas = [None] * self.MAX_CONSULTAS
        self.cantidad_consultas = 0

    def buscar_indice(self, codigo: str) -> int:
        for i in range(self.cantidad_consultas):
            if self.consultas[i] is not None and self.consultas[i].codigo == codigo:
                return i
        return -1

    def buscar_consulta(self, codigo: str) -> Consulta:
        idx = self.buscar_indice(codigo)
        if idx != -1:
            return self.consultas[idx]
        return None

    def registrar_consulta(self, nueva_consulta: Consulta) -> bool:
        if self.cantidad_consultas >= self.MAX_CONSULTAS:
            return False
        if self.buscar_indice(nueva_consulta.codigo) != -1:
            return False

        self.consultas[self.cantidad_consultas] = nueva_consulta
        self.cantidad_consultas += 1
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
            for i in range(idx, self.cantidad_consultas - 1):
                self.consultas[i] = self.consultas[i + 1]

            self.cantidad_consultas -= 1
            self.consultas[self.cantidad_consultas] = None
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
        for i in range(self.cantidad_consultas - 1):
            for j in range(0, self.cantidad_consultas - i - 1):
                if self.consultas[j].area.lower() > self.consultas[j + 1].area.lower():
                    temporal = self.consultas[j]
                    self.consultas[j] = self.consultas[j + 1]
                    self.consultas[j + 1] = temporal

    def obtener_arreglo(self) -> list:
        return self.consultas

    def obtener_cantidad(self) -> int:
        return self.cantidad_consultas
