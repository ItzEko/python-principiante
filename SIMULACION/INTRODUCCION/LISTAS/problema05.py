#crear un vector de 5 elementos de cadenas de caracters, inicialice el vector con datos leidos osea ingresados
#y crear unnuevo vector que muestre los elementos del primer vector pero de orden inveso 

vector=[]
rango =int(input('ingresa el tamaño de la lista'))
while rango > 0:
     datos=input('ingresa las cadenas')
     vector.append(str(datos))
     rango-=1
vector.sort()
print('la lista ordena de manera descendente')
vector.sort(reverse=True)
print(vector)


