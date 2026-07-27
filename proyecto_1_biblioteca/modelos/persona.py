class Persona:

    def __init__(self, identificacion, nombre, correo, telefono):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def mostrar_datos(self):
        return f"{self.identificacion} - {self.nombre}"