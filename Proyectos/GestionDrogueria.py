#codificacion camel case
# 1.5 float 35 in johan manuel str 
ventasTotales = 0.0

#Solicitar el número de productos
numProductos = int(input('Ingrese el número de productos a gestionar: '))

#Listas para almacenar la información
nombres = []
precios = []
cantidades = []

print('Ingreso inicial de productos a la tienda: ')
for i in range(numProductos):
    print(f'Producto {i+1}:')
    nombre = input('Ingrese el nombre de producto: ').lowet() #.lower() es para poner todo lo que ingrese el usuario en minuscula 
    nombres.append(nombre)
    precio = float(input('Digite el precio  del producto: '))
    precios.append(precios)
    cantidad = int(input('Digite la cantidad del producto: '))
    cantidades.append(cantidad)
    
#Ciclo principal menu
while True:
    print('\n ---MENU DE GESTION DROGUERIA---')
    print('1. Vender producto')
    print('2. Mostrar inventario')
    print('3. Mostrar ventas totales')
    print('4. Salir')
    
    opcion = int(input('Ingrese una opcion: '))
    
    if opcion == 1:
        print('\nVender producto')
        nombreVenta = input('Ingrese el nombre el producto a vender: ').lower()
        cantidadVender = int(input('Ingrese la cantidad a vender: '))
        productoEncontrado = False
        
        for i in range(len(nombres)):
            if nombres[i]== nombreVenta:
                productoEncontrado = True
        