# Un diccionario en Python es una estructura de datos que permite almacenar cualquier tipo de información, desde cadenas
# de texto o caracteres hasta números enteros, con decimales, listas e incluso otros diccionarios.

# Al igual que sucede con un diccionario de lengua, los datos se encuentran ordenados utilizando una clave única para 
# cada uno de ellos, lo que permite localizar cada uno de los datos de una forma muy rápida. 

# Los diccionarios Python son mutables, esto quiere decir/ que no tienen un tamaño predefinido y que su contenido 
# aumenta o disminuye según las necesidades de la aplicación. Todos los datos son también modificables, es decir, 
# se puede añadir, modificar, eliminar y consultar todos los datos de una manera sencilla y rápida.

# Ejemplos de diccionario de datos en Python
# Los valores de un diccionario se guardan utilizando un par de valores que siempre van enlazados. 

# Una es la denominadacomo Key o Clave, que es la que nos permite encontrar un dato dentro del diccionario. 
# Cada clave está acompañada por el dato o valor al que representa. Para entender fácilmente cómo funciona un 
# diccionario en Python vamos a ver algunos sencillos ejemplos.

# SINTAXIS
# diccionario = {}
# diccionario = dict()
# """

persona={'nombre' :'itzel','edad' :'20','estatura':1.67,'fechaNA':'09,08,02','direccion':{
    'calle':'principal','numero':'s/n'}}
print(persona)
#cuantos elementos hay en el diccionario
print(len(persona))
#Para imprimir una clave osea un elemento de un diccionario se pone la llave o clave el nombre que tiene asignado dentro del 
#diccionario
#acceder a un elemento por medio de la clave
print(persona['nombre'])
#FUNCION GET OBTIENE UN ELEMENTO
print(persona.get('edad'))
#SETTER MODIFICAR UN ELEMENTO 
persona['nombre'] = 'Teresa'
print(persona['nombre'])

#se le agrego un numero al valor de la llave y despues se obtuvo especificamente
persona['numero'] = '34'
print(persona.get('numero'))

#Agregar un nueva clave al diccionario se agrega hasta el final del diccionario
persona['sexo']='Fememnino'
print(persona)

#FUNCION POP: REMUEVE O ELIMINA UN ELEMENTO DEL DICCIONARIO 
persona.pop('sexo')
print(persona)

#FUNCION CLEAR: LIMPIA todo EL DICCIONARIO no lo elimina
# persona.clear()
# print(persona)

#SENTENCIA DEL: elimina todo el direccionario
# del persona
# print(persona)

#Iterar o recorrer un diccionario 
#por cada verdadero que este en persona se hace un recorrido
#una vez que for entra en persona lo obtiene y lo almacena en clave 
for clave in persona:
    print(f'los elementos que estan dentro de persona son: {clave}')
    
#FUNCION ITEMS(): ITERA O RRECORRE UN DICCIONARIO Y OBTIENE LA CLAVE  Y EL VALOR DEL OBJETO
for clave,valor in persona.items():
    print(f'persona clave {clave}-> {valor}')

#FUNCION KEYS():OBTIENE LA CLAVE DEL DICCIONARIO
for clave in persona.keys():
    print(f'persona clave {clave}') 
    
#FUNCION VALUES():OBTIENE EL VALOR DE LAS CLAVES DEL DICCIONARIO 
for valor in persona.values():
    print(f'persona valor {valor} funcion values()')

#FUNCION .GET() PARA OBTENER EL VALOR DE UNA LLAVE especificamente
print(persona.get('edad'))