# #funcion saludr
def saludar ():
    return ("hola este es un saludo")
print (saludar())


def saludo2 ():
    print('hola mundo')  
saludo2()

# #
def miNombreEs(name,apellido):
    print(f'My name is {name} {apellido}')
miNombreEs('Itzel','Guzman')

#funcion donde me regrese la suma de 2 valores 

def suma (a,b):
    resultado=a + b
    return resultado
print(suma(5,7))

a=int(input('ingresa numero'))
b=int(input('ingresa numero'))
def suma2 (a,b):
        resultado=a + b
        return resultado
print('el resultado es:',suma(a,b))

operacion=input('escoje la operacion que deseas : ')
a=float(input('ingresa numero'))
b=float(input('ingresa numero'))
if operacion =='suma':
    def suma2 (a,b):
        resultado=a + b
        return resultado
    print(suma2(a,b))
elif operacion=='resta':
    def resta(a,b):
        result=a-b
        return result
    print(resta(a,b))
elif operacion=='multiplicacion':
    def multiplicacion (a,b):
        result2=a*b
        return result2
    print(multiplicacion(a,b))
elif operacion=='division':
    def division (a,b):
        result3=a/b
        return result3
    print(division(a,b))

