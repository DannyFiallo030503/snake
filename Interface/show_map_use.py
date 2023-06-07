# pylint: disable=no-member
# pylint: disable=all
import pygame
import sys


def show_map(map,DISPLAY,walls,head,eggs,obstacles_img,green_image,grid_x,cell_size,grid_y,numb):
    if map!=None:
        for i in range(0,len(map)):
            for j in range(0,len(map[i])):
                if map[i][j]==-2:
                    DISPLAY.blit(walls, (grid_x + j * cell_size, grid_y + i * cell_size))
                elif map[i][j]==-3:
                    DISPLAY.blit(head, (grid_x + j * cell_size, grid_y + i * cell_size))
                elif map[i][j]>0:
                    DISPLAY.blit(eggs, (grid_x + j * cell_size, grid_y + i * cell_size))
                    DISPLAY.blit((numb.render(str(map[i][j]), True, (255, 255, 255))), (grid_x + j * cell_size, grid_y + i * cell_size))
                elif map[i][j]==-1:
                    DISPLAY.blit(obstacles_img, (grid_x + j * cell_size, grid_y + i * cell_size))
                elif map[i][j]==0:
                    DISPLAY.blit(green_image, (grid_x + j * cell_size, grid_y + i * cell_size))