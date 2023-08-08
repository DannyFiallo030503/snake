# pylint: disable=no-member
# pylint: disable=all
import random

# generate the size of the map, for example 25x25 squeres and generete the walls of the map
def largue_map(x:int,y:int)->list[list[int]]:

    map=[]

    for i in range(0,x):
        map.append([])
        if i==0 or i==x-1:
            for j in range(0,y):
                map[i].append(-2)
            continue
        for ii in range(0,y):
            if ii==0 or ii==y-1:
                map[i].append(-2)
            else:
                map[i].append(0)  
    return map
    

# generete the obstacles of the map
def obstacles(map:list[list[int]], x:int, y:int,blocks:int):

    count=0
    cord_x=0
    cord_y=0

    if blocks==0:
        return map
    
    while count<blocks:
        if (x and y)>2 and blocks<(x+y)/2:
            num_aleatorio = random.randint(0, x)
            cord_x=int(num_aleatorio)
            num_aleatorio = random.randint(0, y)
            cord_y=int(num_aleatorio)
        else:
            return map   
        if map[cord_x][cord_y]==0:
            map[cord_x][cord_y]=-1
            count=count+1
    return map
             
# genera los huevos en el mapa
def eggs_map(map:list[list[int]], x:int, y:int, eggs:int, maximus_points:int):
    count=0
    cord_x=0
    cord_y=0
    if eggs==None:
        eggs=0

    while count<eggs:
        if (x and y)>2:
            num_aleatorio = random.randint(0, x)
            cord_x=int(num_aleatorio)
            num_aleatorio = random.randint(0, y)
            cord_y=int(num_aleatorio)
               
        if map[cord_x][cord_y]==0:
            map[cord_x][cord_y]=max_points(maximus_points)
            count=count+1
    return map

# genera numeros aleatorios de 0 hasta el maximo elejido
def max_points(maximus_points:int):
    numb_points=random.randint(1,maximus_points)
    return numb_points

#genera la cabeza de la serpiente
def snake_character(map:list[list[int]], x:int, y:int):
    pos_x = random.randint(0, x-1)
    pos_y = random.randint(0, y-1)
    while map[pos_x][pos_y] != 0: # Si la posición ya está ocupada, se generan nuevas posiciones aleatorias
        pos_x = random.randint(0, x-1)
        pos_y = random.randint(0, y-1)
    map[pos_x][pos_y] = -3 # Se asigna el valor -3 a la posición de la cabeza de la serpiente
    return map

# genera el mapa completo de manera aleatoria
def random_map(tipe_map: bool):
    x_rand=random.randint(6,100)
    y_rand=random.randint(6,100)
    if tipe_map == True:
        map=largue_map(x_rand,y_rand)
        map=snake_character(map,x_rand,y_rand)
    if tipe_map == False:
        map=large_map_no_wall(x_rand,y_rand)
        map=snake_character(map,x_rand,y_rand)    


    if x_rand>y_rand:
        obst_rand=random.randint(0,(y_rand))
    elif y_rand>x_rand:
        obst_rand=random.randint(0,(x_rand))
    elif x_rand==y_rand:
        obst_rand=random.randint(0,(y_rand))
    map=obstacles(map,x_rand-1,y_rand-1,obst_rand)
     

    points_rand=random.randint(0,100)
    
    if x_rand>y_rand:
        eggs_rand=random.randint(0,(y_rand))
    elif y_rand>x_rand:    
        eggs_rand=random.randint(0,(x_rand))
    elif x_rand==y_rand:
        eggs_rand=random.randint(0,(x_rand))
    map=eggs_map(map,x_rand-1,y_rand-1,eggs_rand-1,points_rand)


    if x_rand>y_rand:
        fps_rand=random.randint(1,((20*x_rand)//100))
    elif y_rand>x_rand:
        fps_rand=random.randint(1,((20*y_rand)//100))
    elif x_rand==y_rand:
        fps_rand=random.randint(1,((20*x_rand)//100))

    return (map,x_rand,y_rand,fps_rand,points_rand,eggs_rand)        

def large_map_no_wall ( x: int, y: int ) -> list[list[int]]:

    map = []

    for i in range ( 0, x ):
        map.append([])
        for j in range ( 0, y ):
            map[i].append(0)

    return map        
