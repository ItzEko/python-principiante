# se puede hacer un codigo duro, tipado fuerte en una funcion

# def suma (a:int, b:float):
    
#Argumentos o parametros variables 
#Es decir como se reciben 10 0 100 valores, no hay longitud fija 
#para decirle a la funcion que no defina los datos que se ingresan, se ponen con un asterisco antes de los argumentos

def listaNombres (*argumentos):
    for valores in argumentos:
        print (valores)
listaNombres('itzel','Xiao','Deku')



rango=int(input('ingresa los numeros de nombres que quieres agregar -> '))
contador=0
while contador < rango:
    nombres=input('ingresa los nombres')
def lista01 (*nombres):
    for valores in nombres:
        print (valores)
lista01(nombres)


#sacar el factorial de un numero 
num=int(input('ingresa un numero y te dare su factorial -> '))
def factorial (num):
    inicio=1
    siguiente=1
    while inicio <= num:
        siguiente = siguiente * inicio
        inicio +=1
    print(f"el factorial de !{num} es igual a = {siguiente}")
factorial(num)
