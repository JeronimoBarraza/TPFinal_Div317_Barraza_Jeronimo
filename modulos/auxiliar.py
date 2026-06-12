import pygame as pg
import json
import os
import random as rd
import modulos.variables as var
import modulos.forms.base_form as base_form

def parsear_entero(valor: str):
    if valor.isdigit():
        return int(valor)
    return valor

def mapear_valores(matriz: list[list], indice_a_aplicar: int, callback):
    for indice_fila in range(len(matriz)):
        valor = matriz[indice_fila][indice_a_aplicar]
        matriz[indice_fila][indice_a_aplicar] = callback(valor)

def cargar_ranking():
    ranking = []
    with open(var.RUTA_RANKING_CSV, 'r', encoding='utf-8') as file:
        lineas = file.read()
        for linea in lineas.split('\n'):
            if linea:
                ranking.append(linea.split(','))

    mapear_valores(ranking, 1, parsear_entero)
    ranking = ranking[3:]
    ranking.sort(key=lambda fila: fila[1], reverse=True)
    return ranking

def guardar_ranking(jugador_dict: dict):
    with open(var.RUTA_RANKING_CSV, 'a', encoding='utf-8') as file:
        data = f'{jugador_dict.get("nombre")},{jugador_dict.get("puntaje_actual")}\n'
        file.write(data)
        print(f'Datos guardados con éxito: - {data}')

def cargar_configs(path: str) -> dict:
    configuraciones = {}
    with open(path, 'r', encoding='utf-8') as file:
        configuraciones = json.load(file)
    return configuraciones

def cambiar_formulario_on_click(parametro: str):
    base_form.set_active(parametro)
    print(parametro)

def generar_bd(root_path_cards: str):
    carta_dict= {
        "cartas": {}
    }

    for root,dir, files in os.walk(root_path_cards, topdown=True):
        reverse_path = ''
        deck_cards = []
        deck_name = root.split('\\')[-1]

        for file in files:
            path_card = os.path.join(root, file)

            if 'reverse' in path_card:
                reverse_path = path_card
            else:
                file = file.replace('\\', '/')
                filename = file.split('/')[-1]
                datos = filename.split('_')

                card = {
                    "id": f'{deck_name}-{datos[0]}',
                    "atk": int(datos[4]),
                    "def": int(datos[6]),
                    "hp": int(datos[2]),
                    "path_imagen_frente": path_card
                }

                deck_cards.append(card)
        
        for index_card in range(len(deck_cards)):
            deck_cards[index_card]['path_imagen_reverso'] = reverse_path
        
        carta_dict['cartas'][deck_name] = deck_cards
    return carta_dict

def guardar_info_cartas(ruta_archivo: str, dict_cards: dict):
    with open(ruta_archivo, 'w', encoding='utf-8') as file:
        json.dump(dict_cards, file, indent=4)

def guardar_info_csv(informacion: str):
    with open(var.RUTA_RANKING_CSV, 'a', encoding='utf-8') as file:
        file.write(informacion)
        print(f'INFORMACION GUARDADA: - {informacion} ')

def achicar_imagen_card(path_imagen: str, porcentaje: int):
    imagen_raw = pg.image.load(path_imagen)
    alto = int(imagen_raw.get_height() * float(f'0.{porcentaje}'))
    ancho = int(imagen_raw.get_width() * float(f'0.{porcentaje}'))
    imagen_final = pg.transform.scale(imagen_raw, (ancho, alto))
    return imagen_final

def reducir(callback, iterable: list):
    suma = 0
    for elemento in iterable:
        suma += callback(elemento)
    return suma
    