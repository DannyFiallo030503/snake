# pylint: disable=no-member
# pylint: disable=all
 
from typing import List
from Logic.score import calculate_dist

def body_snake_grow_up(map, x, y, count, move, pos_map_x, pos_map_y, body: list):
    if move==1 and map[pos_map_x+1][pos_map_y]==0 and count>0:
        map[pos_map_x+1][pos_map_y]==-4
        body.insert(0,pos_map_y)
        body.insert(0,pos_map_x)

        count-=1
    elif move==2 and map[pos_map_x-1][pos_map_y]==0 and count>0:
        map[pos_map_x-1][pos_map_y]==-4
        body.insert(0,pos_map_y)
        body.insert(0,pos_map_x)

        count-=1
    elif move==3 and map[pos_map_x][pos_map_y-1]==0 and count>0:
        map[pos_map_x][pos_map_y-1]==-4
        body.insert(0,pos_map_y)
        body.insert(0,pos_map_x)

        count-=1 
    elif move==1 and map[pos_map_x][pos_map_y+1]==0 and count>0:
        map[pos_map_x][pos_map_y+1]==-4
        body.insert(0,pos_map_y)
        body.insert(0,pos_map_x)

        count-=1
    print("count=",count)           
    return count
          

# cambiarlo para que sea leer matrices
def snake_body_move_array(map:list[list[int]], body:list[int], x:int, y:int):

    if len(body)<=2 and map[body[0]][body[1]]==0:
        body[0]=x
        body[1]=y

    elif len(body)>3:
        # correr las posiciones
        body.insert(0,y)
        body.insert(0,x)
        map[body[len(body)-2]][body[len(body)-1]]=0
        body.pop()
        body.pop()
        # poner el cuerpo en el mapa
        for j in range(0,len(body),2):
            map[body[j]][body[j+1]]=-4
        map[body[0]][body[1]]=-3

    return map,body  



def choice_move(map:list[list[int]], pos_snake_fila:int, pos_snake_columna:int, move:int, gen_grow_up_snake_count:int, score:int, collition:bool):      
        if move==1:
            # colicion tengo que cambiarlo para que vaya a otra pantalla    
            if map[pos_snake_fila-1][pos_snake_columna]==-4 or map[pos_snake_fila-1][pos_snake_columna]==-2 or map[pos_snake_fila-1][pos_snake_columna]==-1:
                collition=False  
            # condiccion de comer huevo y crecer
            if map[pos_snake_fila-1][pos_snake_columna]>0:
                gen_grow_up_snake_count+=map[pos_snake_fila-1][pos_snake_columna]
                map[pos_snake_fila-1][pos_snake_columna]=-3
                score+=calculate_dist(map,pos_snake_fila-1,pos_snake_columna)
            # condicion de movimiento del cuerpo
            map[pos_snake_fila-1][pos_snake_columna]=-3
            map[pos_snake_fila][pos_snake_columna]=0
            pos_snake_fila-=1


        elif move==2:
            # colicion tengo que cambiarlo para que vaya a otra pantalla    
            if map[pos_snake_fila+1][pos_snake_columna]==-4 or map[pos_snake_fila+1][pos_snake_columna]==-2 or map[pos_snake_fila+1][pos_snake_columna]==-1:
                collition=False
            # condiccion de comer huevo y crecer
            if  map[pos_snake_fila+1][pos_snake_columna]>0:
                gen_grow_up_snake_count+=map[pos_snake_fila+1][pos_snake_columna]
                gen_grow_up_snake_count+=map[pos_snake_fila+1][pos_snake_columna]
                score+=calculate_dist(map,pos_snake_fila+1,pos_snake_columna)
                # condicion de movimiento del cuerpo
            map[pos_snake_fila+1][pos_snake_columna]=-3
            map[pos_snake_fila][pos_snake_columna]=0
            pos_snake_fila+=1

        elif move==3:
            # colicion tengo que cambiarlo para que vaya a otra pantalla
            if map[pos_snake_fila][pos_snake_columna+1]==-4 or map[pos_snake_fila][pos_snake_columna+1]==-2 or map[pos_snake_fila][pos_snake_columna+1]==-1:
                collition=False
            # condiccion de comer huevo y crecer
            if map[pos_snake_fila][pos_snake_columna+1]>0:
                gen_grow_up_snake_count+=map[pos_snake_fila][pos_snake_columna+1]
                gen_grow_up_snake_count+=map[pos_snake_fila][pos_snake_columna+1]
                score+=calculate_dist(map,pos_snake_fila,pos_snake_columna+1)
                # condicion de movimiento del cuerpo
            map[pos_snake_fila][pos_snake_columna+1]=-3
            map[pos_snake_fila][pos_snake_columna]=0
            pos_snake_columna+=1
            
        elif move==4:
            # colicion tengo que cambiarlo para que vaya a otra pantalla
            if map[pos_snake_fila][pos_snake_columna-1]==-4 or map[pos_snake_fila][pos_snake_columna-1]==-2 or map[pos_snake_fila][pos_snake_columna-1]==-1:
                collition=False
            # condiccion de comer huevo y crecer
            if map[pos_snake_fila][pos_snake_columna-1]>0:
                gen_grow_up_snake_count+=map[pos_snake_fila][pos_snake_columna-1]
                gen_grow_up_snake_count+=map[pos_snake_fila][pos_snake_columna-1]
                score+=calculate_dist(map,pos_snake_fila-1,pos_snake_columna-1)
                # condicion de movimiento del cuerpo
            map[pos_snake_fila][pos_snake_columna-1]=-3
            map[pos_snake_fila][pos_snake_columna]=0
            pos_snake_columna-=1

        return map, pos_snake_fila, pos_snake_columna, gen_grow_up_snake_count, score, collition                             
            