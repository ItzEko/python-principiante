#funcion que encuentre el menor de un arreglo 

array =[]
rango=float(input('ingresa el tamaño del arreglo '))
contador=0
while contador < rango:
        numeros=float(input('ingresa los numeros del array -> '))
        array.append(numeros)
        contador+=1
def minimo(array):
    num_menor = 1000
    for i in array:
        if i < num_menor:
            num_menor=i
    print(array)
    print(f'el numero menor es:{num_menor}')
minimo(array)



