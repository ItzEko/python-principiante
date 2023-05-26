class Persona:
    def __init__(self, nom, FechtNa, Yearna):
        self.__nombre=nom
        self.__fechaNacimiento=FechtNa
        self.__YearNacimiento=Yearna
    def _determinarEdad(self):
        calEdad=2023-self.__YearNacimiento
        return calEdad
    def Mostrar(self):
        edad=self._determinarEdad()
        print(f'Tu edad es {edad}')
        print(f'Tu nombre es {self.__nombre}')
        print(f'Tu fecha de nacimiento es {self.__fechaNacimiento}')
