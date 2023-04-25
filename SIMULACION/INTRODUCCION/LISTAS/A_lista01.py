lista=[1,'soy una cadena',1.2,[32,'hola'],42,'pera']
#ACCEDER A UN ELEMENTO DE LA LISTA MEDIANTE EL INDICE
print(lista[4])

#PARA VER UN SUBNIVEL DE LA CADENA SE HACE ASI:
print (lista[3][0])

lista2=[1,'soy una cadena',1.2,[32,'hola'],42,'pera',['pepe','juan',['carro','azul']],'dia']

print (lista2[6][2][1])

#ACCEDER A LOS ELEMENTOS DE LAS LISTAS MEDIANTE UN RANGO
print(lista2[0:4])

#MUESTRA LOS ESPACIOS O INDICES QUE EXISTEN, NO LA POSICION ("FUNCION LEN ")
print(len(lista2))

#APPEND ES LA FUNCION QUE AGREGA CUALQUIER TIPO DE DATO AL FINAL DE LA LISTA
lista.append('UWU')
print(lista)

#RECORRER O ITERRAR UN ARREGLO MEDIANTE UN CICLIO FOR
#para cada indice en la lista (imprime uno por uno elemento de la lista)
for indice in lista:
    print(indice)

#Mostrar un elemento de la lista mientras sea real se va a ejecutar una parte del codigo 
#Aqui celda es la que me va a mostrar el indice osea su posicion del valor que este dentro de la lista
celda=1   
while celda in lista:
    print(f"su indice es : {lista[celda]}")
    celda+=1
    
#FUNCIONES
#len(lista) = cuenta el numeros de elementos que tiene una lista 
print(f'total de elementos de la lista -> {len(lista)}')

# .append() = Adjunta un elemento o indice, agrega un elelemnto al arreglo al final de la lista
lista2.append('soy el nuevo')
print(lista2)

#.insert() = Agrega un elemento en una posicion especifica
           #indice,valor   
lista.insert(0,'hola')
print(lista)

# .remove() = Elimina un elemento en una posicion especifica
lista.remove('soy una cadena')
print(lista)

# .pop() = Elimina el ultimo elemento del arreglo
lista2.pop()
print(lista2)

#del = Eliminar objetos o eliminar listas completas
# del lista
# print(lista)

#Agregar VARIOS ELEMENTOS DE GOLPE A FINAL DE LA LISTA 
lista.extend([1,2,3,4,])
print(lista)

#PARA SABER EL INDICE DE UN ELEMENTO DE LA LISTA
print(lista.index('hola'))

#CUANTAS VECES APARECE UN VALOR EN LA LISTA 
print(lista.count(1))