import pygame as pg
import modulos.variables as var
import modulos.forms.form_main_menu as form_main_menu
import modulos.forms.form_historia as form_historia
import modulos.forms.form_ranking as form_ranking
import modulos.forms.form_start_level as form_start_level
import modulos.forms.form_enter_name as form_enter_name
import modulos.forms.form_pause as form_pause
import modulos.forms.form_bonus as form_bonus
import modulos.forms.form_tutorial as form_tutorial

def create_form_manager(screen: pg.Surface, datos_juego: dict):

    form = {}
    form['main_screen'] = screen
    form['current_level'] = 1
    form['game_started'] = False
    form['enemy'] = None

    form['jugador'] = datos_juego.get('player')

    form['form_list'] = [
        form_main_menu.init_form_main_menu(
            dict_form_data= {
                "name":'form_main_menu', 
                "screen":form.get('main_screen'), 
                "active":True, 
                "coords":(0,0), 
                "stage_number":1, 
                "music_path": var.RUTA_MUSICA_MENU,
                "sound_path": var.RUTA_SONIDO_CLICK,
                "background_path": var.IMAGEN_MENU_PRINCIPAL,
                "screen_dimentions": var.DIMENSION_PANTALLA,
                "botones": {
                    "jugar": var.BOTON_JUGAR,
                    "historia": var.BOTON_HISTORIA,
                    "ranking": var.BOTON_RANKING,
                    "salir": var.BOTON_SALIR
                }
            }
        ),
        form_historia.init_form_historia(
            dict_form_data={
                "name":'form_historia', 
                "screen":form.get('main_screen'), 
                "active":True, 
                "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA_MENU,
                "sound_path": var.RUTA_SONIDO_CLICK,
                "background_path": var.IMAGEN_OPTIONS,
                "screen_dimentions": var.DIMENSION_PANTALLA,
                "botones": {
                    "music_on": '',
                    "music_off": '',
                    "volver": var.BOTON_VOLVER
                }
            }
        ),
        form_ranking.init_form_ranking(
            dict_form_data={
                "name":'form_ranking', 
                "screen":form.get('main_screen'), 
                "active":True, 
                "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA_MENU,
                "sound_path": var.RUTA_SONIDO_CLICK,
                "background_path": var.IMAGEN_RANKING,
                "screen_dimentions": var.DIMENSION_PANTALLA,
                "botones": {
                    "volver": var.BOTON_VOLVER
                    },
            },  
               jugador=form.get('jugador')
        ),
        form_start_level.init_form_start_level(
            dict_form_data={
                "name":'form_start_level', 
                "screen":form.get('main_screen'), 
                "active":True, 
                "coords":(0,0), 
                "stage_number": 1, 
                "music_path": var.RUTA_MUSICA_MENU,
                "sound_path": var.RUTA_SONIDO_CLICK,
                "background_path": var.IMAGEN_CARTA,
                "screen_dimentions": var.DIMENSION_PANTALLA,
                "jugador": form.get('jugador'),
                "botones": {
                    "play_hand": var.BOTON_PLAYHAND,
                    "shield": var.BOTON_SHIELD,
                    "heal": var.BOTON_HEAL,
                },
            },
        ),
        form_enter_name.init_form_enter_name(
            dict_form_data={
                "name":'form_enter_name', 
                "screen":form.get('main_screen'), 
                "active":True, 
                "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA_MENU,
                "sound_path": var.RUTA_SONIDO_CLICK,
                "background_path": var.IMAGEN_ENTER_NAME,
                "screen_dimentions": var.DIMENSION_PANTALLA,
            }, jugador=form.get('jugador')
        ),
        form_pause.init_form_pause(
            dict_form_data={
                "name":'form_pause', 
                "screen":form.get('main_screen'), 
                "active":True, 
                "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA_MENU,
                "sound_path": var.RUTA_SONIDO_CLICK,
                "background_path": var.IMAGEN_PAUSE,
                "screen_dimentions": var.DIMENSION_PANTALLA,
            }
        ),
         form_bonus.init_form_bonus(
            dict_form_data={
                "name":'form_bonus', 
                "screen":form.get('main_screen'), 
                "active":True, 
                "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA_MENU,
                "sound_path": var.RUTA_SONIDO_CLICK,
                "background_path": var.IMAGEN_BONUS,
                "screen_dimentions": var.DIMENSION_PANTALLA,
            }, jugador=form.get('jugador')
       ),
       form_tutorial.init_form_tutorial(
            dict_form_data={
                "name":'form_tutorial', 
                "screen":form.get('main_screen'), 
                "active":True, 
                "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA_MENU,
                "sound_path": var.RUTA_SONIDO_CLICK,
                "background_path": var.IMAGEN_TUTORIAL,
                "screen_dimentions": var.DIMENSION_PANTALLA,
                }
       )        
    ]
    return form 

def forms_update(form_manager: dict, lista_eventos: pg.event.Event):
    #Preguntar por c/u de los form si esta activo y en caso de estarlo, actualizar y dibujar

    #Form menu
    if form_manager.get('form_list')[0].get('active'):
        form_main_menu.update(form_manager.get('form_list')[0])
        form_main_menu.draw(form_manager.get('form_list')[0])

    #Form historia
    elif form_manager.get('form_list')[1].get('active'):
        form_historia.update(form_manager.get('form_list')[1])
        form_historia.draw(form_manager.get('form_list')[1])

    #Form ranking
    elif form_manager.get('form_list')[2].get('active'):
        form_ranking.update(form_manager.get('form_list')[2])
        form_ranking.draw(form_manager.get('form_list')[2])
        
    elif form_manager.get('form_list')[3].get('active'):
        form_start_level.update(form_manager.get('form_list')[3], lista_eventos)
        form_start_level.draw(form_manager.get('form_list')[3]) 

    elif form_manager.get('form_list')[4].get('active'):
        form_enter_name.update(form_manager.get('form_list')[4], lista_eventos)
        form_enter_name.draw(form_manager.get('form_list')[4]) 
    
    elif form_manager.get('form_list')[5].get('active'):
        form_pause.update(form_manager.get('form_list')[5])
        form_pause.draw(form_manager.get('form_list')[5]) 
    
    elif form_manager.get('form_list')[6].get('active'):
        form_bonus.update(form_manager.get('form_list')[6])
        form_bonus.draw(form_manager.get('form_list')[6])

    elif form_manager.get('form_list')[7].get('active'):
        form_tutorial.update(form_manager.get('form_list')[7])
        form_tutorial.draw(form_manager.get('form_list')[7])
        
def update(form_manager: dict, lista_eventos: pg.event.Event):
    forms_update(form_manager, lista_eventos)