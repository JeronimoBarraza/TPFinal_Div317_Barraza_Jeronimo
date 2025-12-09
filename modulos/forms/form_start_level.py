import pygame as pg
import sys
import modulos.forms.base_form as base_form
import modulos.nivel_cartas as nivel_cartas
import modulos.variables as var
import modulos.forms.form_bonus as form_bonus
from utn_fra.pygame_widgets import (
    Button, Label 
)

def init_form_start_level(dict_form_data: dict):

    form = base_form.create_base_form(dict_form_data)

    form['jugador'] = dict_form_data.get('jugador')
    form['actual_level'] = 1

    form['level'] = nivel_cartas.inicializar_nivel_cartas(form.get('jugador'), form.get('screen'), form.get('num_nivel'))
    
    form['clock'] = pg.time.Clock()
    form['bonus_1_used'] = False
    form['bonus_2_used'] = False
    form['first_last_timer'] = pg.time.get_ticks()

    nivel_data = nivel_cartas.inicializar_nivel_cartas(form['jugador'], form['screen'],form['level_number'] )
    dict_form_data['nivel'] = nivel_data
    
    form['lbl_clock'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=30, 
        text=f'TIME LEFT: {form.get("level").get("level_timer")}', 
        screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=45) 
     
    form['lbl_score'] = Label(
        x=75, y=35, text=f'SCORE: {form.get('jugador').get('puntaje_actual')}', 
        screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=45)    

    form['btn_bonus_1'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2 + 560, y=var.DIMENSION_PANTALLA[1] // 2 + 220,
        text='Shield', screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=40,
        color=var.COLOR_NEGRO, on_click=select_bonus, on_click_param={'form': form, 'bonus': 'X2'} 
    )

    form['btn_bonus_2'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2 + 560, y=var.DIMENSION_PANTALLA[1] // 2 + 270,
        text='Heal', screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=40,
        color=var.COLOR_NEGRO, on_click=select_bonus, on_click_param={'form': form, 'bonus': '+50'} 
    )

    form['btn_play'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2 + 560, y= var.DIMENSION_PANTALLA[1] // 2 + 30, 
        text="PLAY HAND",screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=35,
        on_click=jugar_mano, on_click_param=form
    )

    form['widgets_list'] = [
        form.get('lbl_clock'),
        form.get('lbl_score'), 
        form.get('btn_bonus_1'), 
        form.get('btn_bonus_2'), 
        form.get('btn_play')
    ] 

    base_form.forms_dict[dict_form_data.get('name')] = form
    return form

def select_bonus(form_y_bonus_name: dict):
    base_form.stop_music()
    base_form.play_music(base_form.forms_dict['form_bonus'])
    base_form.set_active('form_bonus')

    form_bonus.update_button_bonus(base_form.forms_dict['form_bonus'],form_y_bonus_name.get('bonus'))
    if form_y_bonus_name.get('bonus') == 'X2':
        form_y_bonus_name.get('form')['bonus_1_used'] = True
    else:
        form_y_bonus_name.get('form')['bonus_2_used'] = True

def jugar_mano(dict_form_data: dict):
    nivel = dict_form_data.get('level')
    ganador_mano = nivel_cartas.jugar_mano(nivel)
    print(f'El ganador de la mano es: {ganador_mano}')

def inicializar_nueva_partida(dict_form_data: dict):
    nivel = dict_form_data.get('level_number')
    jugador = dict_form_data.get('jugador')
    pantalla = dict_form_data.get('pantalla')
    dict_form_data['level_number'] = nivel_cartas.reiniciar_nivel(nivel_cartas=nivel, jugador=jugador, pantalla=pantalla, num_nivel=nivel.get('level_number'))
     
def actualizar_timer(dict_form_data: dict):
    if dict_form_data.get('level').get('level_timer') > 0:
        tiempo_actual = pg.time.get_ticks()
        
        if tiempo_actual - dict_form_data.get('first_last_timer') > 1000:
            dict_form_data.get('level')['level_timer'] -= 1
            dict_form_data['first_last_timer'] = tiempo_actual 

def events_handler(event_list: list[pg.event.Event]):
    for evento in event_list:
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_ESCAPE:
                base_form.set_active('form_pause')
                base_form.stop_music()
                base_form.play_music(base_form.forms_dict['form_pause'])

def draw(dict_form_data: dict):
    base_form.draw(dict_form_data)

    for widget_index in range(len(dict_form_data.get('widgets_list'))):
        if widget_index == 3 and dict_form_data.get('bonus_1_used') or widget_index == 4 and dict_form_data.get('bonus_2_used'):
            dict_form_data.get('widgets_list')[widget_index].draw()
    
    if 'nivel' not in dict_form_data or dict_form_data['nivel'] is None:
        nivel_data = nivel_cartas.inicializar_nivel_cartas(
            dict_form_data['jugador'], 
            dict_form_data['screen'], 
            dict_form_data['level_number']
        )
        dict_form_data['nivel'] = nivel_data

    nivel_cartas.draw_jugadores(dict_form_data.get('nivel'))

def update(dict_form_data: dict, cola_eventos: list[pg.event.Event]):
    base_form.update(dict_form_data)

    dict_form_data['lbl_clock'].update_text(f'TIME LEFT: {dict_form_data.get('level').get('level_timer')}', (255,0,0))
    dict_form_data['lbl_score'].update_text(f'SCORE: {dict_form_data.get('jugador').get('puntaje_actual')}', (255,0,0))

    for widget_index in range(len(dict_form_data.get('widgets_list'))):
        if widget_index == 3 and dict_form_data.get('bonus_1_used') or widget_index == 4 and dict_form_data.get('bonus_2_used'):
            continue
        dict_form_data.get('widgets_list')[widget_index].update()

    nivel_cartas.update(dict_form_data.get('level'), cola_eventos)
    
    mazo_vistas = dict_form_data.get('level').get('cartas_mazo_final_vistas')
    if mazo_vistas:
        dict_form_data['txp_info_card'].update_text(mazo_vistas[-1].get('frase'))
    dict_form_data['clock'].tick(var.FPS)
    actualizar_timer(dict_form_data)

    if nivel_cartas.juego_terminado(dict_form_data.get('level')):
        base_form.stop_music()
        base_form.play_music(base_form.forms_dict['form_enter_name'])
        base_form.set_active('form_enter_name')
    
    events_handler(cola_eventos)
