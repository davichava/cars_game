
class Carril:
    def __init__(self, nombre, carro) -> None:
        self.__nombre = nombre
        self.__carro = carro
        
    def get_nombre(self):
        return self.__nombre
    
    def get_carro(self):
        return self.__carro
