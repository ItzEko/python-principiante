
class ConversionUnidades:
    def __init__(self,F,C,L,K,M,KM,Y,Metr):
        self.__Farenheit=F
        self.__Celcius=C
        self.__Libras=L
        self.__Kilos=K
        self.__Millas=M
        self.__Kilometros=KM
        self.__Yardas=Y
        self.__Metros=Metr
    def Farenheit_Celcius(self):
        cal= ( self.__Farenheit - 32) * 5/9
        print(f'Tus grados farenheit ->{self.__Farenheit} a celcius son -> {cal}')
    def Celius_Farenheit(self):
        cal= ( self.__Celcius-32)*1.8
        print(f'Tus grados celcius son ->{self.__Celcius} a Farenheit ->{cal}')
    def Libras_Kilos(self):
        cal = (self.__Libras / 2.205)
        print(f'Las libras {self.__Libras} a kilos son ->{cal}')
    def Kilos_Libras(self):
        cal= self.__Kilos * 2.205
        print(f'Los kilos son {self.__Kilos} a libras ->{cal}')
    def Millas_Kilometros(self):
        cal= self.__Millas * 1.609
        print(f'las millas son {self.__Millas} a kilometros ->{cal}')
    def Kilometros_Millas(self):
        cal= self.__Kilometros / 1.609
        print(f'kilometros son {self.__Kilometros} a millas ->{cal}')
    def yardas_metros(self):
        cal= self.__Yardas / 1.0936133
        print(f'las yardas son {self.__Yardas} a metros ->{cal}')
    def metros_yardas(self):
        cal=self.__Metros * 1.0936133
        print(f'los metros son {self.__Metros} a yardas ->{cal}')
    
        
objConversionUnidades=ConversionUnidades(23,34,21,56,45,67,12,14)
print(objConversionUnidades.Farenheit_Celcius())
print(objConversionUnidades.Celius_Farenheit())
print(objConversionUnidades.Libras_Kilos())
print(objConversionUnidades.Kilos_Libras())
print(objConversionUnidades.Millas_Kilometros())
print(objConversionUnidades.Kilometros_Millas())
print(objConversionUnidades.yardas_metros())
print(objConversionUnidades.metros_yardas())