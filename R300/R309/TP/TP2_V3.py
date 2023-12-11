from tkinter import *
from tkinter import ttk

# ⬇️ Variable of devices ⬇️
devices = ["Client","Router","Switch"]


# ⬇️ Functions ⬇️

# ⬇️ Resize frames ⬇️
def on_resize(event):
    # Get the new size of the root window
    width = event.width
    height = event.height
    # Adjust the size of the left frame based on the root window size
    LEFT_FRAME.config(height=height)
    
    # Adjust the size of the main frame based on the root window size
    RIGHT_FRAME.config(width=width - LEFT_FRAME.winfo_width(), height=height)

# ⬇️ Get the selected device and create a label ⬇️
def on_device_selected_listbox(event):
    selected_index = device_list.curselection()
    print(selected_index)
    if selected_index:
        selected_device = device_list.get(selected_index)
        print(selected_device)
        create_label(selected_device)

# ⬇️ Press the label to move ⬇️
def on_label_press(event):
    global dragged_label
    dragged_label = event.widget
    dragged_label.start_x = event.x
    dragged_label.start_y = event.y

# ⬇️ Move the mouse ⬇️
def on_label_drag(event):
    delta_x = event.x - dragged_label.start_x
    delta_y = event.y - dragged_label.start_y
    x = dragged_label.winfo_x() + delta_x
    y = dragged_label.winfo_y() + delta_y
    dragged_label.place(x=x,y=y)

# ⬇️ Release the label ⬇️
def on_label_release(event):
    global dragged_label
    dragged_label = None

# ⬇️ Create a label and print it on the Right frame ⬇️
def create_label(device):
    print(device)
    label = Label(canvas, text=f"{device}", borderwidth=2, relief="solid")
    label.pack()
    print("Label created")

    # ⬇️ Bind the label to move it and to have toolbar ⬇️
    label.bind("<Alt-Button-1>", on_label_press)
    label.bind("<Alt-B1-Motion>", on_label_drag)
    label.bind("<Alt-ButtonRelease-1>", on_label_release)
    label.bind("<Button-3>", menu_objects)
    label.bind("<Button-1>", objects_links)

# ⬇️ Menu toolbar ⬇️
def menu_objects(event):
    global selected_label
    print("menu")
    selected_label = event.widget
    menu = Menu(ROOT_FRAME, tearoff=0)
    menu.add_command(label="Delete", command=delete_object)
    menu.add_command(label="Properties", command=properties_object)
    # menu.add_command(label="line", command=objects_links)
    menu.post(event.x_root, event.y_root)

def delete_object():
    global selected_label
    print("delete")
    selected_label.destroy()

# ⬇️ Properties modifications ⬇️
def properties_object():
    print("properties")
    
    def on_resize(event):
        # Get the new size of the root window
        width = event.width
        height = event.height
        # Adjust the size of the left frame based on the root window size
        FRAME_PROPERTIES.config(height=height, width=width)
    
    # ⬇️ Save the properties modifications ⬇️
    def save_properties():
        selected_label.config(text=f"{change_name.get()}")
        FRAME_PROPERTIES.destroy()
    # ⬇️ Create the properties frame ⬇️
    FRAME_PROPERTIES=Tk()
    FRAME_PROPERTIES.geometry('400x200')
    FRAME_PROPERTIES.title("Properties")

    # ⬇️ Create the properties entry for change name  ⬇️
    label_name = ttk.Label(FRAME_PROPERTIES, text="Name :")
    label_name.grid(row=0, column=0)
    name = StringVar()
    change_name = ttk.Entry(FRAME_PROPERTIES, textvariable=name)
    change_name.grid(row=0, column=1)

    # ⬇️ Create the properties entry for change icone ⬇️



    # ⬇️ Create the validate modifications button ⬇️
    validate=ttk.Button(FRAME_PROPERTIES, text="Valider", command=save_properties)
    validate.grid(row=1, column=0)

    # ⬇️ Create the cancel modifications button ⬇️
    cancel=ttk.Button(FRAME_PROPERTIES, text="Annuler", command=FRAME_PROPERTIES.destroy)
    cancel.grid(row=1, column=1)


    # ⬇️ Start the properties event loop ⬇️
    FRAME_PROPERTIES.mainloop()

# ⬇️ Objects links function ⬇️
def objects_links(event):
    global start
    print("line")

    start_x = event.widget.winfo_x()
    start_y = event.widget.winfo_y()

    # init du premier point
    start_point = (start_x, start_y)
    print(start_point)

    # ⬇️ Bind the motion and release events for drawing lines ⬇️
    canvas.bind("<B1-Motion>", lambda e: draw_line(start_point, e, event))
    canvas.bind("<ButtonRelease-1>", lambda e: finish_line(start_point, e))

def draw_line(start_point, event, original_event):
    x, y = event.x, event.y
    canvas.delete("current_line")

    # Adjust the position to make the line straight
    x_diff = abs(x - start_point[0])
    y_diff = abs(y - start_point[1])

    if x_diff > y_diff:
        # If the horizontal distance is greater, adjust the y-coordinate
        y = start_point[1]
    else:
        # If the vertical distance is greater, adjust the x-coordinate
        x = start_point[0]

    canvas.create_line(start_point[0], start_point[1], x, y, tags="current_line")

def finish_line(start_point, event):
    x, y = event.x, event.y
    canvas.create_line(start_point[0], start_point[1], x, y) 
    canvas.delete("current_line")



# ⬇️ Double Click Pressed ⬇️ 
def on_double_click(event):

    # If the user double click on listbox device
    if device_list.curselection():
        on_device_selected_listbox(event)
    print("Double click")

# ⬇️ Enter key Pressed ⬇️
def on_enter_key(event):
    
    # If the user pressed enter on listbox device
    if device_list.curselection():
        on_device_selected_listbox(event)
    print("Enter key")



# ⬇️ Root frame ⬇️
ROOT_FRAME = Tk()
ROOT_FRAME.title("Draw Your Network - DYN")
ROOT_FRAME.grid()

# ⬇️ Left frame ⬇️
LEFT_FRAME = Frame(ROOT_FRAME, bg="white", width=250, bd=2, relief="solid")
LEFT_FRAME.grid(row=0, column=0, sticky="ns")
LEFT_FRAME.pack(side=LEFT, fill=Y)

device_list = Listbox(LEFT_FRAME, bg="lightblue")
for n in devices:
    device_list.insert(END, n)
    print(n)
device_list.pack(side=TOP, fill=Y)

# ⬇️ Right frame ⬇️
RIGHT_FRAME = Frame(ROOT_FRAME, bg="white")
RIGHT_FRAME.pack(side=LEFT, fill=BOTH, expand=True)
canvas=Canvas(RIGHT_FRAME, bg="white")
canvas.pack(fill=BOTH, expand=True)


# ⬇️ Key bindings ⬇️
#Double left click
device_list.bind("<Double-Button-1>", on_double_click)

# ⬇️ Enter key pressed ⬇️
device_list.bind("<Return>", on_enter_key)

# ⬇️ Start the Tkinter event loop ⬇️
ROOT_FRAME.mainloop()
