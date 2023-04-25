#hacer una clase 
class Aritmetica:
    def __init__(self):
        self.num1 =2
        self.num2 =2
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
objAritmetica = Aritmetica()
print (objAritmetica.suma())
print (objAritmetica.resta())
print (objAritmetica.multi())
print (objAritmetica.division())
print (objAritmetica.potencia())