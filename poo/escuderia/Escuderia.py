
class Escuderia:
    def __init__(self):
        self.__nombreEscuderia=None
        self.__motor=None
        self.__piloto=None
        self.__costoAnual=None
    
    @property
    def nombreEscuderia(self):
        return self.__nombreEscuderia
    @property
    def motor(self):
        return self.__motor
    @property
    def piloto(self):
        return self.__piloto
    @property
    def costoAnual(self):
        return self.__costoAnual
    
    @nombreEscuderia.setter
    def nombreEscuderia(self,nombreEscuderia):
        self.__nombreEscuderia=nombreEscuderia
    @motor.setter
    def motor(self,motor):
        self.__motor=motor
    @piloto.setter
    def piloto(self,piloto):
        self.__piloto=piloto
    @costoAnual.setter
    def costoAnual(self,costoAnual):
        self.__costoAnual=costoAnual
    