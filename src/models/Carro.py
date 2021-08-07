
class Carro:
    def __init__(self, conductor):
        self.__metros_recorridos = 0
        self.__conductor = conductor
        self.__en_meta = False

    def get_metros_recorridos(self):
        return self.__metros_recorridos

    def set_metros_recorridos(self, metros):
        self.__metros_recorridos += metros*100

    def get_conductor(self):
        return self.__conductor

    def get_en_meta(self):
        return self.__en_meta

    def set_en_meta(self, en_meta):
        self.__en_meta = en_meta
