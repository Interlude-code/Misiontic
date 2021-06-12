from concesionario import concesionario
from vendedores import vendedores
from carro import carro
from moto import moto
from clientes import cliente



def ingresarcarro():
    car=[]
    plantilla=['kilometraje', 'modelo', 'precio','inventario','siGas','siHybrido','marca']
    for i in plantilla:
        car.append(input("Ingrese  " + i + " "))
    car=carro(car[0],car[1],car[2],car[3],car[4],car[5],car[6])
    concesionario1.agregarCarro(car)

def ingresarmoto():
    

    motos=[]
    plantilla=['kilometraje', 'modelo', 'precio','inventario','siSoat','siTecnico','cilindraje']
    for i in plantilla:
        motos.append(input("Ingrese  " + i + " "))
    motos=moto(motos[0],motos[1],motos[2],motos[3],motos[4],motos[5],motos[6])
    concesionario1.agregarMoto(motos)
    
def ingresavendedor():

    vend=[]
    plantilla=['nombre', 'telefono', 'correo', 'documento', 'identificacionEmpresarial']
    for i in plantilla:
        vend.append(input("Ingrese  " + i + " "))
    vend=vendedores(vend[0],vend[1],vend[2],vend[3],vend[4])
    concesionario1.agregarVendedor(vend)    
    
def ingresacliente():
    
    cl=[]
    plantilla=['nombre', 'telefono', 'correo', 'documento', 'direccionEnvio', 'correoFacturacion']
    for i in plantilla:
        cl.append(input("Ingrese  " + i + " "))
    cl=cliente(cl[0],cl[1],cl[2],cl[3],cl[4],cl[5])
    concesionario1.agregarCliente(cl)    

def venderCarro():
    vn=input("Ingrese el nombre del vendedor : ")
    vn=concesionario1.buscarVendedor(vn)
    if not vn:
        print('Vendedor no encontrado !acceso denegado a la venta! ')
        return
    cl=input("Ingrese el documento del cliente : ")
    if not cl:
        print("Cliente no encontrado")
        add=input("Desea agregar como cliente nuevo ").upper()
        if add=='SI':
            ingresacliente()
            venderCarro()
        elif add =='NO' :
            return
    
    opt = input("Ingrese el Codigo de venta del vehiculo deseado : ")
    opt = concesionario1.agregarCarro(opt)
    if not opt:
        print('Codigo de vehiculo no existe : ')
        return
    
    


def venderMoto():
    cl=input("Ingrese el documento del cliente : ")
    vn=input("Ingrese el nombre del vendedor : ")

    
    
    
    
nombreConcesionario = input("Ingresa el nombre del concesionario ")
concesionario1= concesionario(nombreConcesionario)

    
while True:
    opt= input('''Ingrese el numero para la accion seleccionada :
1. Para ingresar un vehiculo
2. Ver inventario
3. Ingresar vehiculos al Inventario
4. Para ingresar un vendedor
5. Ingresar un cliente
6. Vender un vehiculo
''')
    if opt== '1':
        opt=input('''Tipo de vehiculo : 
1. Carro
2. Moto 
''')
        if  opt == '1':
            ingresarcarro()
        elif opt=='2':
            ingresarmoto()
        else:
            print(" opcion erronea ")
    elif opt=='2':
        concesionario1.verInventario()
    elif opt == '4':
        
        
        ingresavendedor()
    elif opt == '5':
        ingresacliente()
    elif opt=='6':
        opt=input('''Tipo de vehiculo : 
1. Carro
2. Moto 
''')
        if  opt == '1':
            venderCarro()
        elif opt=='2':
            venderMoto()
        else:
            print(" opcion erronea ")
    
        
    
    else:
        print('''-------------------------------------------------------------
              opcion erronea''')
        
    
    
