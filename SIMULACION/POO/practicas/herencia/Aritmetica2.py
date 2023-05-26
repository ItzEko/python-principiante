# la clase aritmetica no es instanciada, ya no se reciben en el constructor los argumentos si no que se inicializan 
# ya que las van a recibir las funciones
class Aritmetica2:
    def __init__(self):
        self.num1=0
        self.num2=0
    def suma (self,a,b):
        self.num1=a
        self.num2=b
        return self.num1 + self.num2
    def resta (self,a,b):
        self.num1=a
        self.num2=b
        return self.num1 - self.num2
    def multi (self,a,b):
        self.num1=a
        self.num2=b
        mul=self.num1 * self.num2
        return mul
    def division (self,a,b):
        self.num1=a
        self.num2=b
        div= self.num1 / self.num2
        return div
    def potencia (self,a,b):
        self.num1=a
        self.num2=b
        return self.num1 ** self.num2