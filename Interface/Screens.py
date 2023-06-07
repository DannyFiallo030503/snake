# pylint: disable=no-member
# pylint: disable=all
import pygame
import sys
import os
from Interface.button_use import Button
from Interface.text_button_use import TextInput, TextInput_text
from Logic.map import largue_map, eggs_map, snake_character, max_points, obstacles
from Logic.score import calculate_dist
from Interface.show_map_use import show_map
from Interface.scale_photos import scale_img
from Logic.SNAKE_GRW_UP import body_snake_grow_up, snake_body_move_array, choice_move
from Logic.Save_load import save_maps,load_maps
from Logic.map import random_map

# Colores esto despues lo tengo que mover a un txt y solo dejar los que estoy usando
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
BROWN = (150, 75, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

LIGHT_GREEN = (150, 255, 150)
DARK_GREEN = (50, 150, 70)
MEDIUM_GREEN = (80, 200, 100)
PALE_GREEN = (190, 240, 200)

RED_Tono_claro= (255, 128, 128)
RED_Tono_más_claro= (255, 192, 192)
RED_Tono_oscuro= (128, 0, 0)
RED_Tono_más_oscuro= (64, 0, 0)

ORANGE_Tono_claro= (255, 204, 153)
ORANGE_Tono_más_claro= (255, 229, 204)
ORANGE_Tono_oscuro= (128, 64, 0)
ORANGE_Tono_más_oscuro= (64, 32, 0)

YELLOW_Tono_claro= (255, 255, 128)
YELLOW_Tono_más_claro= (255, 255, 192)
YELLOW_Tono_oscuro= (128, 128, 0)
YELLOW_Tono_más_oscuro= (64, 64, 0)

BLUE_Tono_claro= (128, 128, 255)
BLUE_Tono_más_claro= (192, 192, 255)
BLUE_Tono_oscuro= (0, 0, 128)
BLUE_Tono_más_oscuro= (0, 0, 64)

PURPLE_Tono_claro= (192, 128, 192)
PURPLE_Tono_más_claro= (229, 204, 229)
PURPLE_Tono_oscuro= (64, 0, 64)

# Pantalla principal
def main_screen():
    pygame.init()

    DISPLAYSURF=pygame.display.set_mode((1200,900))

    pygame.display.set_caption("Snake egg-eater")

    fontd = pygame.font.Font(None, 50)
    map=[]
    x_rand=None
    y_rand=None
    fps_rand=None
    points_rand=None
    eggs_rand=None

    #titulo del juego
    title= pygame.font.SysFont('Impact', 150)
    text= title.render("Snake egg-eater", True, (MEDIUM_GREEN))

    #botones de accion para cambios de pantalla
    button1 = Button(390, 400, 400, 100, (RED), "Create map", (255, 255, 255), action=lambda: Create_map(map,None,None,None,None,None,None,None))
    button2 = Button(390, 550, 400, 100, (LIGHT_GREEN), "Create random map", (255, 255, 255), action=lambda: random_map())  # revisar cual es el error
    button3 = Button(390, 700, 400, 100, (BLUE), "load map", (255, 255, 255), action=lambda: load_screen())

    #inicio del juego o mejor dicho del bucle infinito qque esperara a que preciones los botones
    while True:

        DISPLAYSURF.fill(YELLOW_Tono_claro)

        #terminaccion del juego
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            #procesa si precionaste o no el boton
            button1.handle_event(event)
            result=button2.handle_event(event)
            if result != None:
                map,x_rand,y_rand,fps_rand,points_rand,eggs_rand=result
                screen_game_play(map,x_rand,y_rand,fps_rand,points_rand,eggs_rand)
            button3.handle_event(event)

        #dibuja los botones    
        button1.draw(DISPLAYSURF, fontd)
        button2.draw(DISPLAYSURF, fontd)
        button3.draw(DISPLAYSURF, fontd)

        #dibuja el titulo
        text_rect = text.get_rect()
        text_rect.x = 120
        text_rect.y = 150
        DISPLAYSURF.blit(text, text_rect)

        pygame.display.flip() 


# Pantalla de creaccion de mapa
def Create_map(map,x,y,obst,cantMaxEggs,walls,maxPoint,FPSload):

    DISPLAY_CREATE_MAP=pygame.display.set_mode((1200,900))
    pygame.display.set_caption("Snake egg-eater")

    # datos inicales del mapa
    clock = pygame.time.Clock()
    FPS=60
    fila=0
    FPSload=None
    PointMax=None
    EggsMax=None
    correct_obst=0
    columna=0
    cell_size = 64
    grid_x=300
    grid_y=0
    gen_snake_text=None
    count_large_map=0
    count_obst=0
    count_gen_snake=0
    count_fps=0
    count_eggs=0
    count_points=0
    correct_EggsMax=0
    correct_PointMax=0
    pixel_x=0
    pixel_y=0
    pixel_xy=0

    # titulo de las entradas de texto
    l_m=pygame.font.SysFont('Impact', 30)
    text_l_m=l_m.render("Large map",True,(RED_Tono_claro))
    c_o=pygame.font.SysFont('Impact', 30)
    text_c_o=c_o.render("Quantity obst.",True,(RED_Tono_claro))
    m_p=pygame.font.SysFont('Impact', 30)
    text_m_p=m_p.render("Max points",True,(RED_Tono_claro))
    c_h=pygame.font.SysFont('Impact', 30)
    text_c_h=c_h.render("Quantity eggs",True,(RED_Tono_claro))
    f_p_s=pygame.font.SysFont('Impact', 30)
    text_f_p_s=f_p_s.render("Speed snake",True,(RED_Tono_claro))

    #llamada a las clases que se encargan de la creaccion de entrada de datos y botones
    button1 = Button(170, 830, 100, 50, (RED), "Back", (255, 255, 255), action=lambda: screen_game_play(map,x,y,FPSload,correct_PointMax,correct_EggsMax)) # arreglar debe llamar a la pantalla de inicio
    large_fila_box=TextInput(150, 60, 50, 30)
    large_columna_box=TextInput(90, 60, 50, 30)
    obst_box=TextInput(118,150,50,30)
    max_point_box=TextInput(118,250,50,30)
    cant_eggs_box=TextInput(118,350,50,30)
    gen_snake_text=TextInput(50, 530, 200, 50)
    FPS_box=TextInput(118,450,50,30)
    save_map_button= Button(58, 630, 180, 50, (RED), "save map", (255, 255, 255), action=lambda: Save_screen(map,x,y,0,correct_EggsMax,correct_PointMax,FPSload))
    random_mode_button=Button(35, 730, 230, 50, (RED), "choise mode", (255, 255, 255), action=lambda: screen_game_play(map,x,y,FPS,correct_PointMax,correct_EggsMax)) # betado
    start_button=Button(25, 830, 100, 50, (RED), "Start", (255, 255, 255), action=lambda: screen_game_play(map,x,y,FPS,correct_PointMax,correct_EggsMax))

    #buscar manera para que el direcctorio varie
    #cargando imagenes
    os.chdir("C:/Users/danny_fiallo/Documents/!!!Programación/!!!Code/Snake/Photos")
    walls=pygame.image.load("walls.jpg") 
    head=pygame.image.load("head.png")
    eggs=pygame.image.load("eggs.png")
    obstacles_img=pygame.image.load("obstacles.png")
    green_image = pygame.Surface((64, 64))
    numb = pygame.font.SysFont('Arial', 59)
    green_image.fill((0, 255, 0))

    

    #bucle infinito que dara inicio a la creaccion de mapa en tiempo real
    while True:

        #barra de opciones
        barra_menu=pygame.Rect(0,0,300,900)
        pygame.draw.rect(DISPLAY_CREATE_MAP,BLUE_Tono_más_claro,barra_menu)

        #barra de mapa
        barra_mapa=pygame.Rect(300,0,900,900)
        pygame.draw.rect(DISPLAY_CREATE_MAP,YELLOW_Tono_más_claro,barra_mapa)
        fontd = pygame.font.Font(None, 50)

        for event in pygame.event.get():
            # salida del bucle
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.unicode in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])):

                #llamada de espera a botones y textos de evento
                button1.handle_event(event) # boton de back   
                fila=large_fila_box.handle_event_text(event)
                columna=large_columna_box.handle_event_text(event)
                obst=obst_box.handle_event_text(event)
                maxPoint=max_point_box.handle_event_text(event)
                cantMaxEggs=cant_eggs_box.handle_event_text(event)
                gen_snake_text.handle_event_text(event)
                FPSload=FPS_box.handle_event_text(event)
                save_map_button.handle_event(event)
                random_mode_button.handle_event(event)
                start_button.handle_event(event)


                #condicionales para la entrada de texto del largo del mapa
                if count_large_map==0 and (fila or columna)!=None:
                    if fila!=None and columna==None:
                        x=int(fila)
                        fila=None
                        count_large_map=0
                    elif columna!=None and fila==None:
                        y=int(columna)
                        columna=None
                        count_large_map=0    
                    if (x and y)!=None:
                        if (x and y)>4:
                            map=largue_map(x,y)
                            count_large_map=1
                            count_gen_snake=1

                #condicionales para la entrada de texto de obstaculos
                if count_obst==0 or obst!=None:
                    if obst!=None:
                        correct_obst=int(obst)
                        map=obstacles(map,x-1,y-1,correct_obst)
                        count_obst=1
                        ok_obst=correct_obst
                        obst=None
                    elif obst==None and (x and y)!=None:
                        map=obstacles(map,x-1,y-1,correct_obst)    

                # condiccionales para la entrada de texto de la cantidad de huevos
                if count_eggs==0 or (EggsMax or maxPoint)!=None:
                    if maxPoint!=None and cantMaxEggs==None:
                        PointMax=int(maxPoint)
                    elif cantMaxEggs!=None and maxPoint==None:
                        EggsMax=int(cantMaxEggs)
                    if  EggsMax!=None and PointMax!=None:
                        map=eggs_map(map,x-1,y-1,EggsMax,PointMax)
                        correct_EggsMax=EggsMax
                        correct_PointMax=PointMax
                        EggsMax=None
                        PointMax=None
                        count_eggs=1

                # condiccionales para la generaccion de FPS
                if FPSload!=None:
                    FPS=int(FPSload) 

                if count_gen_snake==1:
                    if gen_snake_text!=None and (x and y)!=None :
                        map=snake_character(map,x,y)
                        count_gen_snake=0

        # mostrar el mapa
        if (x and y)!=None:
            pixel_x=900//y
            pixel_y=900//x
            if pixel_x>=pixel_y:
                pixel_xy=pixel_y
            else:
                pixel_xy=pixel_x
            scaled_walls,scaled_head,scaled_eggs,scaled_obstacles_img,scaled_green_image,scaled_numbscale_img=scale_img(pixel_xy,pixel_xy,walls,head,eggs,obstacles_img,green_image,numb)        
            show_map(map,DISPLAY_CREATE_MAP,scaled_walls,scaled_head,scaled_eggs,scaled_obstacles_img,scaled_green_image,grid_x,pixel_xy,grid_y,scaled_numbscale_img)                        

        # mostrar titulos de los box de texto
        text_l_m_xy=text_l_m.get_rect()
        text_l_m_xy.x= 80
        text_l_m_xy.y= 10
        DISPLAY_CREATE_MAP.blit(text_l_m,text_l_m_xy)
        text_c_o_xy=text_c_o.get_rect()
        text_c_o_xy.x=60
        text_c_o_xy.y=100
        DISPLAY_CREATE_MAP.blit(text_c_o,text_c_o_xy)
        text_m_p_xy=text_m_p.get_rect()
        text_m_p_xy.x=80
        text_m_p_xy.y=200
        DISPLAY_CREATE_MAP.blit(text_m_p,text_m_p_xy)       
        text_c_h_xy=text_c_h.get_rect()
        text_c_h_xy.x=60
        text_c_h_xy.y=300
        DISPLAY_CREATE_MAP.blit(text_c_h,text_c_h_xy)
        text_f_p_s_xy=text_f_p_s.get_rect()
        text_f_p_s_xy.x=65
        text_f_p_s_xy.y=400
        DISPLAY_CREATE_MAP.blit(text_f_p_s,text_f_p_s_xy)

        # mostrar botones
        button1.draw(DISPLAY_CREATE_MAP, fontd)
        large_fila_box.draw_text(DISPLAY_CREATE_MAP) 
        large_columna_box.draw_text(DISPLAY_CREATE_MAP)
        obst_box.draw_text(DISPLAY_CREATE_MAP)
        max_point_box.draw_text(DISPLAY_CREATE_MAP)
        cant_eggs_box.draw_text(DISPLAY_CREATE_MAP)        
        FPS_box.draw_text(DISPLAY_CREATE_MAP)
        save_map_button.draw(DISPLAY_CREATE_MAP,fontd)
        random_mode_button.draw(DISPLAY_CREATE_MAP, fontd)
        start_button.draw(DISPLAY_CREATE_MAP, fontd)
        print(map)
        print()
        pygame.display.flip()
        clock.tick(FPS)


def screen_game_play(map:list[list[int]],x:int,y:int,fps:int,pointmax,eggs_max):

    DISPLAY_PLAY=pygame.display.set_mode((1200,900))
    pygame.display.set_caption("Snake egg-eater")

    font = pygame.font.SysFont('Arial', 24)

    # velosidad de la serpiente
    clock = pygame.time.Clock()
    if fps==None:
        fps=1.5

    # validez si pointmax no tiene valor
    if pointmax==None:
        pointmax=10    

    # inicio de las cordenadas
    pixel_x=64
    pixel_y=64
    move=None
    pixel_xy=64
    numb_xy=64
    score=0
    gen_grow_up_snake_count=0
    body=[0,0]
    collition=True

    # cargando pixeles mapa
    pixel_x=1200//y
    pixel_y=900//x
    if pixel_x>=pixel_y:
        pixel_xy=pixel_y
    else:
        pixel_xy=pixel_x
    #print(pixel_xy)        

    # buscar via para cambiar rl directorio y que varie
    # cargando imagenes
    os.chdir("C:/Users/danny_fiallo/Documents/!!!Programación/!!!Code/Snake/Photos")
    walls=pygame.image.load("walls.jpg") 
    head=pygame.image.load("head.png")
    eggs=pygame.image.load("eggs.png")
    obstacles_img=pygame.image.load("obstacles.png")
    green_image = pygame.Surface((64, 64))
    numb = pygame.font.SysFont('Arial', numb_xy)
    green_image.fill((0, 255, 0))

    scaled_walls,scaled_head,scaled_eggs,scaled_obstacles_img,scaled_green_image,scaled_numbscale_img=scale_img(pixel_xy,pixel_xy,walls,head,eggs,obstacles_img,green_image,numb)

    # buscando la posiccion inicial del snake en la matriz
    for i in range(0,len(map)):
        for j in range(0,len(map[i])):
            if map[i][j]==-3:
                pos_snake_fila=i
                pos_snake_columna=j
                body[0]=i
                body[1]=j

    while True:
        DISPLAY_PLAY.fill(BLACK)
        text_score = font.render(f'Score {score}', True, (255, 255, 255))
         
        for event in pygame.event.get():
            # salida del bucle
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            # condicionales para cambiar de direccion
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Create_map(map,x,y)
                elif event.key==pygame.K_w and move!=2:
                    move=1
                elif event.key==pygame.K_s and move!=1:
                    move=2
                elif event.key==pygame.K_d and move!=4:
                    move=3
                elif event.key==pygame.K_a and move!=3:
                    move=4

        # condicionales del movimiento para colicion y comer huevos
        count=1
        result=choice_move(map, pos_snake_fila, pos_snake_columna, move, gen_grow_up_snake_count, score, collition)
        map, pos_snake_fila, pos_snake_columna, gen_grow_up_snake_count, score, collition = result
        

        # colicion
        if collition==False:
            End_screen(map,x,y,score,eggs_max,pointmax,fps)
         
                                                    
        # generar mas huevos en cuanto se acaben los que hay en el mapa
        count=0
        for ii in range(0,len(map)):
            for jj in range(0,len(map[ii])):
                if map[ii][jj]>0:
                    count+=1            
        if count==0:
            map=eggs_map(map,x-1,y-1,eggs_max,pointmax)

            
        # generar cuerpo   
        if gen_grow_up_snake_count>0 and gen_grow_up_snake_count!=None:
            gen_grow_up_snake_count=body_snake_grow_up(map,x,y,gen_grow_up_snake_count,move,pos_snake_fila,pos_snake_columna,body)
            


        # mov cuerpo
        if move==1:
            map,body=snake_body_move_array(map,body,pos_snake_fila,pos_snake_columna)
        elif move==2:
            map,body=snake_body_move_array(map,body,pos_snake_fila,pos_snake_columna) 
        elif move==3:
            map,body=snake_body_move_array(map,body,pos_snake_fila,pos_snake_columna)
        elif move==4:
            map,body=snake_body_move_array(map,body,pos_snake_fila,pos_snake_columna)


        # esto hay que repararlo
        # condicional del tamaño maximo de las x,y
        show_map(map,DISPLAY_PLAY,scaled_walls,scaled_head,scaled_eggs,scaled_obstacles_img,scaled_green_image,0,pixel_xy,0,scaled_numbscale_img)

        # mostrar el score
        text_rect = text_score.get_rect()
        text_rect.topleft = (10, 10)
        DISPLAY_PLAY.blit(text_score, text_rect) 

        pygame.display.flip()
        clock.tick(fps)

# pantalla de carga de mapas
def load_screen():

    RED_Tono_claro= (255, 128, 128)

    pygame.init()

    VENTANA_ANCHO = 1200
    VENTANA_ALTO = 900
    COLOR_FONDO = (255, 255, 255)
    COLOR_BOTON = (128, 128, 128)
    COLOR_TEXTO = (255, 255, 255)
    MARGEN = 20

    map=None
    obst=None
    eggs=None
    walls=None
    points=None
    fps=None

    DISPLAY_LOAD=pygame.display.set_mode((1200,900))
    pygame.display.set_caption("Snake egg-eater")

    font = pygame.font.SysFont('Arial', 24)
    
    # Obtén los nombres de los archivos de texto en el directorio deseado
    directorio_txt = "C:/Games/Snake/Saves"  # reemplaza esto con la ruta de tu directorio
    nombres_archivos = []
    for archivo in os.listdir(directorio_txt):
        if archivo.endswith(".txt"):
            nombres_archivos.append(archivo[:-4])  # elimina la extensión ".txt"


    # Crea la ventana y los botones
    # Crea la superficie que contiene todos los botones
    superficie_botones = pygame.Surface((VENTANA_ANCHO - 2 * MARGEN, len(nombres_archivos) * 40))
    botones = []
    y = MARGEN
    for nombre_archivo in nombres_archivos:
        boton = Button(0, y, VENTANA_ANCHO - 2 * MARGEN, 30, COLOR_BOTON, nombre_archivo, COLOR_TEXTO, lambda x=nombre_archivo: load_maps(nombre_archivo))
        botones.append(boton)
        boton.draw(superficie_botones, font)
        y += 40

    desplazamiento_y = 0
    velocidad_desplazamiento = 3

    while True:

        DISPLAY_LOAD.fill(RED_Tono_claro)

        for event in pygame.event.get():
            # salida del bucle
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            result = boton.handle_event(event)
            if result is not None:
                map, x, y, obst, eggs, walls, points, fps = result

        # Maneja el desplazamiento de la superficie de los botones
        teclas_pulsadas = pygame.key.get_pressed()
        if teclas_pulsadas[pygame.K_UP]:
            desplazamiento_y += velocidad_desplazamiento
        if teclas_pulsadas[pygame.K_DOWN]:
            desplazamiento_y -= velocidad_desplazamiento
        if desplazamiento_y > 0:
            desplazamiento_y = 0
        if desplazamiento_y < -len(nombres_archivos) * 40 + VENTANA_ALTO - 2 * MARGEN:
            desplazamiento_y = -len(nombres_archivos) * 40 + VENTANA_ALTO - 2 * MARGEN

        # Dibuja la ventana y los botones visibles
        for i, boton in enumerate(botones):
            # Mueve el rectángulo del botón en la ventana según el desplazamiento
            boton.rect.top = MARGEN + i * 40 + desplazamiento_y
            # Dibuja el botón en la posición correcta según el rectángulo del botón
            boton.draw(DISPLAY_LOAD, font)

        if  (map and obst and eggs and walls and points and fps)!=None:
            screen_game_play(map,x,y,eggs,points,fps)

        pygame.display.flip()    


# pantalla de juego perdido
def End_screen(map,x,y,score,eggs,points,fps):

    pygame.init()

    RED_Tono_claro= (255, 128, 128)
    MEDIUM_GREEN = (80, 200, 100)

    DISPLAY_END=pygame.display.set_mode((1200,900))
    pygame.display.set_caption("Snake egg-eater")

    font = pygame.font.SysFont('Arial', 50)

    title= pygame.font.SysFont('Impact', 150)
    text= title.render("Game Over", True, (MEDIUM_GREEN))


    button_save = Button(350, 500, 200, 50, (0,0,255), "Save map", (255, 255, 255), action=lambda: Save_screen(map,x,y,score,None,eggs,None,points,fps,None)) # cambiar
    button_create_map = Button(650, 500, 200, 50, (255,0,0), "Back", (255, 255, 255), action=lambda: Create_map(map,x,y,None,eggs,None,points,fps))

    while True:

        text_score = font.render(f'Score {score}', True, (255, 255, 255))

        DISPLAY_END.fill(RED_Tono_claro)

        for event in pygame.event.get():
            # salida del bucle
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            button_create_map.handle_event(event)
            button_save.handle_event(event)


        button_create_map.draw(DISPLAY_END,font) 
        button_save.draw(DISPLAY_END,font)   

        text_rect = text_score.get_rect()
        text_rect.topleft = (500, 380)
        DISPLAY_END.blit(text_score, text_rect)

        text_rect = text.get_rect()
        text_rect.x = 250
        text_rect.y = 150
        DISPLAY_END.blit(text, text_rect)

        pygame.display.flip()


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
    button_create_map = Button(650, 500, 200, 50, (255,0,0), "Title", (255, 255, 255), action=lambda: main_screen())
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