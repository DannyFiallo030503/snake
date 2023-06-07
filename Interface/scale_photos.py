# pylint: disable=no-member
# pylint: disable=all

import pygame

# escala el tamaño de la imagen                    
def scale_img(pixel_x,pixel_y,walls,head,eggs,obstacles_img,green_image,numb):
    scaled_walls=pygame.transform.scale(walls,(pixel_x,pixel_y))
    scaled_head=pygame.transform.scale(head,(pixel_x,pixel_y))
    scaled_eggs=pygame.transform.scale(eggs,(pixel_x,pixel_y))
    scaled_obstacles_img=pygame.transform.scale(obstacles_img,(pixel_x,pixel_y))
    scaled_green_image=pygame.transform.scale(green_image,(pixel_x,pixel_y))
    scaled_numb=pygame.font.SysFont('Arial', pixel_x)
    return scaled_walls,scaled_head,scaled_eggs,scaled_obstacles_img,scaled_green_image,scaled_numb