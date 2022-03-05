#codigos prefabricados(Librerias)
import math
#Declaro el ciclo/bucle/iteración
print("empanadas el machetico")
print("****")
print("0.Digita 0 para salir")
print("1. Digita 1 para calcular la raiz cuadrada de un numero")
print("2. Digita 2 para calcular la potencia cuadrada de un #")
print("****")
opcion = 1
while(opcion != 0):
    #variable controladora
    opcion = int(input("dame una opción: "))

    #Pregunte por la opcion

    if(opcion ==0):
        break
    elif( opcion ==1):
        numero = int(input("digita un numero : "))
        if (numero > 0):
            raiz = math.sqrt(numero) 
            print(f"La raiz es {numero} es {raiz}")   
        else:
            print("El numero no puede ser negativo")

    elif(opcion == 2):
        numero = int(input("digita un numero : "))
        potencia = math.pow(numero,2) 
        print(f"La potencia es {numero} es {potencia}")  
    else:
        print("El menu que seleccionaste no esta crado")
    


