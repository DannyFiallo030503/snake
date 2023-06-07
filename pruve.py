# pylint: disable=no-member
# pylint: disable=all

import pygame
import sys
from Interface.button_use import Button
from Interface.text_button_use import TextInput_text
from Logic.Save_load import save_maps



def Save_screen(map,x,y,score,obst,eggs,walls,points,fps,name):

    pygame.init()

    RED_Tono_claro= (255, 128, 128)
    MEDIUM_GREEN = (80, 200, 100)

    DISPLAY_END=pygame.display.set_mode((1200,900))
    pygame.display.set_caption("Snake egg-eater")

    font = pygame.font.SysFont('Arial', 16)

    title= pygame.font.SysFont('Impact', 150)
    text= title.render("Save Game", True, (MEDIUM_GREEN))


    button_save = Button(350, 500, 200, 50, (0,0,255), "Save map", (255, 255, 255), action=lambda: save_maps(map,x,y,1,eggs,1,points,fps,name)) # cambiar
    button_create_map = Button(650, 500, 200, 50, (255,0,0), "Title", (255, 255, 255), action=lambda: Create_map(map,None,None,eggs,points))
    name_map = TextInput_text(150, 60, 50, 30, (255, 255, 255), "Arial", 16)

    while True:

        text_score = font.render(f'Score {score}', True, (255, 255, 255))

        DISPLAY_END.fill(RED_Tono_claro)

        for event in pygame.event.get():
            # salida del bucle
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if name!=None:
                button_save.handle_event(event)
            button_create_map.handle_event(event)
            name=name_map.handle_event_txt(text)


        button_save.draw(DISPLAY_END,font)
        button_create_map.draw(DISPLAY_END,font)
        name_map.draw_txt(DISPLAY_END,font)   

        text_rect = text_score.get_rect()
        text_rect.topleft = (500, 380)
        DISPLAY_END.blit(text_score, text_rect)

        text_rect = text.get_rect()
        text_rect.x = 250
        text_rect.y = 150
        DISPLAY_END.blit(text, text_rect)

        pygame.display.flip() 

map=[[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2], [-2, 0, 0, 0, 0, 0, 0, 0, 0, -2], [-2, 0, 4, 0, 0, 0, 0, -1, 0, -2], [-2, 0, 0, 0, 0, 0, 0, -3, 0, -2], [-2, 0, 0, 0, 0, 0, 0, -1, 0, -2], [-2, 0, 0, 0, 0, 0, 1, 5, 0, -2], [-2, 0, 0, 0, 0, 0, 0, 0, 0, -2], [-2, 0, 0, 0, 0, 0, 0, 0, 0, -2], [-2, 0, 0, 0, 0, 0, 0, 0, 0, -2], [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2]]
x=10
y=10
score=10
eggs=2
points=5
fps=2
name="3"
Save_screen(map,x,y,score,1,eggs,1,points,fps,name)              