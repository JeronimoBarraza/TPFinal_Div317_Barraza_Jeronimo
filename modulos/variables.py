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

FUENTE_HALIMOUNT = 'modulos/forms/Halimount.otf'

FUENTE_ARIAL = pg.font.SysFont('Arial', 20)

pg.font.quit()

# ------- IMAGENES -------

IMAGEN_ICONO_JUEGO = 'img/Z_star.png'
IMAGEN_BONUS = 'img/img_1.png'
IMAGEN_ENTER_NAME = 'img/img_3.jpg'
IMAGEN_MENU_PRINCIPAL = 'img/img_5.png'
IMAGEN_OPTIONS = 'img/img_6.png'
IMAGEN_RANKING = 'img/img_8.png'
IMAGEN_PAUSE = 'img/img_20.jpg'
IMAGEN_CARTA = 'img/background_cards.png'
IMAGEN_TUTORIAL = 'img/img_jugar_tutorial.png'
IMG_HEAL_TUTORIAL = 'img/img_heal_tutorial.png'
IMG_SHIELD_TUTORIAL = 'img/img_test.jpg'
IMG_SCORE_TUTORIAL = 'img/img_timer_tutorial.png'
IMG_TIMER_TUTORIAL = 'img/img_score_tutorial.jpg'
IMG_RANKING_TUTORIAL = 'img/fondo_tutorial_2.png'

# ------- VIDAS --------

CANTIDAD_VIDAS = 3

# ------- COLOR ---------

COLOR_NARANJA = (255, 85, 20)
COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)

# ------- ARCHIVOS --------

RUTA_RANKING_CSV = 'ranking.csv'
RUTA_CONFIGS_JSON = 'configs.json'
JSON_INFO_CARDS = 'info_cartas.json'

# ------ COORDENADAS CARTAS -------

COORDENADA_MAZO_1 = (340,106)
COORDENADA_CARTA_VISTA = (690, 106)

# ------ TIEMPO CLOCK -------

level_timer = 105

nombres = [
    "Homero", "Zorro", "Ivan"
]

# ------ SONIDOS -----

pg.mixer.init()

RUTA_MUSICA_MENU = 'assets/audio/ChalaHeadChala.mp3'
SOUND = pg.mixer.Sound(RUTA_MUSICA_MENU)
RUTA_SONIDO_CLICK = 'assets/audio/click.mp3'

# ------ BOTONES ------

BOTON_JUGAR = 'img/button/btn_jugar.png'
BOTON_HISTORIA = 'img/button/btn_opciones.png'
BOTON_RANKING = 'img/button/btn_ranking.png'
BOTON_SALIR = 'img/button/btn_salir.png'
BOTON_VOLVER = 'img/button/btn_volver.png'
BOTON_PLAYHAND = 'img/button/btn_play_hand.png'
BOTON_SHIELD = 'img/button/shield.png'
BOTON_HEAL= 'img/button/heal.png'

# ------ BOTONES ICON ------

BOTON_ICON_HEAL = 'img/button/icon_heal.png'
BOTON_ICON_SHIELD = 'img/button/icon_shield.png'

# ------ BOTONES TUTO ------

IMAGEN_SCORE_TUTORIAL = 'img/score.png'
IMAGEN_TIMER_TUTORIAL = 'img/timer.png'