#Ejemplo de estaciones
mes = input("digita un mes del año ").lower()
print(f"El mes digitado fue {mes}")
# caminos para clasificar el mes
if(mes == "diciembre" or mes == "enero" or mes == "febrero" or mes = "marzo"):
    print("Estas en invierno")
elif(mes == "junio" or mes == "julio" or mes == "agosto"):
    print("estas en verano")
elif(mes == "abril" or mes == "mayo"):
    print("Estas en primavera")
elif(mes == "septiembre" or mes == "octubre" or mes == "noviembre"):
    print ("estas en otoño")
else:
    print("Este mes no existe")
