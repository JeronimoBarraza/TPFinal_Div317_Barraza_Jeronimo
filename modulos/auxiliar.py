import pygame as pg
import json
import os
import random as rd
import modulos.variables as var
import modulos.forms.base_form as base_form

def crear_lista_botones(cantidad: int, dimension: tuple, color: str = 'black'):
    lista_botones = []

    for i in range(cantidad):

        boton = {}
        boton['superficie'] = pg.Surface(dimension)
        boton['rectangulo'] = boton.get('superficie').get_rect()
        boton['superficie'].fill(pg.Color(color))

        lista_botones.append(boton)
    return lista_botones


def mostrar_texto(surface: pg.Surface, texto: str, pos: tuple, font: str, color: str = 'white'):
    words = []

    for word in texto.splitlines():
        words.append(word.split(' '))

    space = font.size(' ')[0]
    ancho_max, alto_max = surface.get_size()
    x, y = pos

    for line in words:
        for word in words:
            word_surface = font.render('HISTORIA', False, color)
            ancho_palabra, alto_palabra = word_surface.get_size()

            if x + ancho_palabra >= ancho_max:
                x = pos[0]
                y += alto_palabra
            surface.blit(word_surface, (x,y))
            x += ancho_palabra + space
        x = pos[0]
        y += alto_palabra

def crear_cuadro(dimensiones: tuple, coordenadas: tuple, color: tuple) -> dict:
    cuadro = {}
    cuadro['superficie'] = pg.Surface(dimensiones)
    cuadro['rectangulo'] = cuadro.get('superficie').get_rect()
    cuadro['rectangulo'].topleft = coordenadas
    cuadro['superficie'].fill(pg.Color(color))
    return cuadro

def crear_boton(pantalla: pg.Surface, texto: str, ruta_fuente: str, dimensiones: tuple, coordenadas: tuple, color_fondo: tuple, color_texto: tuple):
    cuadro = crear_cuadro(dimensiones,coordenadas, color_fondo)
    cuadro['texto'] = texto
    cuadro['pantalla'] = pantalla
    cuadro['color_texto'] = color_texto
    cuadro['color_fondo'] = color_fondo
    cuadro['ruta_fuente'] = ruta_fuente
    cuadro['padding'] = (10,10)
    return cuadro


def mostrar_boton(boton_dict):
    mostrar_texto(
        boton_dict.get('superficie'),
        boton_dict.get('texto'),
        boton_dict.get('padding'),
        boton_dict.get('ruta_fuente'),
        boton_dict.get('color_texto')
    )

    boton_dict['rectangulo'] = boton_dict.get('pantalla').blit(
        boton_dict.get('superficie'), boton_dict.get('rectangulo').topleft
    )

    pg.draw.rect(boton_dict.get('pantalla'), boton_dict.get('color_fondo'), boton_dict.get('rectangulo'), 2)

def mostrar_texto_multilinea(superficie, texto: str, posicion, fuente, color):
    x, y = posicion
    for linea in texto.splitlines():  # divide por \n
        superficie_texto = fuente.render(linea, True, color)
        superficie.blit(superficie_texto, (x, y))
        y += superficie_texto.get_height() + 5  # 5 píxeles entre líneas

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
    ranking = ranking[5:]
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
    