print("ingresa el mes y te dire la estacion del año")

estacion=input()

if estacion=="diciembre"or estacion=="enero"or estacion=="febrero"or estacion=="marzo":
    print("es invierno")
elif estacion=="abril" or estacion=="mayo" or estacion=="junio":
    print("es primavera")
elif estacion=="julio" or estacion=="agosto" or estacion=="septiembre":
    print("es verano")
elif estacion=="octubre" or estacion=="diciembre":
    print("es otoño")
else:
    print("no es valida la entrada ")