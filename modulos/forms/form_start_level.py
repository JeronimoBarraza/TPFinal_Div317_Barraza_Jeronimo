import pygame as pg
import modulos.forms.base_form as base_form
import modulos.nivel_cartas as nivel_cartas
import modulos.variables as var
import modulos.auxiliar as aux
import modulos.forms.form_enter_name as enter_name
import modulos.forms.form_bonus as form_bonus
import modulos.carta as carta_jugador
import participante as participante_juego
from utn_fra.pygame_widgets import (
    Button, Label, ImageLabel, ButtonImageSound
)

def init_form_start_level(dict_form_data: dict):

    form = base_form.create_base_form(dict_form_data)

    form['jugador'] = dict_form_data.get('jugador')

    form['actual_level'] = 1

    form['level'] = nivel_cartas.inicializar_nivel_cartas(form.get('jugador'), form.get('screen'), form.get('num_nivel'))
    
    form['clock'] = pg.time.Clock()
    form['bonus_1_used'] = False
    form['bonus_2_used'] = False
    

    # ============ LBLS ============ #
    
    form['lbl_clock'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=30, 
        text=f'TIME LEFT: {nivel_cartas.obtener_tiempo(form.get('level'))}',
        screen=form.get('screen'), font_path=var.FUENTE_HALIMOUNT, font_size=45, color=var.COLOR_BLANCO) 
     
    form['lbl_score'] = Label(
        x=105, y=35, text=f'Score: 0', 
        screen=form.get('screen'), font_path=var.FUENTE_HALIMOUNT, 
        font_size=45, color=var.COLOR_BLANCO)

    form['lbl_carta_e'] = Label(
        x=195, y=215, 
        text=f'', screen=form.get('screen'), 
        font_path=var.FUENTE_HALIMOUNT, font_size=20)
    
    form['lbl_carta_p'] = Label(
        x=195, y=550, 
        text=f'', screen=form.get('screen'), 
        font_path=var.FUENTE_HALIMOUNT, font_size=20)
    
    # ============ LBL ENEMIGO ============ #
    
    form['lbl_enemigo_hp'] = Label(
        x=175, y=190, 
        text=f'', screen=form.get('screen'), 
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    form['lbl_enemigo_atk'] = Label(
        x=135, y=230, 
        text=f'', screen=form.get('screen'), 
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    form['lbl_enemigo_def'] = Label(
        x=240, y=230, 
        text=f'', screen=form.get('screen'), 
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    # ============ LBL JUGADOR ============ #

    form['lbl_jugador_hp'] = Label(
        x=190, y=520, 
        text=f'', screen=form.get('screen'), 
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    form['lbl_jugador_atk'] = Label(
        x=140, y=555, 
        text=f'', screen=form.get('screen'), 
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    form['lbl_jugador_def'] = Label(
        x=240, y=555, 
        text=f'', screen=form.get('screen'), 
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    form['lbl_heal'] = ImageLabel(
        x=1130, y=175, text=f'', screen=form.get('screen'), 
        image_path=var.BOTON_ICON_HEAL, width=60, height=60,
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    # ============ BOTONES ============ #

    form['btn_bonus_1'] = ButtonImageSound(
        x=var.DIMENSION_PANTALLA[0] // 2 + 560, y=var.DIMENSION_PANTALLA[1] // 2 + 220,
        width=125, height=45,text='', screen=form.get('screen'), 
        image_path=dict_form_data.get('botones').get('shield'), sound_path=var.RUTA_SONIDO_CLICK,
        on_click=call_bonus_form, on_click_param={'form': form, 'bonus': 'SCORE X3'} 
    )

    form['btn_bonus_2'] = ButtonImageSound(
        x=var.DIMENSION_PANTALLA[0] // 2 + 560, y=var.DIMENSION_PANTALLA[1] // 2 + 270,
        width=125, height=45, text='', screen=form.get('screen'),
        image_path=dict_form_data.get('botones').get('heal'), sound_path=var.RUTA_SONIDO_CLICK,
        on_click=call_bonus_form, on_click_param={'form': form, 'bonus': 'HEAL'} 
    )

    form['btn_play'] = ButtonImageSound(
        x=var.DIMENSION_PANTALLA[0] // 2 + 560, 
        y=var.DIMENSION_PANTALLA[1] // 2 + 25, 
        width=130, height=55, text="", screen=form.get('screen'), 
        image_path=dict_form_data.get('botones').get('play_hand'), 
        sound_path=var.RUTA_SONIDO_CLICK,
        on_click=jugar_mano, on_click_param=form
    )

    form['widgets_list'] = [
        form.get('lbl_clock'),
        form.get('lbl_score'), 
        form.get('lbl_carta_e'), 
        form.get('lbl_carta_p'),
        form.get('lbl_enemigo_hp'), 
        form.get('lbl_enemigo_atk'), 
        form.get('lbl_enemigo_def'), 
        form.get('lbl_jugador_hp'), 
        form.get('lbl_jugador_atk'), 
        form.get('lbl_jugador_def'), 
        form.get('btn_play')
    ]

    form['widgets_list_bonus'] = [
        form.get('btn_bonus_1'), 
        form.get('btn_bonus_2')
    ]

    base_form.forms_dict[dict_form_data.get('name')] = form
    return form

def jugar_mano(dict_form_data: dict):
    nivel = dict_form_data.get('level')

    if nivel_cartas.hay_jugadores_con_cartas(nivel):
        critical, ganador_mano = nivel_cartas.jugar_mano(nivel)
        print(f'El ganador de la mano es: {ganador_mano}')

def verificar_terminado(dict_form_data: dict):
    nivel = dict_form_data.get('level')

    if nivel_cartas.esta_finalizado(nivel):
        nivel['juego_finalizado'] = True

        print('EL JUEGO ESTÁ TERMINADO')

        if participante_juego.get_nombre_participante(
            nivel_cartas.obtner_ganador(nivel)
        ) == 'enemigo':
            win_status = False
        else:
            win_status = True

        form_enter_name = base_form.forms_dict.get('form_enter_name')
        enter_name.update_texto_victoria(form_enter_name, win_status)
        base_form.set_active('form_enter_name') 

def call_bonus_form(params: dict):

    level = params['form'].get('level')
    level['lbl_heal_used'] = True
    level['heal_available'] = False
    
    dict_form_data = params.get('form')
    bonus_info = params.get('bonus')

    bonus_form = base_form.forms_dict.get('form_bonus')
    form_bonus.update_button_bonus(bonus_form, bonus_info)
    aux.cambiar_formulario_on_click('form_bonus')   

def inicializar_nueva_partida(dict_form_data: dict):
    nivel = dict_form_data.get('level')
    jugador = dict_form_data.get('jugador')
    pantalla = dict_form_data.get('pantalla')
    dict_form_data['level'] = nivel_cartas.reiniciar_nivel(nivel_cartas=nivel, jugador=jugador, pantalla=pantalla, num_nivel=nivel.get('level')) 

def events_handler(event_list: list[pg.event.Event]):
    for evento in event_list:
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_ESCAPE:
                base_form.set_active('form_pause')
                base_form.music_on(base_form.forms_dict['form_pause'])
                base_form.music_off(base_form.forms_dict['form_pause'])
        if evento.type == pg.MOUSEBUTTONDOWN:
            print(evento.pos)

def update_lbls_cards_info(dict_form_data: dict):
    mazo_enemigo = dict_form_data.get('level').get('enemigo').get('cartas_mazo_usadas')
    mazo_jugador = dict_form_data.get('level').get('jugador').get('cartas_mazo_usadas')

    if mazo_enemigo and mazo_jugador: 
        ultima_carta_j = participante_juego.get_carta_actual_participante(dict_form_data.get('level').get('jugador'))
        ultima_carta_e = participante_juego.get_carta_actual_participante(dict_form_data.get('level').get('enemigo'))

def update_lbls_participantes(dict_form_data: dict, tipo_participante: str):
    participante_enemigo = dict_form_data.get('level').get('enemigo')

    dict_form_data[f'lbl_enemigo_hp'].update_text(text=f'HP: {participante_juego.get_hp_participante(participante_enemigo)}', color=var.COLOR_BLANCO)
    dict_form_data[f'lbl_enemigo_atk'].update_text(text=f'ATK: {participante_juego.get_attack_inicial_participante(participante_enemigo)}', color=var.COLOR_BLANCO)
    dict_form_data[f'lbl_enemigo_def'].update_text(text=f'DEF: {participante_juego.get_defense_participante(participante_enemigo)}', color=var.COLOR_BLANCO)

    participante_jugador = dict_form_data.get('level').get('jugador')
    
    dict_form_data[f'lbl_jugador_hp'].update_text(text=f'HP: {participante_juego.get_hp_participante(participante_jugador)}', color=var.COLOR_BLANCO)
    dict_form_data[f'lbl_jugador_atk'].update_text(text=f'ATK: {participante_juego.get_attack_inicial_participante(participante_jugador)}', color=var.COLOR_BLANCO)
    dict_form_data[f'lbl_jugador_def'].update_text(text=f'DEF: {participante_juego.get_defense_participante(participante_jugador)}', color=var.COLOR_BLANCO)

def actualizar_puntaje(dict_form_data: dict):
    participante = dict_form_data.get('level').get('jugador')
    score = participante_juego.get_score_participante(participante)
    dict_form_data.get('lbl_score').update_text(text=f'Score: {score}', color=var.COLOR_BLANCO)   

def draw_bonus_widgets(dict_form_data: dict):
    widget_bonus = dict_form_data.get('widgets_list_bonus')
    level = dict_form_data.get('level')

    if level.get('heal_available'):
        widget_bonus[1].draw()
    if level.get('shield_available'):
        widget_bonus[0].draw()

def update_bonus_widgets(dict_form_data: dict):
    widget_bonus = dict_form_data.get('widgets_list_bonus')
    level = dict_form_data.get('level')

    if level.get('heal_available'):
        widget_bonus[1].update()
    if level.get('shield_available'):
        widget_bonus[0].update()

def draw_icon_heal(dict_form_data):
    level = dict_form_data.get('level')
    if level.get('lbl_heal_used'):
        dict_form_data.get('lbl_heal').draw()

def update_icon_heal(dict_form_data): 
    level = dict_form_data.get('level')
    if level.get('lbl_heal_used'):
        dict_form_data.get('lbl_heal').update([])

def draw(dict_form_data: dict):
    base_form.draw(dict_form_data)
    nivel_cartas.draw_jugadores(dict_form_data.get('level'))    
    base_form.draw_widgets(dict_form_data)
    draw_bonus_widgets(dict_form_data)
    draw_icon_heal(dict_form_data)

def update(dict_form_data: dict, cola_eventos: list[pg.event.Event]):
    dict_form_data['lbl_clock'].update_text(f'TIME LEFT: {nivel_cartas.obtener_tiempo(dict_form_data.get('level'))}', color=var.COLOR_BLANCO)
    base_form.update(dict_form_data)

    nivel_cartas.update(dict_form_data.get('level'))
    update_lbls_cards_info(dict_form_data)
    update_lbls_participantes(dict_form_data, tipo_participante='jugador')
    actualizar_puntaje(dict_form_data)
    update_lbls_participantes(dict_form_data, tipo_participante='enemigo')
    update_bonus_widgets(dict_form_data)
    update_icon_heal(dict_form_data)
    verificar_terminado(dict_form_data)
    
    events_handler(cola_eventos)
