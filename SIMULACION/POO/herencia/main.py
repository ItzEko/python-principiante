#IMPORTAMOS EL MODULO (ARCHIVO) Y SU CLASE
from Aritmetica import Aritmetica
from Poligonos import Poligonos

objAritmetica = Aritmetica()
print (objAritmetica.suma())
print (objAritmetica.resta())
print (objAritmetica.multi())
print (objAritmetica.division())
print (objAritmetica.potencia())

ObjPoligonos= Poligonos(2,2,10 )
print(f'el area del triangulo es {ObjPoligonos.AreaTriangulo()}')