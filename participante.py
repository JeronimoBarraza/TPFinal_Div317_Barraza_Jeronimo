import pygame as pg
import modulos.carta as carta
import modulos.nivel_cartas as nivel_cartas
import modulos.variables as var
import modulos.auxiliar as aux
from functools import reduce

def inicializaar_participante(pantalla: pg.Surface, nombre: str = 'PC'):
    participante = {}
    participante['nombre'] = nombre
    participante['hp_inicial'] = 1
    participante['hp_actual'] = 1
    participante['attack'] = 1
    participante['defense'] = 1
    participante['score'] = 0

    participante['cartas_asignadas'] = []
    participante['cartas_mazo'] = []
    participante['cartas_mazo_usadas'] = []
    
    participante['screen'] = pantalla
    participante['pos_deck_inicial'] = (200,250)
    participante['pos_deck_jugado'] = (300,400)
    
    return participante

def get_hp_inicial_participante(participante: dict):
    """ Retonarmos el hp inicial del participante en cuestión

    Args:
        participante (dict): Le pasamos el diccionario

    Returns:
        _type_: Retorna la hp inicial
    """
    return participante.get('hp_inicial')

def get_hp_participante(participante: dict):
    """ Retonarmos el hp actual del participante en cuestión

    Args:
        participante (dict): Le pasamos el diccionario

    Returns:
        _type_: Retorna la hp actual
    """
    return participante.get('hp_actual')

def get_attack_inicial_participante(participante: dict):
    """ Retonarmos el attack inicial del participante en cuestión

    Args:
        participante (dict): Le pasamos el diccionario

    Returns:
        _type_: Retorna el attack 
    """
    return participante.get('attack')

def get_defense_participante(participante: dict):
    """ Retonarmos la def del participante en cuestión

    Args:
        participante (dict): Le pasamos el diccionario

    Returns:
        _type_: Retorna la defensa
    """
    return participante.get('defense')

def get_nombre_participante(participante: str):
    """ Retonarmos el el nombre del participante

    Args:
        participante (dict): Le pasamos el diccionario

    Returns:
        _type_: Retorna el nombre
    """
    return participante.get('nombre')

def set_nombre_participante(participante: dict, nuevo_nombre: str):
    """ En esta función  el nombre del participante cuando haya finalizado le juego

    Args:
        participante (dict): Le pasamos el diccionario

    Returns:
        _type_: Retorna la hp
    """
    participante['nombre'] = nuevo_nombre

def get_cartas_iniciales_participante(participante: dict) -> list[dict]:
    """ Esta función crea el mazo del participante 
    Args:
        participante (dict): Le pasamos el diccionario

    Returns:
        list[dict]: Retornamos una lista del diccionario 
    """
    return participante.get('cartas_asignadas')

def get_cartas_restantes_participante(participante: dict) -> list[dict]:
    """ Esta función crea el mazo del participante 
    Args:
        participante (dict): Le pasamos el diccionario

    Returns:
        list[dict]: Retornamos una lista del diccionario 
    """
    return participante.get('cartas_mazo')

def get_cartas_jugadas_participante(participante: dict) -> list[dict]:
    """ Esta función crea el mazo del participante 
    Args:
        participante (dict): Le pasamos el diccionario

    Returns:
        list[dict]: Retornamos una lista del diccionario 
    """
    return participante.get('cartas_mazo_usadas')

def get_coordenadas_mazo_inicial(participante: dict):
    """En esta función asignamos las coordenadas del mazo en la posición inicial

    Args:
        participante (dict): Le pasamos el diccionario

    Returns:
        _type_: Retorna las coordenadas
    """
    return participante['pos_deck_inicial']

def get_coordenadas_mazo_jugado(participante: dict):
    """En esta función asignamos las cartas que fueron usadas
    Args:
        participante (dict): Le pasamos el diccionario
    Returns:
        _type_: Retornamos el mazo de las cartas ya jugadas
    """
    return participante['pos_deck_jugado']

def get_carta_actual_participante(participante: dict):
    """En esta función mostramos la última carta jugada del mazo
    Args:
        participante (dict): Le pasamos el diccionario
    Returns:
        _type_: Retorna la última carta del mazo
    """
    return participante.get('cartas_mazo_usadas')[-1]

def setear_stat_participante(participante: dict, stat: str, valor: int):
    participante[stat] = valor

def set_cartas_participante(participante: dict, lista_cartas: list[dict]):
    import copy

    cartas_copia = copy.deepcopy(lista_cartas)
    for carta_base in cartas_copia:
        carta_base['coordenadas'] = get_coordenadas_mazo_inicial(participante)  

    participante['cartas_asignadas'] = cartas_copia
    participante['cartas_mazo'] = cartas_copia.copy()

    print(f"Asignando {len(cartas_copia)} cartas a {participante['nombre']}")

def set_score_participante(participante: dict, score: int):
    """En esta función mostramos el score total del participante

    Args:
        participante (dict): El participante que juega
        score (int): El score total en entero
    """
    participante['score'] = score

def add_score_participante(participante: dict, score: int):
    participante['score'] += score

def asignar_stats_iniciales_participante(participante: dict):
    """En esta función asignamos la información de la carta inicial en el participante

    Args:
        participante (dict): Retornamos la información del hp_inicial, hp_actual, attack y defense
    """
    participante['hp_inicial'] = aux.reducir(carta.get_hp_carta, participante.get('cartas_asignadas'))
    participante['hp_actual'] = participante['hp_inicial']

    participante['attack'] = aux.reducir(carta.get_atk_carta,participante.get('cartas_asignadas'))
    participante['defense'] = aux.reducir(carta.get_def_carta,participante.get('cartas_asignadas'))

def chequear_valor_negativo(stat: int):
    """En esta función chequeamos que el valor del entero sea menor a 0

    Args:
        stat (int): Le pasamos el stat para chequear

    Returns:
        _type_: Retoranmos el valor 0 o en su defecto stat
    """
    if stat < 0:
        return 0
    else:
        return stat

def restar_stats_participante(participante: dict, carta_ganadora: dict, is_critico: bool):
    damage_mul = 1
    if is_critico:
        damage_mul = 2

    carta_jugador = participante.get('cartas_mazo_usadas')[-1]
    damage = carta.get_atk_carta(carta_ganadora) - carta.get_def_carta(carta_jugador)
    damage *= damage_mul

    participante['hp_actual'] = chequear_valor_negativo(participante.get('hp_actual') - damage)
    participante['attack'] -= carta.get_atk_carta(carta_jugador)
    participante['defense'] -= carta.get_def_carta(carta_jugador)

def jugar_carta(participante: dict):
    if participante.get('cartas_mazo'):
        print(f'El jugador {participante.get('nombre')} tiene {len(participante.get('cartas_mazo'))} cartas')
        carta_actual = participante.get('cartas_mazo').pop()

        participante.get('cartas_mazo_usadas').append(carta_actual)
        carta.cambiar_visibilidad_carta(carta_actual)
        carta.asignar_coordenadas_carta(carta_actual, participante['pos_deck_jugado'])
    else:
        print(f'El jugador {participante.get('nombre')} no tiene cartas')

def info_to_csv(participante: dict):
    return f'{get_nombre_participante(participante)},{participante.get('score')}\n'

def reiniciar_datos_participante(participante: dict):
    set_score_participante(participante, 0)

    participante['cartas_asignadas'] = []
    participante['cartas_mazo'] = []
    participante['cartas_mazo_usadas'] = []

    participante['hp_inicial'] = 0
    participante['hp_actual'] = 0
    participante['attack'] = 0
    participante['defense'] = 0
    
def draw_participante(participante: dict, screen: pg.Surface):
    if participante.get('cartas_mazo'):
        carta.draw_carta(participante.get('cartas_mazo')[-1], screen, participante['pos_deck_inicial'])

    if participante.get('cartas_mazo_usadas'): 
        carta.draw_carta(participante.get('cartas_mazo_usadas')[-1], screen, participante['pos_deck_jugado'])
