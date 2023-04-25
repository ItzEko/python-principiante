#QUE TABLA DESEAS DEPLEGAR Y LE VA PEDIR QUE INGRESE EL NUMERO DE LA TBLA QUE QUIERA DESPLEGAR 


num=int(input( "ingresa un numero de la tabla que quieres mostrar"))
num1=1

while num1<=10:
    result=num*num1
    print (f"la tabla del {num} es: {num}x{num1}={result}")
    num1+=1
    
