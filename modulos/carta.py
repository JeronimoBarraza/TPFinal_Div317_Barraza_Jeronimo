import pygame as pg
import random as rd
import os 
import modulos.auxiliar as aux

"""
"id": "assets/decks/blue_deck_expansion_1-['1', 'HP', '2450', 'ATK', '2950', 'DEF', '1650', '3.png']",
"atk": 2950,
"def": 1650,
"hp": 2450,
"path_imagen_frente": "assets/decks/blue_deck_expansion_1\\1_HP_2450_ATK_2950_DEF_1650_3.png",
"path_imagen_reverso": "assets/decks/blue_deck_expansion_1\\reverse.png"
"""

def inicializar_carta(carta_dict: dict, coordenadas: tuple[int, int]) -> dict:     
    carta_dict_final = {}
    carta_dict_final = carta_dict  
    carta_dict_final['id'] = carta_dict_final.get('id')
    carta_dict_final['nombre'] = carta_dict_final.get('nombre')
    carta_dict_final['coordenadas'] = coordenadas
    carta_dict_final['path_imagen_frente'] = carta_dict_final.get('path_imagen_frente')
    carta_dict_final['path_imagen_reverso'] = carta_dict_final.get('path_imagen_reverso')

    carta_dict_final['visible'] = False
    carta_dict_final['imagen'] = aux.achicar_imagen_card(carta_dict_final.get('path_imagen_frente'), 40)
    carta_dict_final['imagen_reverso'] = aux.achicar_imagen_card(carta_dict_final.get('path_imagen_reverso'), 40)

    carta_dict_final['rect'] = carta_dict_final.get('imagen').get_rect()
    carta_dict_final['rect'].x = coordenadas[0]
    carta_dict_final['rect'].y = coordenadas[1]

    carta_dict_final['rect_reverso'] = carta_dict_final.get('imagen_reverso').get_rect()
    carta_dict_final['rect_reverso'].x = coordenadas[0]
    carta_dict_final['rect_reverso'].y = coordenadas[1]

    return carta_dict_final

def draw_carta(card_data: dict, screen: pg.Surface):

    if card_data.get('visible'):
        screen.blit(card_data.get('imagen'), card_data.get('rect'))
    else:
        screen.blit(card_data.get('imagen_reverso'), card_data.get('rect_reverso'))

def get_puntaje_carta(card_dict: dict):
    return card_dict.get('puntaje')

def asignar_coordenadas_carta(carta_dict: dict, nueva_coordenada: tuple[int, int]):
    carta_dict['rect'].topleft = nueva_coordenada
    carta_dict['rect_reverso'].topleft = nueva_coordenada

def cambiar_visibilidad_carta(carta_dict: dict):
    carta_dict['visible'] = True

def get_hp_carta(carta_dict_final: dict):
    return carta_dict_final.get('hp')

def get_atk_carta(carta_dict_final: dict):
    return carta_dict_final.get('atk')

def get_def_carta(carta_dict_final: dict):
    return carta_dict_final.get('def')

def set_puntaje(card_dict: dict, puntaje: int):
    card_dict['puntaje'] = puntaje