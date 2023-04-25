# Factorial de un numero. El usuario debe de ingresar un numero y le tiene que regresar el factorial de ese numero

num = int(input("ingresa un numero cualquiera y te mostrare su factorial ->!"))
# debemos de inicializar las 2 variables
fact = 1
factorial = 1
# MIENTRAS QUE FACT SEA MENOR O IGUAL A NUM...(POR QUE VA MULTIPLICANDO HASTA LLEGAR A NUM)
while fact <= num:
    # FACT TOMARA EL VALOR DE 1,2,3,3..N
    # ENTONCES AL MULTIPLICARLO CON FACTORIAL QUE ESTE ESTA MULTIPLICANDO CON FACT Y TOMARA EL VALOR DE 1,2,3..
    # FACTORIAL VALE UNO Y MULTIPLICA A LA VARIABLE FACT QUE ESTA CUANDO TENGA UN VALOR DIFERENTE DE CERO ENTONCES SE MULTIPLICAN
    # Y FACTORIAL AGARRA EL VALOR DE FACT EJEMPLO: 1*2-> 2*3
    factorial = factorial*fact
    fact += 1
print(f"el factorial de !{num} es igual a = {factorial}")
