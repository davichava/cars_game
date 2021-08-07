from util.funciones import *
import time

# configurar juego
saludar()
presentacion_configuracion()
identificador_juego = traer_indentificador_juego_nuevo()
numero_jugadores = capturar_numero_jugadores()
array_jugadores = crear_jugadores(numero_jugadores)
array_carros = asignar_carros_a_conductores(array_jugadores)
array_carriles = asignar_carril_a_carros(array_carros)
pista = preparar_pista(array_carriles)

# iniciar_juego
presentacion_juego(identificador_juego)
jugando = True
array_podio = []
while jugando:
    for carril in pista.get_carriles():
        if not carril.get_carro().get_en_meta():
            print('-------------------------------------------------------------')
            print(
                f'Turno de {carril.get_carro().get_conductor()}, por {carril.get_nombre()}')
            time.sleep(1)
            resultado_dados = tirar_dados()
            time.sleep(1)
            print(f'\nDado = {resultado_dados}\n')
            time.sleep(1)
            carril.get_carro().set_metros_recorridos(resultado_dados)
            en_meta = validar_posicion(
                carril.get_carro().get_metros_recorridos(), 
                pista.get_distancia()
            )
            carril.get_carro().set_en_meta(en_meta)
            array_podio = actualizar_array_podio(carril, array_podio)
            mostrar_posiciones(pista)
            time.sleep(1)
            print(f'\nMeta {pista.get_distancia()} km\n')
            time.sleep(1)
            if not seguir_juando(pista):
                break
            
    jugando = seguir_juando(pista)

# guardar los resultados
podio = crear_podio(array_podio)
mostrar_podio(podio)
juego = preparar_juego_para_guardar(podio)
guardar_juego(juego)
guardar_campeon(juego)
mostrar_contador_campeones()
