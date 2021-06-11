from vehiculos import vehiculos




class carro(vehiculos):
    def __init__(self, kilometraje, modelo, precio,inventario,siGas,siHybrido,marca): 
        super().__init__(kilometraje, modelo, precio,inventario)
        self.marca=marca
        self.siGas=siGas
        self.siHybrido=siHybrido

    ###prueba damaris

   

