print ("Hello world!")


#operador de asignacion 
#un operador de asignacionves aquel que este a la derecha lo asigna a la izquierda

x = 'soy una cadena' 
print (x)

x = 1
print (x)

#Tarea de IMPRIMIR VALOR DE TIPO FLOTANTE Y BOOLEANO 

#TIPO DE DATO BOOLEANO (boolean)
print("TAREA IMPRIMIR UN NUMERO BOOLEANO Y UN FLOAT")
dato_booleano = 3 == 3
print (dato_booleano,type(dato_booleano))

dato_booleano_2 = 2 == 3
print (dato_booleano_2,type(dato_booleano_2))


#TIPO DE DATO FLOTANTE (float)
numero_flotante = 15.5 
print (numero_flotante,type(numero_flotante))


#CLASE DE PYTHON 
a = 2
print (a)

b = a 
print(b)

b= 45
print(b) 

#OPERADORES ARITMETICOS
print("OPERADORES ARITMETICOS")
suma = 1+2 
print (suma)

resta = 1-2
print (resta)

multiplicacion= 2*3
print (multiplicacion)

division= 2/2
print (division)

division_euclidiana= 5//5
print (division_euclidiana)



#OPERADORES RELACIONALES 
print("OPERADORES RELACIONALES :D")

a=2
b=3

Op_Relacional = a<b
print(F'El resultado es:{Op_Relacional}')

Op_Relacional2 = a <b 
print (F'El resultado 2 es:{Op_Relacional2}')

Op_Relacional3 = a>=b
print (F'El resultado 3 es:{Op_Relacional3}')

Op_Relacional4 = a <= b
print (F'El resultado 4 es:{Op_Relacional4}')

Op_Relacional5 = a == b
print (F'El resultado 5 es:{Op_Relacional5}')

Op_Relacional6 = a != b
print (F'El resultado 6 es:{Op_Relacional6}')










#OPERADORES LOGICOS
#AND  :  SI TODAS LAS CONDICIONES SON VERDADERAS EL RESULTADO DE LA EVALUACION SERA VERDADERO. SI ALGUNA DE LAS CONDICIONES ES FALSA EL RESULTADO SERA FALSO 
print("OPERADORES LOGICOs  :D")

c=2
#a
d= 2
#b
e=3
Op_logico = d==e and d==c
print(F'Operador logico AND :{Op_logico}')