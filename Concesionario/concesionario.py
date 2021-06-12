  
'''Hacer un código para la gestión de ventas en un concesionaro de vehículos usados

El concesionario tiene los siguientes atributos:
    nombre
    lista de clientes
    lista de vendedores
    lista de vehículos que se pueden vender

Un vehículo tiene los siguientes atributos:
    kilometraje
    modelo (año)
    precio

Un vehículo puede ser de dos tipos:
    carro:
        marca
        si tiene gas
        si es hibrido
    moto:
        si tiene soat
        si tiene tecnicomecanica
        cilindraje

hacer un código en el que se puedan vender vehículos ingresando el cliente, 
el vendedor y el vehículo que se quiere vender

El concesionario debe tener la posibilidad de agregar nuevos vehículos al inventario'''

class concesionario:
    def __init__(self,nombre):
        self.nombre = nombre
        self.listadeClientes= []
        self.listadeVendedores= []
        self.listadeCarros= []
        self.listadeMotos=[]
        
    def agregarCarro(self,carro):
        self.listadeCarros.append(carro)
        
    def agregarMoto(self,moto):
        self.listadeMotos.append(moto)
    
    def agregarVendedor(self,vendedor):
        self.listadeVendedores.append(vendedor)
    
    def agregarCliente(self,cliente):
        self.listadeClientes.append(cliente)
        
    def buscarVendedor(self,documento):
        for vendedor in self.listadeVendedores:
            if vendedor.documento == documento:
                return vendedor
            else:
                return False
        
    def buscarCliente(self,documento):
        for cliente in self.listadeClientes:
            if cliente.documento == documento:
                return cliente
            else :
                return False
    
    def verInventario(self):
        for vehiculos in self.listadeCarros:
            print("Carro ")
            print("Marca : ",vehiculos.marca)
            print("Kilometraje : ",vehiculos.kilometraje)
            print("Modelo : ",vehiculos.modelo)
            print("Tiene Gas : ",vehiculos.siGas)
            print("Vehiculo hibrido : ",vehiculos.siHybrido)
            print("Cantidad Disponible : ",vehiculos.inventario)
            print("Precio : ",vehiculos.precio)
            print("-----------------------------------------------")
        for vehiculos in self.listadeMotos:
            print("Moto ")
            print("Cilindraje : ",vehiculos.cilindraje)
            print("Kilometraje : ",vehiculos.kilometraje)
            print("Modelo : ",vehiculos.modelo)
            print("Tiene SOAT : ",vehiculos.siSoat)
            print("Tiene Tecnicomecanica : ",vehiculos.siTecnico)
            print("Precio : ",vehiculos.precio)
            print("Cantidad Dispoible : ",vehiculos.inventario)
            print("-----------------------------------------------")    
        
        
        

        
        