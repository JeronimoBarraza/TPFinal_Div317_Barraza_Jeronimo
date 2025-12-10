import pygame as pg
import modulos.auxiliar as aux
import modulos.forms.base_form as base_form
import modulos.variables as var
import modulos.jugador as jugador_mod
import modulos.forms.form_start_level as form_start_level
import modulos.nivel_cartas as nivel_cartas
import participante as participante
from utn_fra.pygame_widgets import (
    Button, Label
)

def init_form_bonus(dict_form_data: dict, jugador: dict):
    form = base_form.create_base_form(dict_form_data)   
    form['jugador'] = jugador

    form['bonus_info'] = ''

    form['title'] = Label (
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 250, 
        text=var.TITULO_JUEGO, screen=form.get('screen'), 
        font_path=var.RUTA_FUENTE, font_size=70, color=var.COLOR_BLANCO
    )

    form['subtitle'] = Label (
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 170, 
        text='SELECCIONA UN BONUS', screen=form.get('screen'), 
        font_path=var.RUTA_FUENTE, font_size=50, color=var.COLOR_BLANCO
    )

    form['btn_select'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y= var.DIMENSION_PANTALLA[1] // 2, 
        text=form.get('bonus_info'),screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=25, color=var.COLOR_NEGRO,
        on_click=click_select_bonus, on_click_param=form
    )

    form['btn_back'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y= var.DIMENSION_PANTALLA[1] // 2 + 250, 
        text="CANCELAR",screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=25, color=var.COLOR_NEGRO,
        on_click=click_change_form, on_click_param='form_start_level'
    )

    form['widgets_list'] = [
        form.get('title'), form.get('subtitle'), form.get('btn_select'), form.get('btn_back')
    ]

    base_form.forms_dict[dict_form_data.get('name')] = form
    return form

def click_change_form(form_enter_name: str):
    aux.cambiar_formulario_on_click(form_enter_name)
    # base_form.stop_music()
    # base_form.play_music(base_form.forms_dict[param])

def click_select_bonus(dict_form_data: dict):
    bonus_info = dict_form_data.get('bonus_info')
    jugador = dict_form_data.get('jugador')

    start_level_form = aux.base_form.forms_dict['form_start_level']
    level = start_level_form.get('level')

    if bonus_info == 'HEAL':
        bonus = 'heal'
    else:
        bonus = 'shield'

    nivel_cartas.modificar_estado_bonus(level, bonus)

    if bonus_info == 'SCORE X3':
        anterior_puntaje = participante.get_score_participante(jugador)
        nuevo_puntaje = anterior_puntaje * 3

        print(f'ANTERIOR SCORE: {anterior_puntaje} | ACTUAL SCORE: {nuevo_puntaje}')
        participante.set_score_participante(jugador, nuevo_puntaje)

    else:
        hp_inicial = participante.get_hp_inicial_participante(jugador)
        hp_actual = participante.get_hp_participante(jugador)
        hp_perdida = hp_inicial - hp_actual

        hp_bonus = int(hp_perdida * 0.75)
        hp_nuevo = hp_actual + hp_bonus

        print(f'ANTERIOR HP: {hp_actual} | ACTUAL HP: {hp_nuevo}')
        participante.set_hp_participante(jugador, hp_nuevo)

    # reproducir sonido de bonus 
    pg.time.wait(2000)
    click_change_form('form_start_level')
 
def update_button_bonus(dict_form_data: dict, bonus_info: str):
    dict_form_data['bonus_info'] = bonus_info
    dict_form_data.get('widgets_list')[2].update_text(dict_form_data.get('bonus_info'), var.COLOR_NEGRO)
    
def update(dict_form_data: dict):
    base_form.update(dict_form_data)

def draw(dict_form_data: dict):
    base_form.draw(dict_form_data)
    base_form.draw_widgets(dict_form_data)


