#detalles array cuantos elementos tiene y cuantos positivos,negativos y neutros
array02=[]
num_cant=int(input('ingresa la cantidad de numeros que va a tener el array'))
contador=0
while num_cant>contador:
    num01=int(input('ingresa los numeros'))
    array02.append(num01)
    contador+=1
def detalles_array (array01):
    num_po=0
    num_ne=0
    num_neu=0
    for elemento in array02:
                if elemento< 0:
                    num_ne +=1
                elif elemento> 0:
                    num_po+=1
                elif elemento== 0:
                    num_neu+=1
    print (f'la cantidad de numeros negativos son:{num_ne}')
    print (f'la cantidad de numeros positivos son:{num_po}')
    print (f'la cantidad de numeros neutrales son:{num_neu}')
detalles_array(array02)      