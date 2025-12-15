import pygame.mixer as mixer

music_configs = {
    "actual_music_path": ''
}

def set_music(music_path):
    music_configs['actual_music_path'] = music_path

def play_music():
    if music_configs.get('actual_music_path'):
        mixer.music.load(music_configs.get('actual_music_path'))
        mixer.music.set_volume(0.3)
        mixer.music.play(-1, 0, 2500)

def stop_music():
    if music_configs.get('actual_music_path'):
        mixer.music.fadeout(500)
