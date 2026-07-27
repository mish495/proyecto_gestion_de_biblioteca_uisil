from proyecto_1_biblioteca.modelos.persona import Persona

class Usuario(Persona):

    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion, nombre, correo, telefono)
        self.estado = "Activo"