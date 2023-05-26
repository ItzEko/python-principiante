from persona import Persona
class Docente(Persona):
    def __init__(self,f,g):
        super().__init__()
        self.areaAcademica=f
        self.areaFormacion=g
    def mostrarDatosDocente(self):
        infoDocente=print(f'Area academica : {self.areaAcademica} , area formacion : {self.areaFormacion}')
        return infoDocente
objPersona=Persona()
objPersona.mostrarDatos(12,'Itzel','Guzman','F','123456')
objDocente=Docente('Ing.Sistemas Computacionales','Ing.Sistemas Computacionales')
objDocente.mostrarDatosDocente()
