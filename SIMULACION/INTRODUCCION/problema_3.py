# CALCULADORA
print("Hola bienvenido a una calculadora selecciona el numero de  la opcion que deseas realizar")

(print("1.- Suma"))
(print("2.- Resta"))
(print("3.- Multiplicacion"))
(print("4.- Division"))

opcion = int(input())
print ("ingresa los 2 numeros")
num_1 = int(input())
num_2 = int(input())

suma = num_1+ num_2
resta = num_1 - num_2
multiplicacion = num_1 *  num_2
division = num_1 / num_2



if opcion == 1 :
    print (f"La suma de los numeros es  :{suma}")

elif opcion ==2 :
     print (f"La resta de los numeros es  :{resta}")
elif opcion ==3 :
     print (f"La multiplicacion de los numeros es  :{multiplicacion}")
elif opcion == 4:
     print (f"La division de los numeros es  :{division}")
else:
    print("none")