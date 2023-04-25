#Clase dinamica de areas de figuras geometricas 
class Poligonos:
    def __init__(self,base,altura,radio):
        self.base1=base
        self.altura1=altura
        self.radio1=radio
    def AreaRectangulo(self):
        return self.base1 * self.altura1
    def AreaTriangulo(self):
        return (self.base1 * self.altura1) /2
    def AreaCirculo(self):
        return 3.1416*self.radio1**2
ObjPoligonos= Poligonos(3,2,5)
print(f'el area del rectangulo es {ObjPoligonos.AreaRectangulo()}')
print(f'el area del triangulo es {ObjPoligonos.AreaTriangulo()}')
print(f'el area del circulo es {ObjPoligonos.AreaCirculo()}')