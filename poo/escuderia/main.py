from Escuderia import Escuderia
#Construir programa que permita registrar 
# una escudería de F1 caracterizada por nombre, motor 
# (Mercedes/Ferrari/alfaRomero/Honda), piloto y costo anual

# Cree un Menú que permita:​
# -Ingresar escuderías​
# -Comprobar cual es la escudería más cara​
# -Comprobar cuantos escuderías tienen motor mercedes, cuantas Ferrari y cuantas alfaRomero
global lista
lista = list()

def registrarEscuderia():
    print("Registro de escuderías")
    a = Escuderia()
    a.nombreEscuderia = input("Ingrese El nombre de la escudería: ")
    a.motor =input("Ingrese la marca del motor: ")
    a.piloto = input("Ingrese el nombre del piloto: ")
    a.costoAnual = int(input("Ingrese el costo anual: "))
    lista.append(a)

def listar():
    print("Listando todos los ingresos")
    for a in lista:
        print(f"{a.nombreEscuderia} - {a.motor} - {a.piloto} - {a.costoAnual}")

def buscarMotor():
    print("Buscar por motor")
    filtro = input("Ingrese el motor a buscar: ")
    for a  in lista:
        if (a.motor == filtro):
            print(f"{a.motor} - {a.nombreEscuderia} - {a.costoAnual}")
    
def salir():
    print("Gracias por utilizar nuestro codigo")

def menu():
    opcion = 0
    salir = exit
    while (opcion != salir):
        print("Menu")
        print("Digitar 1 para Ingresar escuderias")
        print("Digitar 2 para mostrar los objetos")
        print("Digitar 3 para comprobar cuantos escuderías tienen motor mercedes, cuantas Ferrari y cuantas alfaRomero")
        print(" Digitar 4 para SALIR")
        opcion=int(input("Digita una opcion: "))
        if(opcion==1):
            registrarEscuderia()
        elif(opcion==2):
            listar()
        elif(opcion==3):
             buscarMotor()
        elif(opcion==4):
            salir()
        else:
            print("el numero que ingresaste no esta en el menu")

menu()
