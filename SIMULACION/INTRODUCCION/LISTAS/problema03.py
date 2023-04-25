# mayor y menor de una lista, encuantra dentro de un arreglo dinamico el mayor y el menor de ese rango de muneros

lista = []
mayor = 0
num_menor = 100

rango = int(input('ingresa el tamaño de la lista'))
for indice in range(rango):
    valores = int(input('ingresa valores a la lista'))
    lista.append(valores)
if mayor < valores:
        mayor = valores
if num_menor > valores:
    num_menor = valores
print(lista)
print(f'el numero mayor es :{mayor}')
print(f'el numero menor es:{num_menor}')