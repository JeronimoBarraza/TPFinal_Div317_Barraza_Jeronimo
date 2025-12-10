import pygame as pg
import sys
import modulos.variables as var
import modulos.forms.form_manager as form_manager
import modulos.jugador as jugador_humano
import participante as participante

def pythonisa():

    pg.init()
    pg.mixer.init()

    pg.display.set_caption(var.TITULO_JUEGO)
    pantalla = pg.display.set_mode(var.DIMENSION_PANTALLA)
    pg.display.set_icon(pg.image.load(var.IMAGEN_ICONO_JUEGO))
    corriendo = True
    reloj = pg.time.Clock()
    datos_juego = {
        "puntuacion": 0,
        "cantidad_vidas": var.CANTIDAD_VIDAS,
        "player": participante.inicializaar_participante(pantalla, 'jugador'),
        "volumen_musica": 100,
        "tiempo_finalizado": None,
    }

    f_manager = form_manager.create_form_manager(pantalla, datos_juego)

    while corriendo:

        event_list = pg.event.get()
        reloj.tick(var.FPS)

        for event in event_list:
            if event.type == pg.QUIT:
                corriendo = False
        
        form_manager.update(f_manager, event_list)


        pg.display.flip()

    pg.quit()
    sys.exit()