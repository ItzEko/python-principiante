#OPERADORES FISICOS 

a = 10
b= 15
c= 20
#  >   "MAYOR QUE..."
#  <   "MENOR QUE..."
# ==   "IGUAL A..."
# >=   "MAYOR O IGUAL A..."
# <=   "MANOR O IGUAL A.."


resultado_and = ((a<b) and (b<c))
print (resultado_and)

#PARA QUE OR MUESTRE UN RESULTADO VERDADERO, BASTA CON QUE SOLO HAYA UN VALOR VERDADERO 
resultado_or = ((a>b) or (b<c))
print (resultado_or)

# el operador not niega la sentencia y si es verdadera nos saldra falso ; SI ES FALSA Y SE NIEGA MOSTRARA VERDADERO
#AQUI LA EXPRESION ME SALIA COMO RESULTADO VERDADERO PERO COMO LO ESTAMOS NEGANDO SALDRA FALSO
resultado_not = not ((a>b) or (b<c))
print (resultado_not)



#CALCULA EL AREA DE UN RECTANGULO 