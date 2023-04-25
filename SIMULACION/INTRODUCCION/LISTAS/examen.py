vector=[]
# rango=int(input('ingresa el numero 10 que es el tamaño del vector'))
# contador=0
# while contador < rango:
#     num=int(input('ingresa los numeros del vector'))
#     vector.append(num)
#     contador+=1
for indice in range(10):
    num=int(input('ingresa los numeros del vector'))
    vector.append(num)
print('el vector es :',(vector))
for elemento in vector:
    cuadrado=elemento**2
    cubo = elemento**3
    print('el elemento', elemento,f'su cuadrado es : {cuadrado} y su cubo es : {cubo}')
