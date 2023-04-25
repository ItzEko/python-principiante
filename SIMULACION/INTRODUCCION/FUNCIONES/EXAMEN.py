#LLenar array 5 eleementps solo acepta numeros y arroja un mensaje si estos no son numeros

array01=[]
def array_numeros (array01):
    for num in range(5):
        numeros=input('ingresa el numero -> ')
        if str.isdigit(numeros):
            array01.append(numeros)
            print(f'tu array es el siguiente: {array01} ')
        else:
            print('NO has ingresado numeros validos vuelve a ejecutar ')
        
array_numeros(array01)


