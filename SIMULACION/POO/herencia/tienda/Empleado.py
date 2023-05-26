class Empleado:
    def __init__(self, sueldo):
        self.__sueldoBruto= sueldo
    def salarioNeto(self):
        porcentaje=(self.__sueldoBruto * 10)/100
        retenciones=(self.__sueldoBruto - porcentaje)
        print(f'El sueldo neto es de :{retenciones}')
# objEmpleado = Empleado(3000)
# objEmpleado.salarioNeto()