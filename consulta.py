class Consulta:
    """Representa un ticket de atención de un estudiante."""
    
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
