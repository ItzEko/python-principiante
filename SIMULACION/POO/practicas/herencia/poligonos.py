from Aritmetica2 import Aritmetica2


class Poligono(Aritmetica2):
    def __init__(self,a,b,c):
        super().__init__()
        self.altura=a
        self.base=b
        self.radio=c
    def areaTriangulo(self):
        area=self.multi(self.altura,self.base)
        area2=self.division(area,2)
        return print(f'el area del triangulo es {area}')
    def areaRectangulo(self):
        area=self.multi(self.altura,self.base)
        return print(f'el area del rectangulo es {area}')
    def areaCirculo (self):
        area=self.multi(3.1416,self.radio)
        area2=self.potencia(area,2)
        return print(f'el area del circulo es {area2}')
objPoligono=Poligono(1,2,3)
objPoligono.areaTriangulo()
objPoligono.areaRectangulo()
objPoligono.areaCirculo()
