import pygame as pg
import sys
import modulos.auxiliar as aux
import modulos.forms.base_form as base_form
import modulos.variables as var
from utn_fra.pygame_widgets import (
    Button, Label, ButtonImageSound
)

# def init_form_ranking(name: str, jugador: dict, screen: pg.Surface, active: bool, coords: tuple[int, int], level_num: int) -> dict:
def init_form_ranking(dict_form_data: dict, jugador: dict):
    form = base_form.create_base_form(dict_form_data)

    form['jugador'] = jugador

    form['ranking_screen'] = []
    form['ranking_list'] = []

    form['lbl_titulo'] = Label(x=635, y=105, text='DRAGON BALL Z TCG', screen=form.get('screen'), 
                               font_path=var.FUENTE_HALIMOUNT, font_size=75, color=var.COLOR_BLANCO)

    form['lbl_subtitulo'] = Label(x=635, y=195, text='TOP 10 RANKING', screen=form.get('screen'), 
                                  font_path=var.FUENTE_HALIMOUNT, font_size=55, color=var.COLOR_BLANCO)

    form['boton_volver'] = ButtonImageSound(x=635, y=612, width=125, height=40, text='', screen=form.get('screen'), 
                                            image_path=dict_form_data.get('botones').get('volver'), sound_path=dict_form_data.get('sound_path'),
                                            font_size=40, on_click=click_return_menu, on_click_param='form_main_menu')
    
    form['data_cargada'] = False
    form['widgets_list'] = [
        form.get('lbl_titulo'), form.get('lbl_subtitulo'), form.get('boton_volver')
    ]

    base_form.forms_dict[dict_form_data.get('name')] = form

    return form

def click_return_menu(parametro: str):
    print('asdasdasdasdsa')
    base_form.stop_music()
    base_form.play_music(base_form.forms_dict[parametro])
    base_form.set_active(parametro)
    base_form.forms_dict['form_ranking']['data_loaded'] = False

def init_ranking(form_data: dict):
    form_data['ranking_screen'] = []
    matriz = form_data.get('ranking_list')

    for indice_fila in range(len(matriz)):
        fila = matriz[indice_fila]

        #numero
        form_data['ranking_screen'].append(
                Label(x=435, y=735//2.9 + indice_fila*31,text=f'{indice_fila + 1}', 
                      screen=form_data.get('screen'), font_path=var.FUENTE_HALIMOUNT, 
                      color=var.COLOR_BLANCO, font_size=40)
            )
        
        #nombre
        form_data['ranking_screen'].append(
                Label(x=635, y=735//2.9 + indice_fila*31, text=f'{fila[0]}', 
                      screen=form_data.get('screen'), 
                      font_path=var.FUENTE_HALIMOUNT, color=var.COLOR_BLANCO, font_size=40)
            )
        
        #puntaje
        form_data['ranking_screen'].append(
                Label(x=835, y=735//2.9 + indice_fila*31, text=f'{fila[1]}', 
                      screen=form_data.get('screen'), font_path=var.FUENTE_HALIMOUNT, 
                      color=var.COLOR_BLANCO,font_size=40)
            )

def inicializar_ranking(form_data: dict):
    if not form_data.get('data_loaded'):
        form_data['ranking_list'] = aux.cargar_ranking()[:10]
        init_ranking(form_data)
        form_data['data_loaded'] = True

def update(form_data: dict):
    if form_data.get('active'):
        inicializar_ranking(form_data)
    base_form.update(form_data)

def draw(form_data: dict):
    base_form.draw(form_data)
    base_form.draw_widgets(form_data)
    for lbl in form_data.get('ranking_screen'):
        lbl.draw()
