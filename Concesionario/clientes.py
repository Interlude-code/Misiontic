
from persona import Persona


class cliente(Persona):
    def __init__(self, nombre, telefono, correo, documento, direccionEnvio, correoFacturacion):
        super().__init__(nombre, telefono, correo, documento)
        self.direccionEnvio = direccionEnvio
        self.correoFacturacion = correoFacturacion
   