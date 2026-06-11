import os 
import pygame as pg
import random as rd
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

    return carta_dict_final

def asignar_coordenadas_carta(carta_dict_final: dict, nueva_coordenada: tuple[int, int]):
    carta_dict_final['coordenadas'] = nueva_coordenada

def cambiar_visibilidad_carta(carta_dict_final: dict):
    carta_dict_final['visible'] = True

def get_atk_carta(carta_dict_final: dict):
    return carta_dict_final.get('atk')

def get_def_carta(carta_dict_final: dict):
    return carta_dict_final.get('def')

def get_hp_carta(carta_dict_final: dict):
    return carta_dict_final.get('hp')

def draw_carta(carta_dict_final: dict, screen: pg.Surface, coordenadas: tuple):
    if carta_dict_final.get('visible'):
        carta_dict_final['imagen'] = aux.achicar_imagen_card(carta_dict_final.get('path_imagen_frente'), 40)
        carta_dict_final['rect'] = carta_dict_final.get('imagen').get_rect()
        carta_dict_final['rect'].x, carta_dict_final['rect'].y = coordenadas
        screen.blit(carta_dict_final['imagen'], carta_dict_final['rect'])
    else:
        carta_dict_final['imagen_reverso'] = aux.achicar_imagen_card(carta_dict_final.get('path_imagen_reverso'), 40)
        carta_dict_final['rect_reverso'] = carta_dict_final['imagen_reverso'].get_rect()
        carta_dict_final['rect_reverso'].topleft = coordenadas
        screen.blit(carta_dict_final['imagen_reverso'], carta_dict_final['rect_reverso'])