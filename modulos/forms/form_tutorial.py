import pygame as pg
import modulos.auxiliar as aux
import modulos.forms.base_form as base_form
import modulos.variables as var
import modulos.forms.form_start_level as form_start_level
import modulos.nivel_cartas as nivel_cartas
import participante as participante
from utn_fra.pygame_widgets import (
    Button, Label, ImageLabel
)

def init_form_tutorial(dict_form_data: dict):
    form = base_form.create_base_form(dict_form_data)

    form['pagina_actual'] = 0
    form['pagina_siguiente'] = 0

    form['click_proximo'] = False
    form['click_previo'] = False        

    form['textos_tutorial'] = [
        "Al presionar el boton play_hand, funciona para que empiece la partida y \n muestre tanto la carta del jugador como la del enemigo.",
        "El boton es un bonus que lo que hace es solamente por esa ronda, el daño que deberías recibir vos, se lo das a tu enemigo. generando el famoso ",
        "El boton heal es un bonus que lo que hace es curarte un cierto porcentaje de vida",
        "El label Score es el puntaje progresivo, que se va actualizando cada ronda jugada, si ganas sumas, si empatas/perdes se mantiene",
        "El label TIMER es el tiempo de la partida, donde arranca en 5000 y va disminuyendo",
        "Aqui podes ver el ranking.\nMuestra los mejores puntajes del juego."
        ]
    
    form['fondos_tutorial'] = [
        var.IMAGEN_ENTER_NAME,
        var.IMAGEN_MENU_PRINCIPAL,
        var.IMAGEN_BONUS,
        var.IMAGEN_PAUSE,
        var.IMAGEN_TUTORIAL,
        var.IMAGEN_CARTA
        ]

    form['tutorial'] = Label(
        x=635, y=50, text='TUTORIAL', screen=form.get('screen'), 
        font_path=var.FUENTE_HALIMOUNT, font_size=40, color=var.COLOR_NEGRO)
    
    form['lbl_descripcion'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2,
        y=var.DIMENSION_PANTALLA[1] // 2 + 80,
        text=form['textos_tutorial'][0],
        screen=form.get('screen'),
        font_path=var.FUENTE_HALIMOUNT,
        font_size=28,
        color=var.COLOR_NEGRO
    )
    
    form['imglbl_jugar'] = ImageLabel(
        x=580, y=155, text=f'', screen=form.get('screen'), 
        image_path=var.BOTON_PLAYHAND, width=130, height=50,
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    form['imglbl_heal'] = ImageLabel(
        x=580, y=155, text=f'', screen=form.get('screen'), 
        image_path=var.BOTON_ICON_HEAL, width=90, height=90,
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    form['imglbl_shield'] = ImageLabel(
        x=580, y=155, text=f'', screen=form.get('screen'), 
        image_path=var.BOTON_ICON_SHIELD, width=90, height=90,
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    form['imglbl_puntaje'] = ImageLabel(
        x=595, y=145, text=f'', screen=form.get('screen'), 
        image_path=var.IMAGEN_SCORE_TUTORIAL, width=90, height=90,
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )
    
    form['imglbl_timer'] = ImageLabel(
        x=615, y=175, text=f'', screen=form.get('screen'), 
        image_path=var.IMAGEN_TIMER_TUTORIAL, width=80, height=80,
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    form['imglbl_ranking'] = ImageLabel(
        x=580, y=155, text=f'', screen=form.get('screen'), 
        image_path=var.BOTON_RANKING, width=130, height=50,
        font_path=var.FUENTE_HALIMOUNT, font_size=25
    )

    form['btn_proximo'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2 + 450, y= var.DIMENSION_PANTALLA[1] // 2 + 170, 
        text="PROXIMO",screen=form.get('screen'), font_path=var.FUENTE_HALIMOUNT, 
        font_size=25, color=var.COLOR_NEGRO,
        on_click=click_proximo, on_click_param=form
    )

    form['btn_volver'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y= var.DIMENSION_PANTALLA[1] // 2 + 320, 
        text="VOLVER AL MENU",screen=form.get('screen'), font_path=var.FUENTE_HALIMOUNT, font_size=25, color=var.COLOR_NEGRO,
        on_click=volver_menu, on_click_param='form_main_menu'
    )

    form['btn_previo'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2 - 350, y= var.DIMENSION_PANTALLA[1] // 2 + 170, 
        text="PREVIO",screen=form.get('screen'), font_path=var.FUENTE_HALIMOUNT, font_size=25, color=var.COLOR_NEGRO,
        on_click=click_previo, on_click_param=form
    )

    form['widgets_list'] = [
        form.get('tutorial'), form.get('lbl_descripcion'), form.get('btn_proximo'), form.get('btn_volver'), form.get('btn_previo')
    ]

    base_form.forms_dict[dict_form_data.get('name')] = form
    return form

def click_proximo(form):
    form['click_proximo'] = True

def click_previo(form):
    form['click_previo'] = True

def pagina_siguiente(form):
    if form['pagina_actual'] < len(form['fondos_tutorial']) - 1:
        form['pagina_actual'] += 1
        
def pagina_previa(form):
    if form['pagina_actual'] > 0:
        form['pagina_actual'] -= 1  
        
def volver_menu(_):
    base_form.set_active('form_main_menu')

def draw(form_data: dict):
    pagina = form_data['pagina_actual']

    form_data['background'] = pg.image.load(form_data['fondos_tutorial'][pagina]).convert()

    base_form.draw(form_data)
    base_form.update_widgets(form_data)

    # dibujar imágenes según página
    if pagina == 0:
        form_data['imglbl_jugar'].draw()

    elif pagina == 1:
        form_data['imglbl_heal'].draw()
        
    elif pagina == 2:
        form_data['imglbl_shield'].draw()

    elif pagina == 3:
        form_data['imglbl_puntaje'].draw()

    elif pagina == 4:
        form_data['imglbl_timer'].draw()
    
    elif pagina == 5:
        form_data['imglbl_ranking'].draw()
        
def update(form_data: dict):
    if form_data['click_proximo']:
        if form_data['pagina_actual'] < len(form_data['fondos_tutorial']) - 1:
            form_data['pagina_actual'] += 1
        form_data['click_proximo'] = False

    if form_data['click_previo']:
        if form_data['pagina_actual'] > 0:
            form_data['pagina_actual'] -= 1
        form_data['click_previo'] = False

    pagina = form_data['pagina_actual']

    form_data['lbl_descripcion'].update_text(
        form_data['textos_tutorial'][pagina],
        color=var.COLOR_NEGRO
    )

    base_form.update(form_data)