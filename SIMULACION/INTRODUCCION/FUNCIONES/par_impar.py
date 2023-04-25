# Crear una funcion que detecte el par y el impar 

num=int (input('ingresa un numero y yo te dire si es par o impar -> '))
def detectar(num):
    if num %2== 0:
        print(f"el numero que has ingresado es par -> {num}")
    elif num %2!=0:
        print(f"el numero que ingresaste es impar-> {num}")
    else:
        print("No has ingresado algo valido")
detectar(num)



