# Una clase es un molde
#Declarando una clase(poner sus atributos y metodos)

class Heroe:
   #Constructor de la clase
   #Constructor = Función especial
   #el constructor es una función que permite inicializar los atributos
   def __init__(self,nombre,estatura,poder,tipoHeroe,cantidadVida):
        #Atributos=Propiedades=Datos
        #Variables = Atributos
        self.poder=poder
        self.estatura=estatura
        self.nombre=nombre
        self.tipoHeroe=tipoHeroe
        self.cantidadVida=cantidadVida
    #Metodos = Acciones = ¿Qué hace mi molde?
    #Funciones = Metodos
    #def saludar(self):
    #    print('Holaaa')

#Utilizando la clase=Crear una instancia= Crear un objeto
#Un objeto sin importar el lenguaje, es una variable, solo que es una variable especial
batman=Heroe('Bruce wayne', 1.90,500,'Heroe',100)
joker=Heroe('nn', 1.70,1200,'Villano',100)

#Con el objeto accedo a un atributo
print(batman.nombre)
print(joker.poder)


#Con el objeto, también puedo accedera a un metodo(Función)
#batman.saludar()