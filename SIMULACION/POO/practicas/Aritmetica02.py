#Para pasar los datos dinamicos de unos inputs fuera de la clase estos se deben de llamar dentro de la clase
#los argumentos los recibe el constructor donde las funciones tomaran la instancia de estas 


#El constructor declarada y siempre el primero en definirlo en la clase 
class Aritmetica:
    def __init__(self,a,b,c):
        self.num1=a
        self.num2=b
        self.num3=c
    def suma (self):
        return self.num1 + self.num2 + self.num3
    def resta (self):
        return self.num1 - self.num2 -self.num3
    def multi (self):
        return self.num1 * self.num2
    def division (self):
        return self.num1 / self.num2
    def potencia (self):
        return self.num1 ** self.num2
objAritmetica = Aritmetica(1,2,3) 
print (objAritmetica.suma())
print (objAritmetica.resta())
print (objAritmetica.multi())
print (objAritmetica.division())
print (objAritmetica.potencia())




# class Aritmetica02: 
#     def __init__(self,a,b,c):
#         self.num1=a
#         self.num2=b
#         self.num3=c
#     def suma (self):
#         return self.num1+self.num2+self.num3
#     def resta (self):
#         return self.num1-self.num2-self.num3
# objAritmetica02= Aritmetica02(1,2,3)
# print(objAritmetica02.suma())
# print(objAritmetica02.resta())