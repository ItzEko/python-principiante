# LA UNICA MANERA QUE UNA CLASE MANDE DATOS A OTRA ES HACIENDO UNA INSTANCIA EN UN OBJETO Y HACIENDO CON FUNCIONES
class Persona:
    def __init__(self,nom,ape,ed):
        self.nombre=nom
        self._apellido=ape #hacemos vaiables protegidas
        self.__edad=ed      #variable privada
    def DetallesPersona(self): #ponemos que los datos entraran por self para que la funcion los pueda acceder
        print(f'Esta es una variable publica que es nombre:{self.nombre}')
        print(f'esta es una variable protegida que es apellido:{self._apellido}')
        print(f'esta es una variable publica que es edad: {self.__edad}')
obPersona=Persona('Itzel','Guzman',20) #instancia 
# print(obPersona.nombre)    #accedemos fuera de la clase 
# print(obPersona._apellido) #acedemos a la variable protegida fuera de la clase pero es mala practica
# print(obPersona.__edad)    #accedemos a la variable privada 
print(obPersona.DetallesPersona())
