  
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

        
        