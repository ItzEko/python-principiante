#La clase siempre inicia con mayuscula 
class Aritmetica:
    def __init__(self):
        self.num1 =4
        self.num2 =4
    def suma (self):
        return self.num1 + self.num2
    def resta (self):
        return self.num1 - self.num2
    def multi (self):
        return self.num1 * self.num2
    def division (self):
        return self.num1 / self.num2
    def potencia (self):
        return self.num1 ** self.num2
# objAritmetica = Aritmetica() #instanciamos la clase y la convertimos a objeto
# print (objAritmetica.suma())
# print (objAritmetica.resta())
# print (objAritmetica.multi())
# print (objAritmetica.division())
# print (objAritmetica.potencia())