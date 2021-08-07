class Jugador:
    def __init__(self, nombre, victorias=0) -> None:
        self.__nombre = nombre
        self.__victorias = victorias

    def get_nombre(self):
        return self.__nombre

    def get_victorias(self):
        return self.__victorias
