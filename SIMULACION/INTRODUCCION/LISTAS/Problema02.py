#Calificaciones 2 

calif=[]

for unidad in range(5):
    cal=float(input('ingresa la calificacion de la unidad:'))
    calif.append(cal) #la funcion append agrega un valor al final de la lista 
sumaa = sum(calif)
promed=sumaa/5
print(f'el promedio es {promed}')     































