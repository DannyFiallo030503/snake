# pylint: disable=no-member
# pylint: disable=all
 


def body_snake_grow_up(map,x,y,count,move,pos_map_x,pos_map_y,body):
    if move==1 and map[pos_map_x+1][pos_map_y]==0 and count>0:
        map[pos_map_x+1][pos_map_y]==-4
        body.append([0,0])

        count-=1
    elif move==2 and map[pos_map_x-1][pos_map_y]==0 and count>0:
        map[pos_map_x-1][pos_map_y]==-4
        body.append([0,0])

        count-=1
    elif move==3 and map[pos_map_x][pos_map_y-1]==0 and count>0:
        map[pos_map_x][pos_map_y-1]==-4
        body.append([0,0])

        count-=1 
    elif move==1 and map[pos_map_x][pos_map_y+1]==0 and count>0:
        map[pos_map_x][pos_map_y+1]==-4
        body.append([0,0])

        count-=1
    print("count=",count)           
    return count

def snake_body_move(map,x,y,move):
    count=0
    if move==1:
        while True:
            if map[x+1][y]==-4:
                map[x][y]=-4
                map[x+1][y]=0
                x=x+1
            elif map[x][y+1]==-4:
                snake_body_move(map,x,y+1,4)
            elif  map[x][y-1]==-4:
                snake_body_move(map,x,y-1,3)
            elif map[x-1][y]==-4:
                snake_body_move(map,x-1,y,1)          
    elif move==2:
        ...
    elif move==3:
        ...
    elif move==4:
        ...            

# cambiarlo para que sea leer matrices
def snake_body_move_array(map,body,x,y):

    if len(body)<=2 and map[body[0]][body[1]]==0:
        body[0]=x
        body[1]=y

    elif len(body)>2:
        body[len(body)-1]=0
        body[len(body)-2]=0
        # correr las posiciones
        for i in range(len(body)-3,0,2):
            print("i=",i)
            body[i+2]=body[i]
            body[i+1]=body[i-1]
        body[0]=x
        body[1]=y
        # poner el cuerpo en el mapa
        for j in range(2,len(body),2):
            map[body[j]][body[j+1]]=-4

    return map,body        

            