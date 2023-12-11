import tkinter as tk

def dessiner_ligne(canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, width=2, fill="blue")

def on_clic(event):
    global point1, point2
    if point1 is None:
        point1 = (event.x, event.y)
    else:
        point2 = (event.x, event.y)
        dessiner_ligne(canvas, point1[0], point1[1], point2[0], point2[1])
        # Réinitialiser les points après avoir dessiné la ligne
        point1, point2 = None, None

# Initialisation de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Dessiner une ligne entre deux points")

# Initialisation du Canvas
canvas = tk.Canvas(fenetre, width=400, height=300, bg="white")
canvas.pack()

# Initialisation des points
point1, point2 = None, None

# Lier l'événement clic de la souris à la fonction on_clic
canvas.bind("<Button-1>", on_clic)

# Démarrer la boucle principale Tkinter
fenetre.mainloop()
