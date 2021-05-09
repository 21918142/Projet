import tkinter as tk
import random 

# Constante
HEIGHT = 640
WIDTH  = 640
SIZE = 16
COTE = HEIGHT // SIZE


#Variable global
mur_vert = [(COTE, COTE),
            (COTE*2, COTE*10),
            (COTE*3, COTE*4),
            (COTE*3, COTE*8),
            (COTE*4, 0),
            (COTE*4, COTE*15),
            (COTE*5, COTE*9),
            (COTE*5, COTE*12),
            (COTE*6, COTE*14),
            (COTE*7, COTE*2),
            (COTE*7, COTE*5),
            (COTE*9, COTE*12),
            (COTE*10, COTE),
            (COTE*10, COTE*7),
            (COTE*11, 0),
            (COTE*12, COTE*2),
            (COTE*12, COTE*14),
            (COTE*13, COTE*9),
            (COTE*14, COTE*5),
            (COTE*14, COTE*13),
            (COTE*14, COTE*15)
            ]

mur_horiz = [(0, COTE*6),
             (0, COTE*13),
             (COTE, COTE*2),
             (COTE, COTE*11),
             (COTE*2, COTE*5),
             (COTE*2, COTE*8),
             (COTE*4, COTE*12),
             (COTE*5, COTE*10),
             (COTE*6, COTE*2),
             (COTE*6, COTE*14),
             (COTE*7, COTE*5),
             (COTE*9, COTE),
             (COTE*9, COTE*12),
             (COTE*10, COTE*7),
             (COTE*11, COTE*3),
             (COTE*11, COTE*15),
             (COTE*11, COTE*16),
             (COTE*12, COTE*9),
             (COTE*13, COTE*6),
             (COTE*14, COTE*14),
             (COTE*15, COTE*4),
             (COTE*15, COTE*10)
             ]

robots = []
pos_robot = []
trace =[]
#Fonction:

def plateau() :
    x = WIDTH
    y = HEIGHT

    for i in range(0,x,COTE):
        for j in range(0,y,COTE):
            canvas.create_rectangle(i,j,i+COTE,j+COTE,fill="white")

    gen_mur()
    show_robots()

def position(x, y):
    """Coordonéés par 16"""
    return x // COTE, y // COTE

def clic(event):
    """ Permet d'efectuer un deplacement d'1 robot quand on le clique dessus,
    Et restart quand on clique sur le carré milieu """
    global pos_robot, robots, trace
    i, j = position(event.x , event.y)

    if (i,j) == pos_robot[0]:
        print(pos_robot[0])
    if (i,j) == pos_robot[1]:
        print(pos_robot[1])
    if (i,j) == pos_robot[2]:
        print(pos_robot[2])
    if (i,j) == pos_robot[3]:
        print(pos_robot[3])
    trace.append((i,j))
    print(i,j)


def gen_mur():

    x = WIDTH
    y = HEIGHT
    
    # Mur extérieur
    canvas.create_line(0, 0, 0, y, fill = "black", width = 15)
    canvas.create_line(0, 0, x, 0, fill = "black", width = 15)
    canvas.create_line(0, y, x, y, fill = "black", width = 5)
    canvas.create_line(x, 0, x, y, fill = "black", width = 5)

    # Mur au milieu
    canvas.create_rectangle(x/2 - COTE, y/2 + COTE, 
                            x/2 + COTE, y/2 - COTE, fill = "black",
                            outline = "blue")

    # Mur intérieur
    for x, y in mur_vert:
        canvas.create_line(x, y, x, y+COTE, fill="black", width= 5)
        for x, y in mur_horiz:
            canvas.create_line(x, y, x+COTE, y, fill="black", width= 5)

def show_robots():
    """Création des robots + définir leur position """
    global robots, pos_robot

    n = random.randrange(40, 600, 40)
    m = random.randrange(40, 600, 40)

    x = random.randrange(40, 600, 40)
    y = random.randrange(40, 600, 40)

    u = random.randrange(40, 600, 40)
    v = random.randrange(40, 600, 40)

    a = random.randrange(40, 600, 40)
    b = random.randrange(40, 600, 40)

    Blue = canvas.create_oval(n+5, m+5, n+35, m+35, fill="blue")
    Red = canvas.create_oval(x+5, y+5, x+35, y+35, fill="red")
    Yellow = canvas.create_oval(u+5, v+5, u+35, v+35, fill="yellow")
    Green = canvas.create_oval(a+5, b+5, a+35, b+35, fill="green")

    position_bleu = (n//COTE, m//COTE)
    position_red = (x//COTE, y//COTE)
    position_yellow = (u//COTE, v//COTE)
    position_green = (a/COTE, b//COTE)

    pos_robot.append(position_bleu)
    pos_robot.append(position_red)
    pos_robot.append(position_yellow)
    pos_robot.append(position_green)

    robots.append(Blue)
    robots.append(Red)
    robots.append(Yellow)
    robots.append(Green)
 

def deplacement(event):
    global pos_robot, robots, trace
    key = event.keysym
    if trace[0] == pos_robot[0]:
        if key == "Up":
            canvas.move(robots[0], 0, -40)
        elif key == "Down":
            canvas.move(robots[0], 0, 40)
        elif key == "Left":
            canvas.move(robots[0], -40, 0)
        elif key == "Right":
            canvas.move(robots[0], 40, 0)
    
    elif trace[0] == pos_robot[1]:
        if key == "Up":
            canvas.move(robots[1], 0, -40)
        elif key == "Down":
            canvas.move(robots[1], 0, 40)
        elif key == "Left":
            canvas.move(robots[1], -40, 0)
        elif key == "Right":
            canvas.move(robots[1], 40, 0)
    
# prgramme principal

root = tk.Tk()
root.title("Robot Ricochet")

# Creation des widgets
canvas = tk.Canvas(root,height=HEIGHT, width=WIDTH)
bouton = tk.Button(root, text="Génération terrain", command=plateau)


#Placement des widgets
canvas.grid()
bouton.grid()
#Autre

canvas.bind("<1>", clic)
canvas.bind_all("<Key>", deplacement)

#Fin
root.mainloop()
