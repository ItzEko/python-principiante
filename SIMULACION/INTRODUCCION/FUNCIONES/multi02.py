
#funcion que sume numeros
lista = []
rango = int(input('ingresa la cantidad de numeros a sumar'))
contador=0
while contador < rango:
            numeros=float(input('ingresa los numeros que se sumaran '))
            lista.append(numeros)
            contador +=1
def suma01(lista):
    suma=0
    for num in lista:
        suma=suma + num
    print(f'el resultado de la suma es:{suma}')
suma01(lista)


#Funcion que multiplique los numeros
lista = []
rango = int(input('ingresa la cantidad de numeros a multiplicar'))
contador=0
while contador < rango:
            numeros=float(input('ingresa los numeros que se multiplicaran '))
            lista.append(numeros)
            contador +=1
def multiplicacion01(lista):
    multi=1
    for num in lista:
        multi=multi * num
    print(f'el resultado de la multiplicacion es:{multi}')
multiplicacion01(lista)