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
    car=carro(car[0],car[1],car[2],int(car[3]),car[4],car[5],car[6])
    concesionario1.agregarCarro(car)
    print('Carro creado con exito ')

def ingresarmoto():
    

    motos=[]
    plantilla=['kilometraje', 'modelo', 'precio','inventario','siSoat','siTecnico','cilindraje']
    for i in plantilla:
        motos.append(input("Ingrese  " + i + " "))
    motos=moto(motos[0],motos[1],motos[2],motos[3],motos[4],motos[5],motos[6])
    concesionario1.agregarMoto(motos)
    print('Moto creada con exito ')
    
def ingresavendedor():

    vend=[]
    plantilla=['nombre', 'telefono', 'correo', 'documento']
    for i in plantilla:
        vend.append(input("Ingrese  " + i + " "))
    vend=vendedores(vend[0],vend[1],vend[2],vend[3])
    concesionario1.agregarVendedor(vend)  
    print('Vendedor creado con exito ')
    
def ingresacliente():
    
    cl=[]
    plantilla=['nombre', 'telefono', 'correo', 'documento', 'direccionEnvio', 'correoFacturacion']
    for i in plantilla:
        cl.append(input("Ingrese  " + i + " "))
    cl=cliente(cl[0],cl[1],cl[2],cl[3],cl[4],cl[5])
    concesionario1.agregarCliente(cl)    
    print('Cliente creado con exito ')

def venderCarro():
    vn=input("Ingrese el Codigo de vendedor : ")
    vn=concesionario1.buscarVendedor(vn)
    if not vn:
        print('Vendedor no encontrado !acceso denegado a la venta! ')
        return
    cl=input("Ingrese el documento del cliente : ")
    cl=concesionario1.buscarCliente(cl)
    if not cl:
        print("Cliente no encontrado")
        add=input("Desea agregar como cliente nuevo ").upper()
        if add=='SI':
            ingresacliente()
            print('Cliente creado con exito ')
            venderCarro()
        elif add =='NO' :
            return
    
    opt = input("Ingrese el Codigo de venta del vehiculo deseado : ")
    opt = concesionario1.buscarCarro(opt)
    if not opt:
        print('Codigo de vehiculo no existe : ')
        return
    opt.inventario -= 1
    print('! Venta exitosa !')
    
def venderMoto():
   def venderMoto():
    vn=input("Ingrese el Codigo de vendedor : ")
    vn=concesionario1.buscarVendedor(vn)
    if not vn:
        print('Vendedor no encontrado !acceso denegado a la venta! ')
        return
    cl=input("Ingrese el documento del cliente : ")
    cl=concesionario1.buscarCliente(cl)
    if not cl:
        print("Cliente no encontrado")
        add=input("Desea agregar como cliente nuevo ").upper()
        if add=='SI':
            ingresacliente()
            print('Cliente creado con exito ')
            venderMoto()
            
        elif add =='NO' :
            return
    
    opt = input("Ingrese el Codigo de venta del vehiculo deseado : ")
    opt = concesionario1.buscarMoto(opt)
    if not opt:
        print('Codigo de vehiculo no existe : ')
        return
    opt.inventario -= 1
    print('! Venta exitosa !')

def agregarinventario():
    opt=input('''Tipo de vehiculo : 
1. Carro
2. Moto 
''')
    if  opt == '1':
        sel = input("Ingrese el Codigo de venta del vehiculo deseado : ")
        sel = concesionario1.buscarCarro(sel)
        if not sel:
            print('Codigo de vehiculo no existe : ')
            return
        pd=int(input("Ingresa la cantidad de unidades que deseas agregar : "))
        sel.inventario += pd 
        print('! actulizacion exitosa !')

    elif opt=='2':
        sel = input("Ingrese el Codigo de venta del vehiculo deseado : ")
        sel = concesionario1.buscarMoto(sel)
        if not sel:
            print('Codigo de vehiculo no existe : ')
            return
        pd=int(input("Ingresa la cantidad de unidades que deseas agregar : "))
        sel.inventario += pd 
        print('! actulizacion exitosa !')
        
    else:
        print('Opcion erronea')
    
    
    
    
    
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
    elif opt=='3':
        agregarinventario()
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
        
    
    
