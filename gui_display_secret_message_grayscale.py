## Import Required Packages
from tkinter import *
import tkinter as tk

## Function to Create GUI for Displaying Secret Message - GrayScale
def displayGrayScaleSecretMessage():
    gui_window = Tk()
    gui_window.title('Patient Details(Displaying Secret Message) - GrayScale')
    gui_window.geometry("500x300")

    ## Create the Input Fields
    ## Text Box Creation
    textbox_label = Label(gui_window, text='Secret Message  :',font=("Times New Roman", 15))
    textbox_input = Text(gui_window,width = 30,height=6)
    textbox_input.pack()
    textbox_label.place(x=20,y=70)
    textbox_input.place(x=170,y=73)

    ## Open a Text File in Read Mode and Read the Extracted Secret Message from the File
    with open("ext_output.txt", "r") as file:
        content=file.read()
        textbox_input.insert(tk.END,content)

    ## Running The GUI
    gui_window.mainloop()

#displayGrayScaleSecretMessage()