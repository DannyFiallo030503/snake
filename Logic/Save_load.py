import os



def save_maps(map,x,y,obst,eggs,walls,points,fps,name):
    ruta_games = os.path.join("C:\\", "Games")
    ruta_snake = os.path.join(ruta_games, "Snake")
    ruta_saves = os.path.join(ruta_snake, "Saves")
    ruta_archivo = os.path.join(ruta_saves, name + ".txt")

    if not os.path.exists(ruta_games):
        os.makedirs(ruta_games, exist_ok=True) # esto te ahorra los if

    if not os.path.exists(ruta_snake):
        os.makedirs(ruta_snake)

    if not os.path.exists(ruta_saves):
        os.makedirs(ruta_saves)
    
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(str(map) + "\n")
        archivo.write(str(x) + "\n")
        archivo.write(str(y) + "\n")
        archivo.write(str(obst) + "\n")
        archivo.write(str(eggs) + "\n")
        archivo.write(str(walls) + "\n")
        archivo.write(str(points) + "\n")
        archivo.write(str(fps) + "\n")
    archivo.close()

def load_maps(name):
    ruta_games = os.path.join("C:\\", "Games")
    ruta_snake = os.path.join(ruta_games, "Snake")
    ruta_saves = os.path.join(ruta_snake, "Saves")
    ruta_archivo = os.path.join(ruta_saves, name + ".txt")

    if not os.path.exists(ruta_games) or not os.path.exists(ruta_snake) or not os.path.exists(ruta_saves):
        print("No se encontró el archivo.") # esto despues lo debo de cambiar
    else:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            map=eval(lineas[0])
            x=int(lineas[1])
            y=int(lineas[2])
            obst=int(lineas[3])
            eggs=int(lineas[4])
            walls=int(lineas[5])
            points=int(lineas[6])
            fps=int(lineas[7])
        archivo.close()

        return map,x,y,obst,eggs,walls,points,fps    

