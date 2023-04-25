#Calcular el area y perimetro de un rectangulo 
print ("ingresa la base :")
dato_base = int (input())


print("ingresa la altura :")
dato_altura = int(input())



area = dato_base * dato_altura
print ( F'el resultado del area es : {area}')

perimetro = (dato_base + dato_altura)*2
print ( F'el resultado del perimetro es : {perimetro}')