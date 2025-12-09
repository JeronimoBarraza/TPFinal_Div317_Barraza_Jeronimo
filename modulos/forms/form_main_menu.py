import pygame as pg
import sys
import modulos.forms.base_form as base_form
import modulos.nivel_cartas as nivel_cartas
import modulos.variables as var
import participante as participante
from utn_fra.pygame_widgets import (
     Label, ButtonImageSound, TextPoster
)

# def init_form_main_menu(name: str, screen: pg.Surface, active: bool, coords: tuple[int, int], level_num: int) -> dict:
def init_form_main_menu(dict_form_data: dict):

    form = base_form.create_base_form(dict_form_data)

    form['label_titulo'] = Label(
        x=635, y=115, text='DRAGON BALL Z TCG', screen=form.get('screen'), 
        font_path="./modulos/forms/Halimount.otf", font_size=75, color=var.COLOR_NARANJA)
    
    form['label_main_menu'] = Label(
        x=645, y=185, text='MAIN MENU', screen=form.get('screen'), 
        font_path="./modulos/forms/Halimount.otf", font_size=55)   

    form['boton_jugar'] = ButtonImageSound(
        x=645, y=365, width=126, height=33,text='', screen=form.get('screen'), 
        image_path=dict_form_data.get('botones').get('jugar'), sound_path=dict_form_data.get('sound_path'),
        font_size=35, on_click=cambiar_formulario_on_click, on_click_param='form_start_level') 

    form['boton_historia'] = ButtonImageSound(
        x=645, y=437, width=126, height=33,text='', screen=form.get('screen'), 
        image_path=dict_form_data.get('botones').get('historia'),sound_path=dict_form_data.get('sound_path'), 
        font_size=35, on_click=cambiar_formulario_on_click, on_click_param='form_historia') 
    
    form['boton_ranking'] = ButtonImageSound(
        x=645, y=510, width=126, height=33,text='', screen=form.get('screen'), 
        image_path=dict_form_data.get('botones').get('ranking'), sound_path=dict_form_data.get('sound_path'), 
        font_size=35, on_click=cambiar_formulario_on_click, on_click_param='form_ranking')

    form['boton_salir'] = ButtonImageSound(
        x=645, y=585, width=126, height=33,text='', screen=form.get('screen'), 
        image_path=dict_form_data.get('botones').get('salir'),sound_path=dict_form_data.get('sound_path'), 
        font_size=35, on_click=click_salir, on_click_param='Boton Salir')

    form['widgets_list'] = [
        form.get('label_titulo'), form.get('label_main_menu'), form.get('boton_jugar'), 
        form.get('boton_historia'), form.get('boton_ranking'), form.get('boton_salir')
    ]

    base_form.forms_dict[dict_form_data.get('name')] = form

    return form

def iniciar_stage(form_name: str):
    cambiar_formulario_on_click(form_name)
    # stage_form = var.

def cambiar_formulario_on_click(parametro: str):
    base_form.set_active(parametro)
    
    if parametro == 'form_start_level':

        form_start_level = base_form.forms_dict[parametro]

        if form_start_level.get('jugador') is None:
            form_start_level['jugador'] = participante.inicializaar_participante(
            pantalla=form_start_level.get('screen'),
            nombre='Jugador'
        )
        form_start_level['level'] = nivel_cartas.reiniciar_nivel(          # puede ser None y NO hay problema
            form_start_level['jugador'],
            form_start_level['screen'],
            form_start_level['level_number']
            )
        nivel_cartas.inicializar_data_nivel(form_start_level.get('level'))
    base_form.set_active(parametro)
    base_form.stop_music()
    base_form.play_music(base_form.forms_dict[parametro])

def click_start(parametro: str):
    print(parametro)

def click_salir():
    pg.quit()
    sys.exit()

def draw(form_data: dict):
    base_form.draw(form_data)
    base_form.draw_widgets(form_data)

def update(form_data: dict):
    base_form.update(form_data)

