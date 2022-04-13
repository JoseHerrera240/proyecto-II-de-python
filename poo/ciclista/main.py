from Ciclista import Ciclista

ciclistas1 = Ciclista()
ciclistas2 = Ciclista()
nombre1=input("Digite el nombre del ciclista: ")
edad1=int(input("Digite la edad del ciclista: "))
pais1=input("Digite el pais del ciclista: ")
tiempo1=int(input("Digite el tiempo que le tomó la prueba: "))
ciclistas1 = Ciclista.__nombre=nombre1
ciclistas1 = Ciclista.__edad=edad1
ciclistas1 = Ciclista.__pais=pais1
ciclistas1 = Ciclista.__tiempo=tiempo1
nombre2=input("Digite el nombre del segundo ciclista ciclista: ")
edad2=int(input("Digite la edad del segundo ciclista ciclista: "))
pais2=input("Digite el pais del segundo ciclista ciclista: ")
tiempo2=int(input("Digite el tiempo que le tomó la prueba al segundo ciclista: "))
ciclistas2 = Ciclista.__nombre=nombre2
ciclistas2 = Ciclista.__edad=edad2
ciclistas2 = Ciclista.__pais=pais2
ciclistas2 = Ciclista.__tiempo=tiempo2
# while (opcion !=0):
#     print("Digitar 1 para Ingresar un ciclista (nombre,edad,pais y tiempo):  ")
#     print("Digitar 2 para mostrar todos los ciclistas:  ")
#     print(" Digitar 0 para SALIR:  ")
#     opcion=int(input("Digita una opcion: "))
#     if(opcion == 0):
#         break
#     elif(opcion==1):
#             nombre1=input("Digite el nombre del ciclista: ")
#             edad1=int(input("Digite la edad del ciclista: "))
#             pais1=input("Digite el pais del ciclista: ")
#             tiempo1=int(input("Digite el tiempo que le tomó la prueba: "))
#             ciclista1 = Ciclista.nombre=nombre1
#             ciclista1 = Ciclista.edad=edad1
#             ciclista1 = Ciclista.pais=pais1
#             ciclista1 = Ciclista.tiempo=tiempo1
#             nombre2=input("Digite el nombre del segundo ciclista ciclista: ")
#             edad2=int(input("Digite la edad del segundo ciclista ciclista: "))
#             pais2=input("Digite el pais del segundo ciclista ciclista: ")
#             tiempo2=int(input("Digite el tiempo que le tomó la prueba al segundo ciclista: "))
#             ciclista2 = Ciclista.nombre=nombre2
#             ciclista2 = Ciclista.edad=edad2
#             ciclista2 = Ciclista.pais=pais2
#             ciclista2 = Ciclista.tiempo=tiempo2
#     # elif(opcion==2):
#     #     print(ciclistas1.nombre)
#     #     print(ciclistas1.tiempo)
#     #     print(ciclistas2.nombre)
#     #     print(ciclistas2.tiempo)
#     else:
#         print("el numero que ingresaste no esta en el menu")

print(ciclistas1.__nombre)
print(ciclistas1.__tiempo)
print(ciclistas2.__nombre)
print(ciclistas2.__tiempo)