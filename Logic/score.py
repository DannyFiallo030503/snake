# pylint: disable=no-member
# pylint: disable=all 

def calculate_dist(map,x,y):
    dist=20000
    correct_point=0
    for i in range(0,len(map)):
        for j in range(0,len(map[i])):
            if map[i][j]>0 and map[i][j]!=map[x][y]:
                map_x=i
                map_y=j
                map_x=x-map_x
                map_y=y-map_y
                dist_squ=abs(map_x)+abs(map_y)
                point=map[i][j]*100
                if dist_squ<dist:
                    dist=dist_squ
                    correct_point=point
    return correct_point                
