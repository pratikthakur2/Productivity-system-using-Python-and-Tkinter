#import modules

from re import L
from tkinter import *
import os
import pickle
from tkinter.font import BOLD, ITALIC
from tkinter.font import Font
from PIL import ImageTk,Image
from tkinter import filedialog
import PySimpleGUI as sg
import pathlib
import math

import todo3
import notepad
import pomodoro

def mainwin_func():

    # Designing Main(first) window
    
    def main_window():
        global main_screen
        main_screen = Tk()
        main_screen.configure(bg="white")
        main_screen.geometry("600x500")#300x250

        Label(text="hellohello\n\n",bg="white",fg="white").pack()
        main_screen.title("TASK-ON")
        Label(text="hellohello\n\n",bg="white",fg="white").pack()
        Label(text="hello",bg="white",fg="white").pack()

        #PAGE IMAGE
        #opening the image
        #page_img =Image.open("sovlong.png")

        #Resizing the image
        #resized_img = page_img.resize((460,130),Image.ANTIALIAS)

        #Inserting the image
        #new_image =ImageTk.PhotoImage(resized_img)
        #image_label = Label(main_screen,image=new_image)
        #image_label.pack(pady=20)

        Label(text="hello\n\n\n",bg="white",fg="white").pack()
        Label(text="TASK-ON", bg="white",fg="BLACK", width="300", height="2", font=("Verdana",30,BOLD)).pack()

        Label(text="hellohello\n\n",bg="white",fg="white").pack()
        
        #creating a button frame
        button_frame = Frame(main_screen)
        button_frame.pack()

        #DISPLAYING THE BUTTONS

        button_todo = Button(button_frame,text="TO-DO LIST APP",highlightthickness=0, height="5", width="30",bg='#811B98',fg='white',command=todo3.todoyo)

        Label(text="hhello",bg="white",fg="white").pack()

        button_notes = Button(button_frame,text="NOTES APP",highlightthickness=0, height="5", width="30",bg='#811B98',fg='white',command=notepad.notes_func)

        Label(text="hhello",bg="white",fg="white").pack()

        button_notify = Button(button_frame,text="DESKTOP NOTIFIER",highlightthickness=0, height="5", width="30",bg='#811B98',fg='white')

        Label(text="hhello",bg="white",fg="white").pack()

        button_pomo = Button(button_frame,text="POMODORO TIMER",highlightthickness=0,height="5", width="30",bg='#811B98',fg='white',command=pomodoro.pomo_func)

        #ALIGNING ALL THE BUTTONS
        button_todo.grid(row=0,column=0,pady=10)
        button_notes.grid(row=0,column=1,padx=10,pady=10)
        button_notify.grid(row=2,column=0,pady=10)
        button_pomo.grid(row=2,column=1,padx=10,pady=10)

    
        main_screen.mainloop()
    
    
    main_window()