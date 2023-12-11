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




# ⬇️ Create a label and print it on the Right frame ⬇️
def create_label(device):
    print(device)
    label = Label(canvas, text=f"{device}", bd=2, relief="solid")
    label.pack()
    print("Label created")

    # ⬇️ Bind the label to move it and to have toolbar ⬇️
    label.bind("<Alt-Button-1>", on_label_press)
    label.bind("<Alt-B1-Motion>", on_label_drag)
    label.bind("<Alt-ButtonRelease-1>", on_label_release)
    label.bind("<Button-3>", menu_objects)
    label.bind("<Button-1>", first_point)
    label.bind("<Shift-Button-1>", Shift_second_point)
    label.bind("<Control-Button-1>", CTRL_first_point)
    label.bind("<Control-Shift-Button-1>", CTRL_Shift_second_point)






# ⬇️ Press the label to move ⬇️
def on_label_press(event):
    global dragged_label
    dragged_label = event.widget
    dragged_label.start_x = event.x
    dragged_label.start_y = event.y

# ⬇️ Move the mouse ⬇️
def on_label_drag(event):
    global start_point
    delta_x = event.x - dragged_label.start_x
    delta_y = event.y - dragged_label.start_y
    x = dragged_label.winfo_x() + delta_x
    y = dragged_label.winfo_y() + delta_y
    dragged_label.place(x=x,y=y)

# ⬇️ Release the label ⬇️
def on_label_release(event):
    global dragged_label
    dragged_label = None






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



# ⬇️ Delete the label ⬇️
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

    # ⬇️ Create the properties entry for change icon ⬇️


    # ⬇️ Create the properties entry for change port numbers ⬇️
    label_port = ttk.Label(FRAME_PROPERTIES, text="Port :")
    label_port.grid(row=1, column=0)
    port = StringVar()
    change_port = ttk.Entry(FRAME_PROPERTIES, textvariable=port)
    change_port.grid(row=1, column=1)

    # ⬇️ Create the validate modifications button ⬇️
    validate=ttk.Button(FRAME_PROPERTIES, text="Valider", command=save_properties)
    validate.grid(row=2, column=0)

    # ⬇️ Create the cancel modifications button ⬇️
    cancel=ttk.Button(FRAME_PROPERTIES, text="Annuler", command=FRAME_PROPERTIES.destroy)
    cancel.grid(row=2, column=1)





    # ⬇️ Start the Properties event loop ⬇️
    FRAME_PROPERTIES.mainloop()







# ⬇️ Get the first point ⬇️
def first_point(event):
    global start_point
    print("line")
    start_point = event.widget.winfo_x(), event.widget.winfo_y()
    print(start_point)

    for n in range(10):
        print(start_point)

# ⬇️ Get the second point and create the line ⬇️
def Shift_second_point(event):
    global end_point
    print("line")
    end_point = event.widget.winfo_x(), event.widget.winfo_y()
    print(end_point)

    canvas.create_line(start_point, end_point, fill="blue", width=2)







# Temporary line object
temp_line = None

# Get the first point
def CTRL_first_point(event):
    global start_point , point_start_name
    point_start_name=event.widget.cget("text")
    print(point_start_name)
    print("line")
    start_point = event.widget.winfo_x(), event.widget.winfo_y()
    print(start_point)

# Update the line while dragging
# def on_label_drag(event):
#     global temp_line, start_point, end_point
#     canvas.delete("horizontal")
#     canvas.delete("vertical")
#     if dragged_label is start_point:
#         delta_x = event.x - dragged_label.start_x
#         delta_y = event.y - dragged_label.start_y
#         x = dragged_label.winfo_x() + delta_x
#         y = dragged_label.winfo_y() + delta_y
#         dragged_label.place(x=x,y=y)
#     elif dragged_label is end_point:
#         delta_x = event.x - dragged_label.start_x
#         delta_y = event.y - dragged_label.start_y
#         x = dragged_label.winfo_x() + delta_x
#         y = dragged_label.winfo_y() + delta_y
#         dragged_label.place(x=x,y=y)



    # # Update the temporary line
    # if temp_line is not None:
    #     canvas.delete(temp_line)
    # temp_line = None

    # # Create horizontal and vertical lines
    # horizontal_line = canvas.create_line(start_point[0], start_point[1], x, start_point[1], fill="black", width=2, tags="horizontal")
    # vertical_line = canvas.create_line(x, start_point[1], x, y, fill="black", width=2, tags="vertical")
    # temp_line = (horizontal_line, vertical_line)





# Get the second point and create the line
def CTRL_Shift_second_point(event):
    global start_point, temp_line, horizontal_1, horizontal_2, vertical_1, vertical_2, point_end_name
    point_end_name=event.widget.cget("text")
    print("line")

    horizontal_1= (start_point[0], start_point[1])
    horizontal_2= (event.widget.winfo_x(), start_point[1])

    vertical_1= (event.widget.winfo_x(), event.widget.winfo_y())
    vertical_2= (event.widget.winfo_x(), start_point[1])

    check_if_line_between_points_exists(event)

# Set to store existing lines
existing_lines = set()
print(existing_lines, " : 1")

def check_if_line_between_points_exists(event):
    global point_start_name, point_end_name
    print(point_start_name)
    print(point_end_name)
    name_start=point_start_name
    name_end=point_end_name
    print(f"name1 = {name_start},name2=  {name_end}")
    print("check")
    print(existing_lines, " : 2")
    if point_start_name == point_end_name:
        print("same")
        canvas.delete("horizontal")
        canvas.delete("vertical")
    elif (name_start, name_end) in existing_lines or (name_end, name_start) in existing_lines:
        print("line already exists")
        print(existing_lines, " : 3")
    else:
        print("different")
        create_line(event)




def create_line(event):
    global point_start_name, point_end_name, existing_lines
    # Create the final line
    if existing_lines == {(point_start_name, point_end_name)}:
        print("line already exists can't create antoher one")
        print(existing_lines, " : 4")
    else:
        existing_lines.add((point_start_name, point_end_name))
        canvas.create_line(horizontal_1,horizontal_2, fill="black", width=2, tags="horizontal")
        canvas.create_line(vertical_1, vertical_2, fill="black", width=2, tags="vertical")
        print(existing_lines, " : 5")



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
