import pygame as pg
from pygame import mixer
import os 
import re 

pg.init()
mixer.init()


'''
File handling
'''
def get_playlist(path):
    if os.path.exists(path):
        for dirpath, dirlist, files in os.walk(path):
            for f in files:    
                new_list.append(os.path.join(dirpath, f))
    else:
        print("The path does not exist.")

    return list(filter(re.compile(r".*\.(mp3|ogg|wav)$").match, new_list))            

path = r"c:\Users\Temirlan\Desktop\second sem\pp2\labs\lab 7\player_assets"
new_list = []
playlist = get_playlist(path)
songNames = []


'''
PyGame setup
'''
screen = pg.display.set_mode((450, 650))
title = pg.display.set_caption("music player")
icon = pg.display.set_icon(pg.image.load(r"player_assets/icon.png"))
clock = pg.time.Clock()

done = False
started = False
paused = False

song_index = 0
song_channel = mixer.Channel(1)

initial_volume = 0.5
current_volume = initial_volume


'''
Image Handling
'''
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pg.image.load(canonicalized_path)
                _image_library[path] = image
        return image

os.chdir("player_assets")
play_surf = get_image("play.png")
pause_surf = get_image("pause.png")
next_surf = get_image("next.png")
previous_surf = get_image("prev.png")

volumeUp_surf = get_image("volumeUp.png")
volumeDown_surf = get_image("volumeDown.png")
volumeDefault_surf = get_image("volumeDefault.png")

blackgound_surf = get_image("blackgound.jpg")
resized_blackgound = pg.transform.scale(blackgound_surf, (450, 650))

play_rect = play_surf.get_rect(center = (screen.get_rect().center[0], 550))
next_rect = next_surf.get_rect(center = (screen.get_rect().center[0]*3/2, 550))
previous_rect = previous_surf.get_rect(center = (screen.get_rect().center[0]/2, 550))
volume_rect = volumeDefault_surf.get_rect(center = (screen.get_rect().center[0]/8, 40))


'''
Main Loop
'''
while not done:
    for event in pg.event.get():
        
        #exit the program
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            done = True
        
        #play button
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            if not started:
                song_channel.play(mixer.Sound(playlist[song_index]))
                started = True
                play_surf = get_image("pause.png")
            elif started and not paused:
                paused = True
                song_channel.pause()
                play_surf = get_image("play.png")            
            elif started and paused:
                paused = False
                song_channel.unpause()
                play_surf = get_image("pause.png")

        #next button
        elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
            song_index += 1
            if song_index == len(playlist):
                song_index = 0
            if started:
                play_surf = get_image("pause.png")
                song_channel.play(mixer.Sound(playlist[song_index]))
        
        #previous button
        elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
            song_index -= 1
            if song_index == -1:
                song_index = len(playlist) - 1
            if started:
                play_surf = get_image("pause.png")
                song_channel.play(mixer.Sound(playlist[song_index]))

        #volumeUP button
        elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
            volumeDefault_surf = get_image("volumeUp.png")
            current_volume = min(1.0, current_volume + 0.1)
            song_channel.set_volume(current_volume)

        #volumeDOWN button
        elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            volumeDefault_surf = get_image("volumeDown.png")
            current_volume = max(0.0, current_volume - 0.1)
            song_channel.set_volume(current_volume)

        #when keyup => volumeDEFAULT button 
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                volumeDefault_surf = get_image("volumeDefault.png")

    screen.blit(resized_blackgound, (0, 0))

    play_button = screen.blit(play_surf, play_rect)
    next_button = screen.blit(next_surf, next_rect)
    previous_button = screen.blit(previous_surf, previous_rect)
    volume_button = screen.blit(volumeDefault_surf, volume_rect)

    pg.display.flip()
    clock.tick(90)

pg.quit()