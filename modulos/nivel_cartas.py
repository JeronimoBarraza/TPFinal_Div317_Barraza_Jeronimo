import os
import pygame as pg
import random as rd
import modulos.variables as var
import modulos.auxiliar as aux
import modulos.carta as carta
import participante as participante

def inicializar_nivel_cartas(jugador: dict, pantalla: pg.Surface, num_nivel: int):
    nivel_data = {}

    nivel_data['num_nivel'] = num_nivel
    nivel_data['configs'] = {}
    nivel_data['cartas_mazo_juego'] = []
    nivel_data['cartas_mazo_juego_final'] = []
    nivel_data['cartas_mazo_juego_final_vistas'] = []
    nivel_data['cartas_mazo_preparadas'] = []
    nivel_data['ruta_mazo'] = '' 
    nivel_data['screen'] = pantalla
    nivel_data['jugador'] = jugador

    nivel_data['lbl_heal_used'] = False
    nivel_data['lbl_shield_used'] = False

    nivel_data['heal_available'] = True
    nivel_data['shield_available'] = True
    
    nivel_data['enemigo'] = participante.inicializaar_participante(pantalla, nombre='enemigo')
    nivel_data['coords_iniciales_enemigo'] = (410,120)
    nivel_data['coords_finales_enemigo'] = (610,120)

    nivel_data['coords_iniciales_jugador'] = (410,450)
    nivel_data['coords_finales_jugador'] = (610,450)

    nivel_data['cantidad_cartas_jugadores'] = 10

    participante.setear_stat_participante(nivel_data['enemigo'], 'pos_deck_inicial', nivel_data['coords_iniciales_enemigo'])
    participante.setear_stat_participante(nivel_data['enemigo'], 'pos_deck_jugado', nivel_data['coords_finales_enemigo'])

    participante.setear_stat_participante(nivel_data['jugador'], 'pos_deck_inicial', nivel_data['coords_iniciales_jugador'])
    participante.setear_stat_participante(nivel_data['jugador'], 'pos_deck_jugado', nivel_data['coords_finales_jugador'])

    nivel_data['jugador']['pos_deck_inicial'] = nivel_data['coords_iniciales_jugador']
    nivel_data['jugador']['pos_deck_jugado'] = nivel_data['coords_finales_jugador']
    nivel_data['enemigo']['pos_deck_inicial'] = nivel_data['coords_iniciales_enemigo']
    nivel_data['enemigo']['pos_deck_jugado'] = nivel_data['coords_finales_enemigo']

    nivel_data['juego_finalizado'] = False
    nivel_data['puntaje_guardado'] = False
    nivel_data['ganador'] = None

    nivel_data['level_timer'] = var.level_timer
    nivel_data['first_last_timer'] = pg.time.get_ticks()
    nivel_data['puntaje_nivel'] = 0
    nivel_data['data_cargada'] = False

    return nivel_data

def modificar_estado_bonus(nivel_data: dict, bonus: str):
    nivel_data[f'{bonus}_available'] = False

    if bonus == 'HEAL':
        nivel_data['heal_available'] = False
        nivel_data['lbl_heal_used'] = True

    elif bonus == 'SCORE X3':
        nivel_data['shield_available'] = False
        nivel_data['lbl_shield_used'] = True

def actualizar_timer(nivel_data: dict):
    if nivel_data['level_timer'] > 0:
        tiempo_actual = pg.time.get_ticks()
        
        if tiempo_actual - nivel_data.get('first_last_timer') > 1000:
            nivel_data['level_timer'] -= 1
            nivel_data['first_last_timer'] = tiempo_actual 

def obtener_tiempo(nivel_data: dict):
    return nivel_data.get('level_timer')

def inicializar_data_nivel(nivel_data: dict):
    cargar_configs_nivel(nivel_data)
    cargar_bd_cartas(nivel_data)
    generar_mazo(nivel_data)
    barajar_mazos_nivel(nivel_data)

def cargar_configs_nivel(nivel_data: dict):
    if not nivel_data.get('juego_finalizado') and not nivel_data.get('data_cargada'):
        print("ANTES DEL FORM - enemigo mazo:", len(nivel_data['enemigo']['cartas_mazo']))
        print('=============== CARGANDO CONFIGS INICIALES ===============')
        configs_globales = aux.cargar_configs(var.RUTA_CONFIGS_JSON)
        nivel_data['configs'] = configs_globales.get(f'nivel_{nivel_data.get("num_nivel")}')
        nivel_data['ruta_mazo'] = nivel_data.get('configs').get('ruta_mazo')
        nivel_data['coords_iniciales_enemigo'] = nivel_data.get('configs').get('coordenadas_mazo_1')
        nivel_data['coords_iniciales_jugador'] = nivel_data.get('configs').get('coordenadas_mazo_2')
        nivel_data['cantidad_cartas_jugadores'] = nivel_data.get('configs').get('cantidad_cartas_jugadores')

def cargar_bd_cartas(nivel_data: dict):
    if not nivel_data.get('juego_finalizado'):
        if os.path.exists(var.JSON_INFO_CARDS) and os.path.isfile(var.JSON_INFO_CARDS):
            print('=============== GENERANDO BD CARTAS INICIALES DESDE FILE ===============')
            print("ENTRANDO FORM - enemigo mazo:", len(nivel_data['enemigo']['cartas_mazo']))
            nivel_data['cartas_mazo_juego'] = aux.cargar_configs(var.JSON_INFO_CARDS)
        else:
            print('=============== GENERANDO BD CARTAS INICIALES DESDE DIR ===============')
            bd = aux.generar_bd(nivel_data.get('ruta_mazo'))
            nivel_data['cartas_mazo_juego'] = {"cartas": bd["cartas"]}
  
def asignar_cartas_stage(nivel_data: dict, participantes: dict):
    
    rd.shuffle(nivel_data.get('cartas_mazo_preparadas'))
    cantidad_cartas = nivel_data.get('cantidad_cartas_jugadores')
    cartas_panticipante = rd.sample(nivel_data.get('cartas_mazo_preparadas'), cantidad_cartas)
    participante.set_cartas_participante(participantes,cartas_panticipante)
    
def generar_mazo(nivel_data: dict): 
    print('=============== GENERANDO MAZO FINAL ===============')

    if "cartas" in nivel_data["cartas_mazo_juego"]:
        mazo = nivel_data['cartas_mazo_juego']['cartas']['assets/decks/blue_deck_expansion_1']
    else:
        mazo = nivel_data['cartas_mazo_juego']['assets/decks/blue_deck_expansion_1']

    for cartas in mazo:
        carta_final = carta.inicializar_carta(cartas, (500,250))
        nivel_data['cartas_mazo_preparadas'].append(carta_final)

def barajar_mazos_nivel(nivel_data: dict): 
    if not nivel_data.get('juego_finalizado'):

        asignar_cartas_stage(nivel_data, nivel_data['jugador'])
        asignar_cartas_stage(nivel_data, nivel_data['enemigo'])

        participante.asignar_stats_iniciales_participante(nivel_data['jugador'])
        participante.asignar_stats_iniciales_participante(nivel_data['enemigo'])

        nivel_data['data_cargada'] = True

    print("Jugador mazo:", len(nivel_data['jugador']['cartas_mazo']))
    print("Enemigo mazo:", len(nivel_data['enemigo']['cartas_mazo']))

def hay_jugadores_con_cartas(nivel_data: dict):
    jugador_con_carta = participante.get_cartas_restantes_participante(nivel_data.get('jugador'))
    enemigo_con_carta = participante.get_cartas_restantes_participante(nivel_data.get('enemigo'))

    return jugador_con_carta or enemigo_con_carta

def reiniciar_nivel(jugador: dict, pantalla: pg.Surface, num_nivel: int):
    
    nivel_data = inicializar_nivel_cartas(jugador, pantalla, num_nivel)

    # NO volver a cargar mazo
    participante.reiniciar_datos_participante(nivel_data["jugador"])
    # participante.reiniciar_datos_participante(nivel_data["enemigo"])

    return nivel_data

def juego_terminado(nivel_data: dict):
    nivel_data['juego_finalizado'] = False

def jugar_mano_stage(nivel_data):
    participante.jugar_carta(nivel_data['jugador'])
    participante.jugar_carta(nivel_data['enemigo'])

def es_golpe_critico() -> bool:
    critical = rd.choice([False, False, False, True])
    return critical

def comparar_damage(nivel_data):
    ganador_mano = None
    jugador = nivel_data['jugador']
    enemigo = nivel_data['enemigo']
    critical = False

    carta_jugador = participante.get_carta_actual_participante(jugador)
    carta_enemigo = participante.get_carta_actual_participante(enemigo)

    if carta_enemigo and carta_jugador:
        critical = es_golpe_critico()
        atk_jugador = carta.get_atk_carta(carta_jugador)
        atk_enemigo = carta.get_atk_carta(carta_enemigo)

        if atk_enemigo > atk_jugador:
            ganador_mano = 'ENEMIGO'
            participante.restar_stats_participante(jugador, carta_enemigo, critical)
        else:
            score = atk_jugador - carta.get_def_carta(carta_enemigo)
            ganador_mano = 'JUGADOR'
            participante.restar_stats_participante(enemigo, carta_jugador, critical)
            participante.add_score_participante(jugador,score)

    return critical, ganador_mano

def setear_ganador(nivel_data: dict, participante_jugador: dict):
    puntaje_extra = nivel_data.get('level_timer')
    puntaje_actual = participante.get_score_participante(participante_jugador)
    participante.add_score_participante(participante_jugador, puntaje_extra)

    puntaje_nuevo = participante.get_score_participante(participante_jugador)

    print(f'Puntaje actual: {puntaje_actual} - Puntaje nuevo: {puntaje_nuevo}')

    nivel_data['ganador'] = participante_jugador
    nivel_data['juego_finalizado'] = True

def chequear_ganador(nivel_data):
    jugador = nivel_data['jugador']
    enemigo = nivel_data['enemigo']
    hay_tiempo_disponible = nivel_data.get('level_timer') > 0

    jugador_perdio = (participante.get_hp_porcent_participante(jugador) <= 0 or\
        (participante.get_hp_porcent_participante(jugador) < participante.get_hp_porcent_participante(enemigo)))
    
    enemigo_perdio = (participante.get_hp_porcent_participante(enemigo) <= 0 or\
        (participante.get_hp_porcent_participante(enemigo) <= participante.get_hp_porcent_participante(jugador)))
    
    enemigo_sin_cartas = len(participante.get_cartas_restantes_participante(enemigo)) == 0
    jugador_sin_cartas = len(participante.get_cartas_restantes_participante(jugador)) == 0

    if jugador_perdio and\
       (not hay_tiempo_disponible or\
        (hay_tiempo_disponible and jugador_sin_cartas)):
        setear_ganador(nivel_data, enemigo)

    elif enemigo_perdio and\
       (not hay_tiempo_disponible or\
        (hay_tiempo_disponible and enemigo_sin_cartas)):
        setear_ganador(nivel_data, jugador)

    elif hay_tiempo_disponible == 0:
        setear_ganador(nivel_data, enemigo)


def esta_finalizado(nivel_data: dict) -> bool:
    return nivel_data.get('juego_finalizado')

def obtner_ganador(nivel_data: dict) -> bool:
    return nivel_data.get('ganador')

def jugar_mano(nivel_data:dict):
    if not nivel_data.get('juego_finalizado'):
        jugar_mano_stage(nivel_data)

        critical, ganador_mano = comparar_damage(nivel_data)
        return critical, ganador_mano
    return None

def draw_jugadores(nivel_data: dict):
    # Dibujamos los participantes
    participante.draw_participante(nivel_data['jugador'], nivel_data['screen'])
    participante.draw_participante(nivel_data['enemigo'], nivel_data['screen'])
    
def update(nivel_data: dict):
    actualizar_timer(nivel_data)
    chequear_ganador(nivel_data)