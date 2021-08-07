
class Pista:
    def __init__(self,distancia,carriles) -> None:
        self.__distancia = distancia
        self.__carriles = carriles
        
    def get_distancia(self):
        return self.__distancia
    
    def get_carriles(self):
        return self.__carriles