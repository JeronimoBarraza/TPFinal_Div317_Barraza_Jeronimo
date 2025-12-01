import pygame as pg
import os

# ------ PANTALLA --------

RATIO_SD = (854, 480)
RATIO_SDP = (800, 600)
RATIO_HD = (1280,720)
RATIO_FHD = (1920, 1080)
RATIO_UHD = (3840, 2160)

DIMENSION_PANTALLA = (RATIO_HD)

TITULO_JUEGO = 'Dragon Ball Z'

FPS = 60

# ------ FUENTES -------

pg.font.init()

RUTA_FUENTE = './modulos/forms/Halimount.otf'
FUENTE_HALIMOUNT = pg.font.Font(RUTA_FUENTE, 25)

FUENTE_ARIAL = pg.font.SysFont('Arial', 20)

pg.font.quit()
# ------- IMAGENES -------

IMAGEN_ICONO_JUEGO = 'E:/UTN/UTN/Segundo cuatrimestre/Programacion I/assets_Dragon_Ball_Trading_Card_Game/assets_Dragon_Ball_Trading_Card_Game/PYGAME/img/Z_star.png'

IMAGEN_MENU_PRINCIPAL = 'E:/UTN/UTN/Segundo cuatrimestre/Programacion I/assets_Dragon_Ball_Trading_Card_Game/assets_Dragon_Ball_Trading_Card_Game/PYGAME/img/img_5.png'

IMAGEN_RANKING = 'E:/UTN/UTN/Segundo cuatrimestre/Programacion I/assets_Dragon_Ball_Trading_Card_Game/assets_Dragon_Ball_Trading_Card_Game/PYGAME/img/img_8.png'

IMAGEN_OPTIONS = 'E:/UTN/UTN/Segundo cuatrimestre/Programacion I/assets_Dragon_Ball_Trading_Card_Game/assets_Dragon_Ball_Trading_Card_Game/PYGAME/img/img_6.png'

IMAGEN_CARTA = 'E:/UTN/UTN/Segundo cuatrimestre/Programacion I/assets_Dragon_Ball_Trading_Card_Game/assets_Dragon_Ball_Trading_Card_Game/PYGAME/img/background_cards.png'
# ------- VIDAS --------

CANTIDAD_VIDAS = 3

# ------- COLOR ---------

COLOR_NARANJA = (255, 85, 20)
COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)

# ------- ARCHIVOS --------

RUTA_RANKING_CSV = 'E:/UTN/UTN/Segundo cuatrimestre/Programacion I/assets_Dragon_Ball_Trading_Card_Game/assets_Dragon_Ball_Trading_Card_Game/PYGAME/ranking.csv'

RUTA_CONFIGS_JSON = 'E:/UTN/UTN/Segundo cuatrimestre/Programacion I/assets_Dragon_Ball_Trading_Card_Game/assets_Dragon_Ball_Trading_Card_Game/PYGAME/configs.json'

JSON_INFO_CARDS = 'E:/UTN/UTN/Segundo cuatrimestre/Programacion I/assets_Dragon_Ball_Trading_Card_Game/assets_Dragon_Ball_Trading_Card_Game/PYGAME/info_cartas.json'


# ------ COORDENADAS CARTAS -------

COORDENADA_MAZO_1 = (340,106)
COORDENADA_CARTA_VISTA = (690, 106)

# ------ TIEMPO CLOCK -------

level_timer = 25

nombres = [
    "Homero", "Zorro", "Ivan"
]

# ------ SONIDOS -----

pg.mixer.init()
RUTA_MUSICA_MENU = 'E:/UTN/UTN/Segundo cuatrimestre/Programacion I/assets_Dragon_Ball_Trading_Card_Game/assets_Dragon_Ball_Trading_Card_Game/PYGAME/assets/audio/ChalaHeadChala.mp3'
SOUND = pg.mixer.Sound(RUTA_MUSICA_MENU)