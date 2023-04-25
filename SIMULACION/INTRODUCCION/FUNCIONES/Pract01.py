# Crear una funcion que detecte el par y el impar 
#funcion que sume numeros
#Funcion que multiplique los numeros
#funcion que encuentre el menor de un arreglo 
#funcion que encuentre el menor de un arreglo 
#sacar el factorial de un numero 
#funcion que convierta los grados celsius a Farenheit 
#otra funcion donde convierta los Farenheit a Celsisus 

#Realizar una funcion la cual saque la media de una lista 

def media (lista):
    return sum(lista)/len(lista)
lista=[4,7,8,9]
media01=media(lista)
print(f'la media de la lista es la siguiente -> {media01}')
lista=[9,10,8,9,10,10]
media01=media(lista)
print(f'la media de la lista es la siguiente -> {media01}')

# Crear una funcion que detecte el par y el impar 
num=int(input('ingresa el numero'))
def par_impar(num):
    if num%2==0:
        print('el numero es par')
    else:
        print('el numero es impar')
par_impar(num)

#funcion que sume numeros

lista_num=[]
numeros_cant=float(input('ingresa cantidad de numeros a sumar'))
contador=0
while numeros_cant > contador:
    numeros=float(input('ingresa los numeros -> '))
    lista_num.append(numeros)
    contador+=1
def suma01 (lista_num):
    sumaa=0
    for numero in lista_num:
        sumaa=sumaa + numero
    print(f'la suma de los numeros es ={sumaa}')
suma01(lista_num)

#funcion que encuentre el menor de un arreglo 

arreglo=[]
numeros=int(input('ingresa la cantidad de numeros que va a tener el arreglo'))
contador=0
while numeros > contador:
    numm=int(input('ingresa los numeros del arreglo'))
    arreglo.append 