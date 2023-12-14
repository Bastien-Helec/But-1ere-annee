from tkinter import *
from tkinter import ttk

# Exercice 1: 
# nbr=0
# Frame1=Tk()
# Frame1.title("Exercice 1")

# def plus():
#     global nbr
#     nbr+=1
#     labnbr.config(text=f"Nombre {nbr}")
# def moins():
#     global nbr
#     nbr-=1
#     labnbr.config(text=f"Nombre {nbr}")

# btnmoins=ttk.Button(Frame1, text="-", command=moins)

# btnmoins.grid(row=0, column=0)

# labnbr= ttk.Label(Frame1, text=f"Nombre {nbr}")
# labnbr.grid(row=0, column=1)

# btnplus=ttk.Button(Frame1, text="+", command=plus)
# btnplus.grid(row=0, column=2)

# Frame1.mainloop()


# Exercice 2:



Frame2=Tk()
Frame2.title("Exercice 2")


labeltitle=ttk.Label(Frame2, text="Veuillez entrer votre Email :")
labeltitle.grid()

lstate=ttk.Label(Frame2, text="Etat :")

mail= StringVar()
entrymail=ttk.Entry(Frame2, textvariable=mail)
entrymail.grid()

def backup_on_terminal():
    print(mail.get())


validate=ttk.Button(Frame2, text="Valider", command=backup_on_terminal)
validate.grid()
validate.config(state="disabled")

checking=int
def check ():
    if "@" not in mail.get():
        checking=1
        return checking
    
    elif "." not in mail.get():
        checking=2
        return checking
    
    elif " " in mail.get():
        checking=3
        return checking
    else:
        checking=0
        return checking


def unlock(event):
    checking=check()
    if checking==0:
        validate.config(state="normal")
        lstate.config(text="Email valide")
        lstate.grid(row=3, column=0)

    else:
        lstate.config(text="Email non valide")
        lstate.grid(row=3, column=0)
        validate.config(state="disabled")

entrymail.bind("<KeyRelease>", unlock)





Frame2.mainloop()