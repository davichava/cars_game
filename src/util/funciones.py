from models.Carril import Carril
from models.Carro import Carro
from models.Conductor import Conductor
from models.Juego import Juego
from models.Jugador import Jugador
from models.Pista import Pista
from models.Podio import Podio

from database.conexion import DataBase

import time
import random


dataBase = DataBase()


def saludar():
    print('Bienvenido\n\n')


def crear_jugadores(numero_jugadores):
    array_jugadores = []
    for i in range(int(numero_jugadores)):
        nombre = input(f'Ingrese nombre del jugador {i+1}: ')
        jugador = Jugador(nombre.upper())
        array_jugadores.append(jugador)

    return array_jugadores


def capturar_numero_jugadores():
    return input('Ingrese número de jugadores: ')


def traer_indentificador_juego_nuevo():
    return dataBase.calcular_nuevo_indicador_juego()


def asignar_carros_a_conductores(array_jugadores):
    array_carros = []
    for jugador in array_jugadores:
        carro = Carro(jugador.get_nombre())
        array_carros.append(carro)

    return array_carros


def asignar_carril_a_carros(array_carros):
    array_carriles = []
    for i, carro in enumerate(array_carros, start=1):
        carril = Carril(f'carril_{i}', carro)
        array_carriles.append(carril)

    return array_carriles


def preparar_pista(array_carriles):
    distancia = input(f'Ingrese la distancia en km que tendrá la pista: ')
    pista = Pista(distancia, array_carriles)
    return pista


def presentacion_juego(identificador_juego):
    print('-------------------------------------------------------------\n\n')
    time.sleep(1)
    print(f'Inicia el juego # {identificador_juego}\n')
    time.sleep(1)


def presentacion_configuracion():
    print('-------------------------------------------------------------\n\n')
    time.sleep(1)
    print(f'Configuración del juego\n')
    time.sleep(1)


def tirar_dados():
    tirar = ''
    while tirar != 't' and tirar != 'T':
        tirar = input('Digita "t" para tirar los datos: ')
    return random.randint(1, 6)


def mostrar_posiciones(pista):
    for carril in pista.get_carriles():
        string = f'{carril.get_carro().get_conductor()} {carril.get_carro().get_metros_recorridos()} m '
        if carril.get_carro().get_en_meta():
            string += '- ya llegó'
        print(string)


def validar_posicion(metros_recorridos, meta):
    if int(metros_recorridos) >= int(meta)*1000:
        return True
    else:
        return False


def seguir_juando(pista):
    terminados = 0
    for carril in pista.get_carriles():
        if int(carril.get_carro().get_metros_recorridos()) >= int(pista.get_distancia())*1000:
            terminados += 1
    if terminados == len(pista.get_carriles()):
        return False
    else:
        return True


def actualizar_array_podio(carril, array_podio):
    if carril.get_carro().get_en_meta():
        array_podio.append(carril)
    return array_podio


def crear_podio(array_podio):
    podio = Podio(
        get_puesto_en_podio(array_podio, 0),
        get_puesto_en_podio(array_podio, 1),
        get_puesto_en_podio(array_podio, 2)
    )
    return podio


def get_puesto_en_podio(array_podio, puesto):
    try:
        return array_podio[puesto].get_carro().get_conductor()
    except:
        return '-'


def mostrar_podio(podio):
    time.sleep(1)
    print('############# PODIO #############\n')
    print(f'1ro\t{podio.get_primero()}\tCampeon!')
    print(f'2do\t{podio.get_segundo()}')
    print(f'3er\t{podio.get_tercero()}')
    print('\n###############################\n\n\n')


def preparar_juego_para_guardar(podio):
    return  Juego(podio)
    

def guardar_juego(juego):
    dataBase.save_juego(juego)

def guardar_campeon(juego):
    dataBase.save_campeon(juego)
    
def mostrar_contador_campeones():
    campeones = dataBase.get_campeones()
    array_jugadores = crear_jugadores_campeones(campeones)
    imprimir_campeones(array_jugadores)
    
    
def crear_jugadores_campeones(campeones):
    array_jugadores = []
    for campeon in campeones:
        jugador = Jugador(campeon['nombre'],campeon['victorias'])
        array_jugadores.append(jugador)
        
    return array_jugadores

def imprimir_campeones(array_jugadores):
    time.sleep(1)
    print('######################## Estadísticas ########################\n')
    print('Nombre\t\t\t\t\tVictorias')
    print('--------------------------------------------------------------')
    for jugador in array_jugadores:
        print(f"{jugador.get_nombre()}\t\t\t\t\t{jugador.get_victorias()}\n")
    print('##############################################################\n')
