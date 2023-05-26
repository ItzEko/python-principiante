class Persona:
    def __init__(self):
        self.__id=''
        self.nombre=''
        self.apellido=''
        self.genero=''
        self.telefono=''
    def mostrarDatos(self,a,b,c,d,e):
        self.__id=a
        self.nombre=b
        self.apellido=c
        self.genero=d
        self.telefono=e
        idP=print(f'Id:{self.__id}')
        NombreCompleto =print(f'Nombre de la persona: {self.nombre} {self.apellido}')
        gen=print(f'genero: {self.genero}')
        tel=print(f'Telefono: {self.telefono}')
        return idP, NombreCompleto,gen, tel
