import pygame as pg
import modulos.auxiliar as aux
import modulos.forms.base_form as base_form
import modulos.variables as var
import participante as particip
from utn_fra.pygame_widgets import (
    Button, Label, TextBox
)

def init_form_enter_name(dict_form_data: dict, jugador: dict):
    form = base_form.create_base_form(dict_form_data)

    form['jugador'] = jugador
    form['confirm_name'] = False

    form['title'] = Label (
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 250, 
        text=var.TITULO_JUEGO, screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=70, 
    )
    form['title_2'] = Label (
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 150, text='¡Ganaste!', 
        screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=60, color=var.COLOR_NEGRO
    )
    form['subtitle'] = Label (
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 80, text='Escribe tu nombre: ', 
        screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=50, color=var.COLOR_BLANCO
    )
    form['subtitle_score'] = Label (
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 20, text=f'{particip.get_score_participante(form.get('jugador'))}', 
        screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=30, color=var.COLOR_BLANCO
    )

    form['lbl_nombre_texto'] = Label (
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 + 30, text=f'', 
        screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=30, color=var.COLOR_BLANCO
    )

    form['text_box'] = TextBox(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 + 40, 
        text='________________',screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=25, color=var.COLOR_NEGRO
    )

    form['btn_confirm_name'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y= var.DIMENSION_PANTALLA[1] // 2 + 100, 
        text="CONFIRMAR NOMBRE",screen=form.get('screen'), font_path=var.RUTA_FUENTE, font_size=25,
        on_click=submit_name, on_click_param=form
    )

    form['widgets_list'] = [
        form.get('title'), form.get('title_2'), form.get('subtitle'), form.get('subtitle_score'), form.get('lbl_nombre_texto'), form.get('btn_confirm_name')
    ]

    base_form.forms_dict[dict_form_data.get('name')] = form
    return form

def update_texto_victoria(dict_form_data: dict, win_status: bool):
    if win_status:
        mensaje = 'Victoria!'
    else: 
        mensaje = 'Derrota!'
        dict_form_data.get('widgets_list')[1].update_text(text=mensaje, color=var.COLOR_BLANCO)

def clear_text(form_dict: dict):
    form_dict['text_box'].writing = ''

def submit_name(form_dict: dict):

    nombre_jugador = form_dict.get('lbl_nombre_texto').text
    particip.set_nombre_participante(form_dict.get('jugador'), nombre_jugador)

    nombre_jugador_seteado = particip.get_nombre_participante(form_dict.get('jugador'))
    puntaje_jugador = particip.get_score_participante(form_dict.get('jugador'))

    print(f'{nombre_jugador_seteado} - {puntaje_jugador}')
    data_to_csv = particip.info_to_csv(form_dict.get('jugador')) 
    aux.guardar_info_csv(data_to_csv)

    form_dict['confirm_name'] = True
    base_form.set_active('form_ranking')    

def update(dict_form_data: dict, event_list: list):
    dict_form_data['score'] = particip.get_score_participante(dict_form_data.get('jugador'))    

    dict_form_data['subtitle_score'].update_text(f'Score: {dict_form_data['score']}', var.COLOR_BLANCO)
    dict_form_data['lbl_nombre_texto'].update_text(f'{dict_form_data.get('text_box').writing.upper()}', var.COLOR_BLANCO)

    dict_form_data.get('text_box').update(event_list)
    base_form.update(dict_form_data)

def draw(dict_form_data: dict):
    base_form.draw(dict_form_data)
    base_form.draw_widgets(dict_form_data)
    dict_form_data.get('text_box').draw()

    # dict_form_data['writing_text'] = Label(
    #     x=var.DIMENSION_PANTALLA[0] // 2, y= var.DIMENSION_PANTALLA[1] // 2 + 30, 
    #     text=f'{dict_form_data.get('text_box').writing.upper()}', screen=dict_form_data.get('screen'), 
    #     font_path=var.RUTA_FUENTE, font_size=30, color= var.COLOR_BLANCO
    # )

    # dict_form_data.get('writing_text').draw()
