from tkinter import *
from tkinter.font import BOLD, Font
from tkinter import filedialog
import pickle

def todoyo():
    root = Tk()
    root.title('Todo now')
    root.configure(bg='white')
    root.iconbitmap('C:/Users/admin/Downloads/sovlong.PNG')
    root.geometry("550x400")

    #defining the fonts
    my_font = Font(family="Verdana",
                    size=15,
                    weight="bold")
    button_fonts = Font(family="Verdana",
                        size=7,
                        weight = "bold"
                        )

    #creating a frame
    my_frame = Frame(root)
    my_frame.pack(pady=10)

    #creating a listbox
    my_list = Listbox(my_frame,
                    font = my_font,
                    width= 37,
                    height= 7,
                    bg= "#7E15D6",
                    bd=0,             #border
                    fg="white",
                    highlightthickness=0,
                    selectbackground="#5D1797",
                    activestyle="none"
                    )
    my_list.pack(side=LEFT,fil=BOTH)

    #Creating a dummy list
    stuff = ["Eat","Sleep","study","Go out","Run","Drink"]

    #for loop to insert dummy list items in the todo list
    for item in stuff:
        my_list.insert(END, item)

    #creating a scroll bar
    my_scrollbar = Scrollbar(my_frame)
    my_scrollbar.pack(side=RIGHT,fill=BOTH)

    #add scrollbar
    my_list.config(yscrollcommand=my_scrollbar.set)
    my_scrollbar.config(command=my_list.yview)

    #create an entry box to add items
    my_entry = Entry(root,fg="#5D1797",font=("Verdana",18,BOLD),width=25) 
    my_entry.pack(pady=20)

    #creating a button frame
    button_frame = Frame(root)
    button_frame.pack(pady=20)

    #DEFINING THE FUNCTIONS

    def delete_item():
        my_list.delete(ANCHOR)  
        #deletes whatever is highlighted in the list

    def add_item():
        my_list.insert(END,my_entry.get())
        my_entry.delete(0,END)

    def cross_off_item():
        # cross of the item
        my_list.itemconfig(
            my_list.curselection(),
            fg="#270632")
            #get rid of the selection bar
        my_list.selection_clear(0,END)


    def uncross_item():
        #uncross item
        my_list.itemconfig(
            my_list.curselection(),
            fg="white"
        )
        #getting the selection bar
        my_list.selection_clear(0,END)

    def delete_crossed():
        #deleting all the crossed
        #print(my_list.size())
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count,"fg")=="#270632":
                my_list.delete(my_list.index(count))
            else:
                count +=1

    def save_list():
        file_name=filedialog.asksaveasfilename()
        initialdir="D:/Mini project/Data",
        title="Save File",
        filetypes=(
                    ("Dat Files","*.dat"),
                    ("All Files","*.*"))
        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name = f'{file_name}.dat'

            #delete crossed off items before saving
            count = 0
            while count < my_list.size():
                if my_list.itemcget(count,"fg")=="#270632":
                    my_list.delete(my_list.index(count))
                else:
                    count +=1
            
            #get all the stuff from the list
            stuff = my_list.get(0,END)

            #Open the file
            output_file = open(file_name,'wb')

            #adding the stuff to the file
            pickle.dump(stuff,output_file)




    def open_list():
        file_name = filedialog.askopenfilename(
            initialdir="D:/Mini project/Data",
            title="Save File",
            filetypes=(
                        ("Dat Files","*.dat"),
                        ("All Files","*.*")
                    )
        )
        if file_name:
            #delete currently opened list
            my_list.delete(0,END)

            #open the file
            input_file = open(file_name,'rb')

            #load the data from the file
            stuff = pickle.load(input_file)

            #output stuff to the screen
            for item in stuff:
                my_list.insert(END,item)

    def delete_list():
        my_list.delete(0,END)

    #Create Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    #Adding items to the menu
    file_menu = Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="FIle",menu=file_menu)
    #Adding dropdown items
    file_menu.add_command(label="Save list",command=save_list)
    file_menu.add_command(label="Open list",command=open_list)
    file_menu.add_separator()
    file_menu.add_command(label="Clear list",command=delete_list)


    #ADDING ALL THE BUTTONS ON THE WINDOW

    #delete button 
    delete_button = Button(button_frame, 
                            text="Delete",font=button_fonts,
                            bg="#8038AB",fg="white",command=delete_item)

    #button to add items    
    add_button = Button(button_frame,
                        text="Add",
                        font=button_fonts,
                        bg="#8038AB",fg="white",command=add_item)

    #button to cross off the items
    cross_off_button = Button(button_frame, 
                            text="Cross off",
                            font=button_fonts,
                            bg="#8038AB",fg="white",
                            command=cross_off_item)

    #button to uncross the items
    uncross_button = Button(button_frame, 
                            text="Uncross",font=button_fonts,
                            bg="#8038AB",fg="white",command=uncross_item)

    #button to delete all the items 
    delete_crossed_button = Button(button_frame,
    text="Delete crossed",
                            font=button_fonts,
                            bg="#8038AB",fg="white",command=delete_crossed)


    #ALIGNING ALL THE BUTTONS
    delete_button.grid(row=0,column=0)
    add_button.grid(row=0,column=1,padx=20)
    cross_off_button.grid(row=0,column=2)
    uncross_button.grid(row=0,column=3,padx=20)
    delete_crossed_button.grid(row=0,column=4)

    root.mainloop()