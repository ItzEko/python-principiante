# encontrar los numeros negativos y positivos de una lista y neutrales 
lista = []
rango = int(input('ingresa el tamaño de la lista'))
contador=0
while contador < rango:
    numeros=float(input('ingresa los numeros de la lista '))
    lista.append(numeros)
    contador +=1
num_po=0
num_ne=0
num_neu=0
for elemento in lista:
        if elemento< 0:
            num_ne +=1
        elif elemento> 0:
            num_po+=1
        elif elemento== 0:
            num_neu+=1
print (f'la cantidad de numeros negativos son:{num_ne}')
print (f'la cantidad de numeros positivos son:{num_po}')
print (f'la cantidad de numeros neutrales son:{num_neu}')