class Consulta:

    def __init__(self, codigo, motivo, area, horario, estado="Pendiente"):
        self.codigo = codigo
        self.motivo = motivo
        self.area = area
        self.horario = horario
        self.estado = estado

    def obtener_resumen(self):
        return ("Código: " + self.codigo +
                " | Área: " + self.area +
                " | Horario: " + self.horario +
                " | Estado: " + self.estado +
                " | Motivo: " + self.motivo)

    def modificar_datos(self, nuevo_motivo, nueva_area):
        self.motivo = nuevo_motivo
        self.area = nueva_area

    def derivar_consulta(self, nueva_area):
        self.area = nueva_area
        self.estado = "En proceso"

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_datos(self):
        print("\n--- INFORMACIÓN DE LA CONSULTA ---")
        print("Código:", self.codigo)
        print("Motivo:", self.motivo)
        print("Área:", self.area)
        print("Horario:", self.horario)
        print("Estado:", self.estado)