from persona import Persona
class Administrativos(Persona):
    def __init__(self,h,i):
        super().__init__()
        self.areaAcademica=h
        self.areaDependencia=i
    def mostrarDatosAdministrativos(self):
        infoPerson=self.mostrarDatos(12,'Itzel','Guzman','F','123456')
        infoAdminDepnd=print(f'Dependencia: {self.areaDependencia}')
        infoAdminArea=print(f'Area Academica: {self.areaAcademica}')
        return infoAdminArea, infoAdminDepnd
objPersona=Persona()
objAdministrativos=Administrativos('Ing.Forestal','none')
objAdministrativos.mostrarDatosAdministrativos()
