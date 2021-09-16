from lifestore_file import  lifestore_searches, lifestore_sales, lifestore_products
import sys

##Solicitud al usuario de contraseña y nombre
usuario_01=input("Bienvenido, ingrese su nombre de usuario ")
contraseña_01=input("ingrese su contraseña ")

usuario= ["Admin1", "Admin2"]
contraseña=["123", "abc"] 

if usuario_01  not in usuario and contraseña_01  not in  contraseña:
    sys.exit("Usted no tiene permisos para ejecutar este programa, gracias por su visita")
##fin de nombre y contraseña del usuario 

##Productos vendidos del menos vendido al más vendido 

##Para observar cuantas veces es nombrada la variable en la lista se utiliza el contador
### Los ciclos for son necesarios para poder entrar dentro de la estructura de la lista 
ventas=[] 
contador=0
for producto in lifestore_products:
    for venta in lifestore_sales:
        if producto[0]==venta[1]:
            contador= contador+1
    if contador != 0:
        ventas.append ([contador, producto[0]])
        contador=0
ventas.sort(reverse=True)

##50 productos más vendidos del listado 
##Se busca el nombre del producto en la lista life_store mediante la variable nombre_del_producto
### Las ventas por unidades se obtienen del valor[0] de la lista ventas 
contador=0
print("Los 50 productos mas vendidos de mayor a menor son:")
print("\n")
for id in ventas:
    if contador!=50:
        nombre_del_producto = lifestore_products[id[1]-1][1]
        print(f"{nombre_del_producto} ")   
        print(f"No. Ventas por unidades: {id[0]} ")
    contador += 1
    print("\n")

## En la siguiente parte del codigo seleccionamos los productos menos vendidos por categoría de entre los 50 productos menos vendidos

## Se empleo la función sort() para tener la lista ordenada de menor a mayor
ventas.sort()
productos_menos_vendidos = ventas[:49]
print(productos_menos_vendidos)

print("Productos por categoria con menores ventas")
print("\n")
## Las ventas que se obtuvieron de los productos de acuerdo con sus categorías se obtuvieron comparando el nombre de la categoría
# deseada con el valor del nombre del producto en la lista lifestore_products
print(" Procesadores con menores ventas")
for venta in productos_menos_vendidos:
    procesador= lifestore_products[venta[1]-1][3]
    if procesador == "procesadores":
        print(f"Nombre: {lifestore_products[venta[1]-1][1]}")
        print(f"Unidades vendidas: {venta[0]} ")
print("\n")

print("Tarjetas de video")
for venta in productos_menos_vendidos:
    tarjeta_video= lifestore_products[venta[1]-1][3]
    if tarjeta_video == "tarjetas de video":
        print(f"La  {lifestore_products[venta[1]-1][1]} vendio {venta[0]} unidad")
print("\n")

print("Tarjetas madre")
for venta in productos_menos_vendidos:
    tarjeta_madre= lifestore_products[venta[1]-1][3]
    if tarjeta_madre == "tarjetas madre":
        print(f"La  {lifestore_products[venta[1]-1][1]} vendio {venta[0]} unidad")
print("\n")

print("discos duros")
for venta in productos_menos_vendidos:
    discos= lifestore_products[venta[1]-1][3]
    if discos == "discos duros":
        print(f"La  {lifestore_products[venta[1]-1][1]} vendio {venta[0]} unidad")
print("\n")

print("Audifonos")
for venta in productos_menos_vendidos:
    audifono= lifestore_products[venta[1]-1][3]
    if audifono == "audifonos":
        print(f" {lifestore_products[venta[1]-1][1]} vendio {venta[0]} unidad")
print("\n")

print("Memorias USB")
for venta in productos_menos_vendidos:
    memorias= lifestore_products[venta[1]-1][3]
    if memorias == "memorias usb":
        print(f"La  {lifestore_products[venta[1]-1][1]} vendio {venta[0]} unidad")
print("\n")

print("Pantallas")
for venta in productos_menos_vendidos:
    pantalla= lifestore_products[venta[1]-1][3]
    if pantalla == "pantallas":
        print(f"La  {lifestore_products[venta[1]-1][1]} vendio {venta[0]} unidad")
print("\n")

print("bocinas")
for venta in productos_menos_vendidos:
    bocina= lifestore_products[venta[1]-1][3]
    if bocina == "bocinas":
        print(f"Las  {lifestore_products[venta[1]-1][1]} vendio {venta[0]} unidad")
print("\n")

##fin del código para los productos menos vendidos por categoría

###100 productos con menores busquedas 
##En esta lista se almacenaron los indices de los productos que habían sido buscados por lo menos una vez
lista_busquedas=[]
for busqueda in lifestore_searches:
    numero_busquedas = busqueda[1]
    lista_busquedas.append( numero_busquedas )

##Se creo una lista llamada conteo en la que se almacenaron los valores de los productos en función de su número de búsquedas
conteo=[]
for producto_buscado in lista_busquedas:
    if [lista_busquedas.count(producto_buscado),producto_buscado] not in conteo:
        conteo.append([lista_busquedas.count(producto_buscado),producto_buscado])
conteo.sort(reverse=True)
##Fin del código para productos con menores busqueda 

#Productos mas buscados  
## Para obtener cuales fueron los productos más buscados se utilizo un contador que iniciamos en 0
## Para localizar el nombre del producto fue necesario navegar la lista lifestore_products
print("Productos MÁs buscados")
contador=0
print("Los 100 productos con más busquedas son:")
print("\n")
for numero in conteo:
    if contador!=100:
        nombre_del_producto = lifestore_products[numero[1]-1][1]
        print(f"Nombe: {nombre_del_producto}         Número de búsquedas: {numero[0]} ")
        contador += 1

##Busquedas de productos
##Para obtener la lista que nos diera los porductos que habían sido buscados se localizó ese producto en la
#lista productos_menos_buscados, si el producto no estaba en tal lista, el valor del numero de veces que tal producto aparecía
# junto con el valor del Id de este producto eran almacenados en esa lista
productos_menos_buscados=[]
for producto_buscado in lista_busquedas:
    if [lista_busquedas.count(producto_buscado),producto_buscado] not in productos_menos_buscados:
        productos_menos_buscados.append([lista_busquedas.count(producto_buscado),producto_buscado])
productos_menos_buscados.sort()

print("/"*100)
print("Productos por categoria con menores busquedas")

##Los productos con menores busquedas se buscaron en la lista de productos_menos_buscados. El nombre del producto se busco en la 
## lista lifestore_producs, en cada caso fue necesario hacer conincidir el nombre con la categoria del producto que estabamos 
#buscando 
print(" Procesadores con menores busquedas")
for producto_no_buscado in productos_menos_buscados:
    procesador= lifestore_products[producto_no_buscado[1]-1][3]
    if procesador == "procesadores":
        print(f"El  {lifestore_products[producto_no_buscado[1]-1][1]} fue buscado {producto_no_buscado[0]} vez")
print("\n")

print(" discos duros")
for producto_no_buscado in productos_menos_buscados:
    disco_duro_01= lifestore_products[producto_no_buscado[1]-1][3]
    if disco_duro_01== "dicos duros":
        print(f"El  {lifestore_products[producto_no_buscado[1]-1][1]} fue buscado {producto_no_buscado[0]} vez")
print("\n")

print("Audifonos")
for producto_no_buscado in productos_menos_buscados:
    audifono= lifestore_products[producto_no_buscado[1]-1][3]
    if audifono == "audifonos":
        print(f" {lifestore_products[producto_no_buscado[1]-1][1]}       No. Busquedas: {producto_no_buscado[0]} ")
print("\n")

print("Tarjetas de video")
for producto_no_buscado in productos_menos_buscados:
    tarjeta_video= lifestore_products[producto_no_buscado[1]-1][3]
    if tarjeta_video == "tarjetas de video":
        print(f"La  {lifestore_products[producto_no_buscado[1]-1][1]} fue buscado {producto_no_buscado[0]} vez")
print("\n")

print("Tarjetas madre")
for producto_no_buscado in productos_menos_buscados:
    tarjeta_madre= lifestore_products[producto_no_buscado[1]-1][3]
    if tarjeta_madre == "tarjetas madre":
        print(f"La  {lifestore_products[producto_no_buscado[1]-1][1]} fue buscado {producto_no_buscado[0]} veces")
print("\n")

print("Memorias USB")
for producto_no_buscado in productos_menos_buscados:
    memorias= lifestore_products[producto_no_buscado[1]-1][3]
    if memorias == "memorias usb":
        print(f"La  {lifestore_products[producto_no_buscado[1]-1][1]} fue buscado {producto_no_buscado[0]} veces")
print("\n")

print("Pantallas")
for producto_no_buscado in productos_menos_buscados:
    pantalla= lifestore_products[producto_no_buscado[1]-1][3]
    if pantalla == "pantallas":
        print(f"La  {lifestore_products[producto_no_buscado[1]-1][1]} fue buscado {producto_no_buscado[0]} veces")
print("\n")

print("bocinas")
for producto_no_buscado in productos_menos_buscados:
    bocina= lifestore_products[producto_no_buscado[1]-1][3]
    if bocina == "bocinas":
        print(f"Las  {lifestore_products[producto_no_buscado[1]-1][1]} fue buscado {producto_no_buscado[0]} veces")
print("\n")

##fin del codigo para productos por catregoria con menores busquedas 

##Productos por reseña y categoría

print("productos por reseña y por servicio")

## Para obtner los productos que no se vendieron se realizo una comparacion entre los valores almacenados para los Id
# en las listas lifestore_products y lifestore_sales. Los productos que no podían localizarse en ambas listas se alamacenaron en 
# una tercera lista que concentró los productos no vendidos 
print("los productos que no se vendieron son")
for producto in lifestore_products:
    for venta in lifestore_sales:
        if producto[0] != venta[1]:
            producto_no_vendido = True      
    if producto_no_vendido == True:
        print(f"ID: {producto[0]}   Nombre: {producto[1]} ")
print("\n")

conteo.sort(reverse=True)
ventas.sort(reverse=True)

##Código para productos más buscados 
##En este caso se tuvo que realizar una identación de tres niveles y obtner una lista en la que se pudieran 
# almacenar los valores que se necesitaban, en este caso, el Id del producto, su nombre y su numero de busquedas 

productos_mas_buscados=[]
for producto in lifestore_products:
    for producto_buscado in conteo:
        if producto_buscado[1]==producto[0]:
            productos_mas_buscados.append([producto[0], producto[1], producto_buscado[0]])

##El promedio que se obtuvo de la forma que a continuación se ilustra, fue un valor necesario para posteriormente obtner los 
# mejores y peores productos en función de su número de búsquedas y ventas
lista=[]
for busquedas in productos_mas_buscados:
    b=int(busquedas[2])
    for id in ventas:
        a=int(id[0])
        if id[1]==busquedas[0]:
         promedio=(a+b)/2
         lista.append([promedio, busquedas[0], busquedas[1]])

print("Los 56 mejores productos de acuerdo con el número de venta y numero de búsquedas son:")
for elemento in productos_mas_buscados:
    for id in ventas:
        if elemento[0]==id[1]:
         print(f"ID: {id[1]}     Nombre: {elemento[1]}")
         print(f"No.busquedadas: {elemento[2]}   ventas {id[0]}")
         print("\n")     
print("\n")
## Para calcular los mejores 20 productos por "reseña" considerando el análisis realizado para obtnere los productos más vendidos
### y los productos con más busquedas, sin eliminar los productos devueltos, tenemos el código siguiente:

##20 mejores prodctos 
## Se empleo la funcion sort() inverse para poder obtner los valores acomodados del más grande al más pequeño 
#Se considero la lista de productos_mas_buscados para poder obtener una lista que nos diera los productos mejor ranqueados

lista.sort(reverse=True)
productos_mejores=lista[0:19]

print("Mejores 20 productos de acuerdo a numero de ventas y numero de busquedas")
for elemento in productos_mejores:
    print(f"Id: {elemento[1]}    Nombre: {elemento[2]}   Promedio: {elemento[0]}")
print("\n")

### 20 Peores productos 
###Se empleo la función sort() para poder obtener los valores ordenados de menor a mayor
##Se realizo una nueva lista que contenia a los productos ranqueados con el puntaje más bajo de acuerdo con el promedio
lista.sort()
productos_peores=lista[0:19]
print("Peores 20 productos de acuerddo a numero de búsquedas y ventas")
for elemento in productos_peores:
    print(f"Id: {elemento[1]}    Nombre: {elemento[2]}   Promedio: {elemento[0]}")
print("\n")

##fin del código para mejores y peores productos de acuerdo con reseña 

##Calculos de ingresos 

##En este caso se empleo la funcion round para obtner el valor redondeado 
#Fue necesario contar el numero de elementos en la lista para poder obtener el promedio de las ventas
print("Promedio de Ventas Mensuales")
ventas_anuales=len(lifestore_sales)
ventas_promedio_mensuales=(ventas_anuales)/12
Numero_redondeado = round(ventas_promedio_mensuales, 2)
print(Numero_redondeado)
print("\n")

##Ingresos mensuales
print("Ingresos mensuales")
ingresos_mensuales = []
##Ciclo for que permite validar los valores encontrados para una lista de datos 
for i in range(1,13):
    total = 0
    for ventas in lifestore_sales:
        producto_vendido = ventas[1]
        ganancia = lifestore_products[ventas[1]-1][2]
        fecha_de_venta = ventas[3]
        mes_de_venta = fecha_de_venta[3:5]
        if i == int(mes_de_venta):
            total += ganancia
    ingresos_mensuales.append([total,i])
    ingresos_mensuales.sort(reverse=True)
print("\n")

for ingreso in ingresos_mensuales:
    print(f"Mes: {ingreso[1]}           Ingresos: {ingreso[0]}")
print("\n")

##meses con mayores ventas

meses_con_mas_ventas=ingresos_mensuales[0:5]

print("Meses con mayores ventas")
for ingresos in meses_con_mas_ventas:
    print(f"Mes: {ingresos[1]}   Ingresos: {ingresos[0]} pesos")

valores=[]
inicio=0
for ingreso in ingresos_mensuales:
    m=int(ingreso[0])
    inicio=inicio+m
    valores.append(inicio)
no_meses=len(ingresos_mensuales)
promedio_1=inicio/(no_meses)
print(f"Promedio de ingresos mensuales: {promedio_1} pesos")
print("Total de ingresos anuales:")
print(f"{valores[11]} pesos")


