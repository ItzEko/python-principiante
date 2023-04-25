class Persona:
    #constructor = inicializa los atributos (variables)
    def __init__(self):
        #cuando se ejecute la clase por primera vez se va instanciar sus variables (propiedades)
        #self dice que la variable es de la clase osea la clase dice ("esto es mio")
        self.nombre='Itzel'
        self.apellido='Guzman'
    def Ficha (self):
        print(f'El nombre de la persona es :{self.nombre} {self.apellido}')
print(Persona)
#para acceder a una clase se necesita convertir a un objeto para acceder a sus variables 

#convertir una clase a objeto o INSTANCIAR UNA CLASE
objPersona = Persona()
print(objPersona.nombre)
print(objPersona.Ficha())
#INSTACIA= CONVERTIR UNA CLASE A OBJETO