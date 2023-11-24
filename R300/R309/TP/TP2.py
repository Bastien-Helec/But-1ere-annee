from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
#Exercie 1 

#1.1 

# Ct=Téléphone
# CO=Ordinateur
# S= Switch
# R= Routeur
# # Realisation d'une page avec plusieurs fenetres permettant de faire des schémas réseaux

root = Tk()
root.geometry('500x300')

my_paned = PanedWindow(root, orient="horizontal")
my_paned.pack(fill="both", expand=True)

left_pane = Frame(my_paned , background="beige", width=100, height=200)
right_pane = Frame(my_paned , background="beige", width=200, height=200)

my_paned.add(left_pane)
my_paned.add(right_pane)


client=Label(left_pane, text="Client")
router=Label(left_pane, text="Router")
switch=Label(left_pane, text="Switch")
client2=Label(right_pane, text="Client")
router2=Label(right_pane, text="Router")
switch2=Label(right_pane, text="Switch")

client.tag="client"
router.tag="router"
switch.tag="switch"
client2.tag="client2"
router2.tag="router2"
switch2.tag="switch2"


client.grid(row=0,column=1)
router.grid(row=1,column=1)
switch.grid(row=2,column=1)


def anywhere_object_deplacement(event): 
    event.widget.place(x=event.x, y=event.y)

def move_client(event):
    client2 = Label(right_pane, text="Client")
    client2.grid()
    client2.bind("<B1-Motion>", anywhere_object_deplacement)
    client2.bind("<Button-3>", menu_objects)

def move_router(event):
    router2 = Label(right_pane, text="Router")
    router2.grid()
    router2.bind("<B1-Motion>", anywhere_object_deplacement)

def move_switch(event):
    switch2 = Label(right_pane, text="Switch", id="switch2")
    switch2.grid()
    switch2.bind("<B1-Motion>", anywhere_object_deplacement)

def delete_object():
    print("delete")
    

def properties_object():
    print("properties")
    Frame2=Tk()
    Frame2.geometry('500x300')
    Frame2.title("Properties")
    Label(Frame2, text="Properties").pack()

    Frame2.mainloop()


menu = Menu(right_pane, tearoff=0)
menu.add_command(label="Delete", command=delete_object)
menu.add_separator()
menu.add_command(label="Properties", command=properties_object)

def menu_objects(event):
    try :
        print(widget.item(curItem)["tags"])
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()



client.bind("<Button-1>", move_client)
client.bind('<c>', move_client)
router.bind("<Button-1>", move_router)
router.bind('<r>', move_router)
switch.bind("<Button-1>", move_switch)
switch.bind('<s>', move_switch)



client2.bind("<Button-3>", menu_objects)
router2.bind("<Button-3>", menu_objects)
switch2.bind("<Button-3>", menu_objects)




root.mainloop()