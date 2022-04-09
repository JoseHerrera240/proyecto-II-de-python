class Personaje:
    
    #Constructor
    def __init__(self):
        #Atributos
        self.__nombre = None
        self.__edad = None
    #metodos GET (Leer/obtener el valor de un atributo)
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad

    #METODOS SET (Escribir/ Ingresar / Llevar un valor a un atributo)
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @edad.setter
    def edad(self,edad):
        if (edad<0 ):
            print("No acepto edades negativas")
        else:
            self.__edad=edad
    