## Import Required Packages
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

## Function to Create GUI for Selecting Stego Image - GrayScale
def selectGrayScaleStegoGUI():
    ## Function to Close Window
    def close_window():
        if (dropdownbox_input.current() != -1):
            pass
            #gui_window.destroy()  # Close the window
        else:
            messagebox.showerror("Error", "Selection of Grayscale Stego Image CANNOT be Empty!!")
    ## Function to Save to a File
    def saveToFile():
        ## Get GrayScale Stego Image Input
        stego_image = dropdownbox_input.get()
        flag = 0
        if not stego_image.strip():
            messagebox.showerror("Error", "Select grayscale stego image.")
            flag = 1
        ## Open a Text File in Write Mode and Write the Option Selected from the Drop Down Box to the File
        with open("GrayScale Stego Image Selected.txt","w") as img_file:
            img_file.write(f"{stego_image}")
        if  flag == 0  :
            gui_window.destroy()
    ## Create GUI Window
    gui_window = Tk()
    gui_window.protocol("WM_DELETE_WINDOW", close_window)
    gui_window.title('Patient Details(Selection of Stego Image) - GrayScale')
    gui_window.geometry("600x400")

    ## Create the Input Fields
    ## Drop Down Box Creation
    dropdownbox_label = Label(gui_window, text='Grayscale Stego Image :' ,font=("Times New Roman", 15))
    dropdownbox_options = ['grayscale_stego_image.png'] # create a list of options
    dropdownbox_input = Combobox(gui_window, values=dropdownbox_options , font = ("Times New Roman", 15),width = 25) # create a drop-down box with the list of options
    dropdownbox_input.pack()
    dropdownbox_label.place(x=40,y=50)
    dropdownbox_input.place(x=240,y=53)

    ## Button Creation
    embed_button = Button(gui_window, text="EXTRACT", font = ("Times New Roman", 15),command=saveToFile,width = 20,height = 2)
    embed_button.place(x= 180,y=200)

    ## Running The GUI
    gui_window.mainloop()

#selectGrayScaleStegoGUI()