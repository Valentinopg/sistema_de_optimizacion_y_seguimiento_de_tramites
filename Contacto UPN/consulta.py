class Consulta:
    def __init__(self, codigo: str, motivo: str, area: str, horario: str = "08:30 AM", estado: str = "Pendiente"):
        self._codigo = codigo
        self._motivo = motivo
        self._area = area
        self._horario = horario
        self._estado = estado


    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def motivo(self) -> str:
        return self._motivo

    @motivo.setter
    def motivo(self, nuevo_motivo: str):
        if len(nuevo_motivo.strip()) > 0:
            self._motivo = nuevo_motivo


    @property
    def area(self) -> str:
        return self._area


    @area.setter
    def area(self, nueva_area: str):
        if len(nueva_area.strip()) > 0:
            self._area = nueva_area


    @property
    def horario(self) -> str:
        return self._horario


    @property
    def estado(self) -> str:
        return self._estado


    @estado.setter
    def estado(self, nuevo_estado: str):
        if nuevo_estado in ["Pendiente", "En proceso", "Atendida"]:
            self._estado = nuevo_estado


    def obtener_resumen(self) -> str:
        return (f"Código: {self._codigo:<12} | Sede/Área: {self._area:<12} | "
                f"Horario: {self._horario:<10} | Estado: {self._estado:<12} | Motivo: {self._motivo}")


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
        """Guarda todas las consultas: una por línea, campos separados por '|'."""
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
