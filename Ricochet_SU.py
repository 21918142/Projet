import tkinter as tk

# Constante
HEIGHT = 640
WIDTH  = 640
COTE = 40

#Variable global
point = []

#Fonction:

def plateau() :
    """taille 16x16"""
    x = WIDTH
    y = HEIGHT

    for i in range(0,x,COTE):
        for j in range(0,y,COTE):
            canvas.create_rectangle(i,j,i+COTE,j+COTE,fill="white")

    # Mur extérieur
    canvas.create_line(0, 0, 0, y, fill = "black", width = 15)
    canvas.create_line(0, 0, x, 0, fill = "black", width = 15)
    canvas.create_line(0, y, x, y, fill = "black", width = 5)
    canvas.create_line(x, 0, x, y, fill = "black", width = 5)

    # Mur au milieu
    canvas.create_rectangle(x/2 - COTE, y/2 + COTE, 
                            x/2 + COTE, y/2 - COTE, fill = "black",
                            outline = "blue")
    

def position(x, y):
    return x // COTE, y // COTE

def cherche_position(event) :
    i, j = position(event.x , event.y)
    print(i, j)


# prgramme principal

root = tk.Tk()
root.title("Robot Ricochet")

# Creation des widgets
canvas = tk.Canvas(root,height=HEIGHT, width=WIDTH)

#Placement des widgets
canvas.grid()

#Autre
plateau()
canvas.bind("<1>", cherche_position)


#Fin
root.mainloop()
