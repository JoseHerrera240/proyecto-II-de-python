from Ciclista import Ciclista
#El programa debe mostrar el ciclista con el mejor tiempo
ciclistas1 = Ciclista()
ciclistas2 = Ciclista()
opcion = 1
while (opcion !=0):
    print("Digitar 1 para Ingresar dos ciclistas (nombre,edad,pais y tiempo)")
    print("Digitar 2 para mostrar todos los ciclistas")
    print("Digitar 3 para mostrar al mejor tiempo")
    print(" Digitar 0 para SALIR")
    opcion=int(input("Digita una opcion: "))
    if(opcion == 0):
        break
    elif(opcion==1):

            nombre1=input("Digite el nombre del ciclista: ")
            edad1=int(input("Digite la edad del ciclista: "))
            pais1=input("Digite el pais del ciclista: ")
            tiempo1=int(input("Digite el tiempo que le tomó la prueba: "))
            ciclistas1.nombre=nombre1
            ciclistas1.edad=edad1
            ciclistas1.pais=pais1
            ciclistas1.tiempo=tiempo1

            nombre2=input("Digite el nombre del segundo ciclista ciclista: ")
            edad2=int(input("Digite la edad del segundo ciclista ciclista: "))
            pais2=input("Digite el pais del segundo ciclista ciclista: ")
            tiempo2=int(input("Digite el tiempo que le tomó la prueba al segundo ciclista: "))
            ciclistas2.nombre=nombre2
            ciclistas2.edad=edad2
            ciclistas2.pais=pais2
            ciclistas2.tiempo=tiempo2       
    elif(opcion==2):
        print(ciclistas1.nombre)
        print(ciclistas1.tiempo)
        print(ciclistas2.nombre)
        print(ciclistas2.tiempo)
    elif(opcion==3):
        primerTiempo = ciclistas1.tiempo
        segundoTiempo = ciclistas2.tiempo
        if(primerTiempo<segundoTiempo):
            print(ciclistas1.nombre)
            print(ciclistas1.edad)
            print(ciclistas1.pais)
            print(ciclistas1.tiempo)
        else:
            print(ciclistas2.nombre)
            print(ciclistas2.edad)
            print(ciclistas2.pais)
            print(ciclistas2.tiempo)

    else:
        print("el numero que ingresaste no esta en el menu")
