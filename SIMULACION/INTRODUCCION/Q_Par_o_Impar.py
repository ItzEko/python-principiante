#DETERMINAR SI EL USUARIO A INGRESADO UN NUMERO PAR O E IMPAR 

num=int(input("ingresa un numero y yo te dire si es par o impar"))
#aqui estamos diciendo que si el numero es ingresado a la hora de dividirlo entre 2 este da como residuo cero
#es por que este es par ya que no hay sobrantes
if num %2== 0:
    print(f"el numero que has ingresado es par -> {num}")
#Aca estamos diciendo que si el numero es ingresado a la hora de dividirlo entre 2 este su residuo da un numero diferente
#de cero entonces es impar   
elif num %2!=0:
    print(f"el numero que ingresaste es impar-> {num}")
else:
    print("No has ingresado algo valido")