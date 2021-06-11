from persona import Persona


class vendedores(Persona):
    def __init__(self, nombre, telefono, correo, documento, identificacionEmpresarial):
        super().__init__(nombre, telefono, correo, documento)
        self.identificacionEmpresarial = identificacionEmpresarial