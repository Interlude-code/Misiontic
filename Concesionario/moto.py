from vehiculos import vehiculos

class moto(vehiculos):
    def __init__(self, kilometraje, modelo, precio,inventario,siSoat,siTecnico,cilindraje): 
        super().__init__(kilometraje, modelo, precio,inventario)
        self.siSoat=siSoat
        self.siTecnico=siTecnico
        self.cilindraje=cilindraje