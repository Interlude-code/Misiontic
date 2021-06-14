from persona import Persona
import random


class vendedores(Persona):
    def __init__(self, nombre, telefono, correo, documento):
        super().__init__(nombre, telefono, correo, documento)
        self.identificacionEmpresarial = random.randint(1000,9999)