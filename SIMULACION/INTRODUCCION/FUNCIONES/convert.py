#funcion que convierta los grados celsius a Farenheit 
#otra funcion donde convierta los Farenheit a Celsisus 


grados=int(input('ingresa los grados celsius que quieres convertir a Farenheit -> '))
    
def farenheit(grados):
    F=(grados * 1.8) + 32
    print(f'los grados {grados}° en Farenheit son {F}°')
farenheit(grados)
    


grados2=int(input('ingresa los grados en Farenheit para convertilos a celsius-> '))
def celcius (grados):
    C=(grados2 - 32) /1.8
    print(f'los grados {grados2}° Farenheit son {C}° grados celsius')
celcius(grados2)
