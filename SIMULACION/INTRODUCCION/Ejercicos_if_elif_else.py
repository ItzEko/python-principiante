

#DIA DE DESCANSO 
#Realize el siguiente progrmama. un padre desea 

futbol =input(("ingresa true en caso de que el dia sea de descanso, de lo contrario false"))

respuesta = futbol == "true"

if respuesta:
    print(f'puedes asistir al partido de futbol   :{futbol}')
else :
        print(f'No puedes asistir al partido de futbol   :{futbol}')

#CUARENTA Y VEINTE 
#Verifiaca si una persona esta emtre sus 20,30 0 40. El programa le preguntara la edad y posteriormente 
#le repondera en que estapa de su vida esta


#IF SIRVE PARA EVALUAR UNA CONDICION Y EJECUTARLO SI ESTA SE CUMPLE ESTA
#EN PYTHON ELIF SE UTILIZAR PARA RELIZAR MULTIPLES CONDICIONES 

edad = int(input('Escribe tu edad'))

if edad >= 20 and edad < 30  :
    print('estas en la etapa de tus 20')
elif edad >= 30 and edad <40 :
    print('estas en la etapa de tus 30')
elif edad >= 40 and edad <50 :
    print('estas en la etapa de los 40')
else : 
    print('estas en otra etapa')
    
    
    
    
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