import pygame as pg
import modulos.forms.base_form as base_form
import modulos.variables as var
import modulos.forms.form_main_menu as form_main_menu
from utn_fra.pygame_widgets import (
    Button, Label
)

# def init_form_historia(name: str, screen: pg.Surface, active: bool, coords: tuple[int, int], level_num: int) -> dict:
def init_form_historia(dict_form_data: dict):
    form = base_form.create_base_form(dict_form_data)

    form['lbl_titulo_juego'] = Label(x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 250, text='DRAGON BALL Z', screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=75)
    form['lbl_titulo_options'] = Label(x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 175, text='OPTIONS', screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=50)
    
    form['boton_volver'] = Button(x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 + 270, text='BACK TO MENU', screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=30, on_click=click_volver, on_click_param='form_main_menu') 
    form['boton_music_on'] = Button(x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 30, text='MUSIC ON', screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=40, on_click=click_volver, on_click_param='music_on') 
    form['boton_music_off'] = Button(x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 + 30, text='MUSIC OFF', screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=40, on_click=click_volver, on_click_param='music_off') 


    form['widgets_list'] = [
        form.get('lbl_titulo_juego'), form.get('lbl_titulo_options'), form.get('boton_volver'), form.get('boton_music_on'), form.get('boton_music_off')
    ]
    
    base_form.forms_dict[dict_form_data.get('name')] = form
    return form

def click_volver(parametro: str):
    base_form.stop_music()
    base_form.play_music(base_form.forms_dict[parametro])
    base_form.set_active(parametro)

def draw(form_data: dict):
    base_form.draw(form_data)
    base_form.update_widgets(form_data)

def update(form_data: dict):
    base_form.update(form_data)
