import os
import pygame as pg
import random as rd
import modulos.variables as var
import modulos.auxiliar as aux
import modulos.frases as fra
import modulos.carta as carta
import modulos.jugador as jugador_humano
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

    nivel_data['coords_iniciales_enemigo'] = (50,340)
    nivel_data['coords_finales_enemigo'] = (230,40)

    nivel_data['coords_iniciales_jugador'] = (20,370)
    nivel_data['coords_finales_jugador'] = (20,370)

    nivel_data['enemigo'] = participante.inicializaar_participante(nivel_data.get('screen'), 'Enemigo')
    participante.setear_stat_participante(nivel_data.get('enemigo'), 'pos_deck_inicial', nivel_data.get('coords_iniciales_enemigo'))
    participante.setear_stat_participante(nivel_data.get('enemigo'), 'pos_deck_jugado', nivel_data.get('coords_finales_enemigo'))

    participante.setear_stat_participante(nivel_data.get('jugador'), 'pos_deck_inicial', nivel_data.get('coords_iniciales_jugador'))
    participante.setear_stat_participante(nivel_data.get('jugador'), 'pos_deck_jugado', nivel_data.get('coords_finales_jugador'))

    nivel_data['cantidad_cartas_jugadores'] = 0

    nivel_data['juego_finalizado'] = False
    nivel_data['puntaje_guardado'] = False
    nivel_data['level_timer'] = var.level_timer
    nivel_data['ganador'] = None

    nivel_data['puntaje_nivel'] = 0
    nivel_data['data_cargada'] = False

    return nivel_data

def inicializar_data_nivel(nivel_data: dict):
    cargar_configs_nivel(nivel_data)
    cargar_bd_cartas(nivel_data)
    generar_mazo(nivel_data)
    barajar_mazos_nivel(nivel_data)

# print("DEBUG 1 — cartas_mazo_juego:", nivel_data.get('cartas_mazo_juego'))
# print("DEBUG 2 — cartas_mazo_preparadas:", nivel_data.get('cartas_mazo_preparadas'))
# print("DEBUG 3 — cartas_asignadas ANTES:", participante.get('cartas_asignadas'))

def cargar_configs_nivel(nivel_data: dict):
    if not nivel_data.get('juego_finalizado') and not nivel_data.get('data_cargada'):
        print('=============== CARGANDO CONFIGS INICIALES ===============')
        configs_globales= aux.cargar_configs(var.RUTA_CONFIGS_JSON)
        nivel_data['configs'] = configs_globales.get(f'nivel_{nivel_data.get("num_nivel")}')
        nivel_data['ruta_mazo'] = nivel_data.get('configs').get('ruta_mazo')
        nivel_data['coords_iniciales_enemigo'] = nivel_data.get('configs').get('coordenadas_mazo_1')
        nivel_data['coords_iniciales_jugador'] = nivel_data.get('configs').get('coordenadas_mazo_2')
        nivel_data['cantidad_cartas_jugadores'] = nivel_data.get('configs').get('cantidad_cartas_jugadores')

def cargar_bd_cartas(nivel_data: dict):
    if not nivel_data.get('juego_finalizado'):
        if os.path.exists(var.JSON_INFO_CARDS) and os.path.isfile(var.JSON_INFO_CARDS):
            print('=============== GENERANDO BD CARTAS INICIALES DESDE FILE ===============')
            nivel_data['cartas_mazo_juego'] = aux.cargar_configs(var.JSON_INFO_CARDS)
        else:
            print('=============== GENERANDO BD CARTAS INICIALES DESDE DIR ===============')
            nivel_data['cartas_mazo_juego'] = aux.generar_bd(nivel_data.get('ruta_mazo')).get('cartas').get('E:/UTN/UTN/Segundo cuatrimestre/Programacion I/assets_Dragon_Ball_Trading_Card_Game/assets_Dragon_Ball_Trading_Card_Game/PYGAME/assets/decks/blue_deck_expansion_1')

def generar_mazo(nivel_data: dict): 
    print('=============== GENERANDO MAZO FINAL ===============')
    # lista_mazo_original = nivel_data.get('cartas_mazo_juego')
    # nivel_data['cartas_mazo_juego_final'] = []

    for cartas in nivel_data['cartas_mazo_juego']['cartas']['assets/decks/blue_deck_expansion_1']:
        
        carta_final = carta.inicializar_carta(cartas, (395,450))
        nivel_data.get('cartas_mazo_preparadas').append(carta_final)
        # nivel_data.get('cartas_mazo_juego_final').append(carta_final)


    # nivel_data['cartas_mazo_juego_final'] = nivel_data['cartas_mazo_juego_final'][:10]

    # rd.shuffle(nivel_data.get('cartas_mazo_juego_final'))

def asignar_cartas_stage(nivel_data: dict, participante: dict):
    rd.shuffle(nivel_data.get('cartas_mazo_preparadas'))
    cantidad_cartas = nivel_data.get('cantidad_cartas_jugadores')
    cartas_panticipante = rd.sample(nivel_data.get('cartas_mazo_preparadas'), cantidad_cartas)
    participante['cartas_asignadas'] = cartas_panticipante

def barajar_mazos_nivel(nivel_data: dict): 
    if not nivel_data.get('juego_finalizado'):
        asignar_cartas_stage(nivel_data, nivel_data.get('jugador'))
        asignar_cartas_stage(nivel_data, nivel_data.get('enemigo'))

    participante.asignar_stats_iniciales_participante(nivel_data.get('jugador'))
    participante.asignar_stats_iniciales_participante(nivel_data.get('enemigo'))


def eventos(nivel_data: dict, cola_eventos: list[pg.event.Event]):
    for evento in cola_eventos:
        if evento.type == pg.MOUSEBUTTONDOWN:
            
            if nivel_data.get('cartas_mazo_juego_final') and nivel_data.get('cartas_mazo_juego_final')[-1].get('rect').collidepoint(evento.pos) and not nivel_data.get('cartas_mazo_juego_final')[-1].get('visible'):
                carta.asignar_coordenadas_carta(nivel_data.get('cartas_mazo_juego_final')[-1], nivel_data.get('coords_finales'))
                carta.cambiar_visibilidad_carta(nivel_data.get('cartas_mazo_juego_final')[-1])

                carta_vista = nivel_data.get('cartas_mazo_juego_final').pop()
                nivel_data.get('cartas_mazo_juego_final_vistas').append(carta_vista)
                
                carta_actual = nivel_data.get('cartas_mazo_juego_final_vistas')[-1]
                jugador_humano.sumar_puntaje_carta_actual(nivel_data.get('jugador'), carta_actual)

                print(f'puntaje act: {jugador_humano.get_puntaje_actual(nivel_data["jugador"])}')

                print(f'frase actual: {nivel_data.get('cartas_mazo_juego_final_vistas')[-1].get('frase')}')

def tiempo_esta_terminado(nivel_data: dict):
    return nivel_data.get('level_timer') <= 0

def mazo_esta_vacio(nivel_data: dict):
    return len(nivel_data.get('cartas_mazo_juego_final')) == 0 

def check_juego_terminado(nivel_data: dict):
    if mazo_esta_vacio(nivel_data) or tiempo_esta_terminado(nivel_data):
        nivel_data['juego_finalizado'] = True

def reiniciar_nivel(nivel_cartas: dict, jugador: dict, pantalla: pg.Surface, num_nivel: int):
    print('=============== REINICIANDO NIVEL ===============')
    nivel_cartas = inicializar_nivel_cartas(jugador, pantalla, num_nivel)
    participante.reiniciar_datos_participante(jugador)
    inicializar_data_nivel(nivel_cartas)    
    return nivel_cartas

def juego_terminado(nivel_data: dict):
    nivel_data['juego_finalizado'] = False

def jugar_mano_stage(nivel_data):
    participante.jugar_carta(nivel_data.get('jugador'))
    participante.jugar_carta(nivel_data.get('enemigo'))

def es_golpe_critico() -> bool:
    critical = rd.choice([False, False, False, True])
    return critical

def comparar_damage(nivel_data):
    ganador_mano = None
    jugador = nivel_data.get('jugador')
    enemigo = nivel_data.get('enemigo')

    carta_jugador = participante.get_carta_actual_participante(jugador)
    carta_enemigo = participante.get_carta_actual_participante(enemigo)

    if carta_enemigo and carta_jugador:
        critical = es_golpe_critico()
        atk_jugador = carta.get_atk_carta(carta_jugador)
        atk_enemigo = carta.get_atk_carta(carta_enemigo)

        if atk_enemigo > atk_jugador:
            ganador_mano = enemigo
            participante.restar_stats_participante(jugador, carta_enemigo, critical)
        else:
            ganador_mano = jugador
            participante.restar_stats_participante(enemigo, carta_jugador, critical)

    return ganador_mano

def chequear_ganador(nivel_data):
    jugador = nivel_data.get('jugador')
    enemigo = nivel_data.get('enemigo')

    if (participante.get_hp_participante(jugador) <= 0 or\
        participante.get_hp_participante(jugador) <= participante.get_hp_participante(enemigo)) and\
            len(participante.get_cartas_restantes_participante(enemigo)) == 0:
        nivel_data['ganador'] = enemigo
        nivel_data['juego_finalizado'] = True

    elif (participante.get_hp_participante(enemigo) <= 0 or\
        participante.get_hp_participante(enemigo) <= participante.get_hp_participante(jugador)) and\
            len(participante.get_cartas_restantes_participante(jugador)) == 0:
        nivel_data['ganador'] = jugador
        nivel_data['juego_finalizado'] = True

def jugar_mano(nivel_data:dict):
    jugar_mano_stage(nivel_data)

    ganador_mano = comparar_damage(nivel_data)
    chequear_ganador(nivel_data)
    return ganador_mano

def draw_jugadores(nivel_data: dict):
    participante.draw_participante(nivel_data.get('jugador'), nivel_data.get('screen'))
    participante.draw_participante(nivel_data.get('enemigo'), nivel_data.get('screen'))

    if nivel_data.get('cartas_mazo_juego_final_vistas'):
        carta.draw_carta(nivel_data.get('cartas_mazo_juego_final_vistas')[-1], nivel_data.get('screen'))

def update(nivel_data: dict, cola_eventos: list[pg.event.Event]):
    eventos(nivel_data, cola_eventos)
    check_juego_terminado(nivel_data)
    if juego_terminado(nivel_data) and not nivel_data.get('puntaje_guardado'): 
        jugador_humano.actualizar_puntaje_total(nivel_data['jugador'])
        # nombre_elegido = rd.choice(var.nombres)
        # jugador_humano.set_nombre(nivel_data.get("jugador"), nombre_elegido)
        # aux.guardar_ranking(nivel_data.get('jugador'))
        nivel_data['puntaje_guardado'] = True
        print(f'Puntos: {jugador_humano.get_puntaje_total(nivel_data.get('jugador'))}')
