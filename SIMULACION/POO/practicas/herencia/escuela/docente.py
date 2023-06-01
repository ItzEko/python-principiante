from persona import Persona
class Docente(Persona):
    def __init__(self,f,g):
        super().__init__()
        self.areaAcademica=f
        self.areaFormacion=g
    def mostrarDatosDocente(self):
        infoPerson=self.mostrarDatos(12,'Itzel','Guzman','F','123456')
        infoDocente=print(f'Area academica : {self.areaAcademica} , area formacion : {self.areaFormacion}')
        return infoDocente
objPersona=Persona()
objDocente=Docente('Ing.Sistemas Computacionales','Ing.Sistemas Computacionales')
objDocente.mostrarDatosDocente()
