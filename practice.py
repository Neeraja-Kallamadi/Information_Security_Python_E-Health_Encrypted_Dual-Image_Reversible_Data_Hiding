'''
import tkinter as tk

# create a tkinter window
root = tk.Tk()

# create a transparent label with the watermark text
watermark_label = tk.Label(root, text="Medical", fg="gray", bg="white", font=("Arial", 20))
watermark_label.config(anchor="center", justify="center")
watermark_label.place(relx=0.5, rely=0.5, anchor="center")

# add other widgets to the GUI
# ...

# start the tkinter main loop
root.mainloop()
'''
'''
import tkinter as tk
from PIL import Image, ImageTk

# create a tkinter window
root = tk.Tk()

# create a transparent label with the watermark text
watermark_text = "Watermark Text"
watermark_image = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
watermark_font = ('Arial', 20)
#watermark_draw = ImageDraw.Draw(watermark_image)
#watermark_draw.text((0, 0), watermark_text, fill='gray', font=watermark_font)
watermark_image = watermark_image.rotate(45, expand=1)


# add other widgets to the GUI
# ...

# start the tkinter main loop
root.mainloop()
'''
'''
import tkinter as tk

# create a tkinter window
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# calculate the desired dimensions based on percentage
window_width = int(0.80 * screen_width)
window_height = int(0.80 * screen_height)
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_position, y_position))

# create a canvas widget with the window size
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# create a transparent label with the watermark text
watermark_text = "Confidential"
watermark_font = ('Arial', 15)
watermark_color = 'gray'
# create a loop that repeats the watermark 3 times diagonally
for i in range(4):
    x_offset = 70 +((i*2)*158)
    y_offset = 35
    watermark_id = canvas.create_text(0, 0, text=watermark_text, fill=watermark_color, font=watermark_font)
    canvas.move(watermark_id, x_offset, y_offset)
    canvas.itemconfig(watermark_id, angle=30)

# add other widgets to the GUI
# ...

# start the tkinter main loop
root.mainloop()
'''
'''
import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the window title
window.title("My GUI")

# Create a label widget
label = tk.Label(window, text="Hello, World!",font=("Times New Roman",14), fg="blue", bg="white")

# get the screen width and height in pixels
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


    # calculate the desired dimensions based on percentage
window_width = int(0.75 * screen_width)
window_height = int(0.75 * screen_height)
# Add the label to the window
label.pack()
window.config(bg="white")
window.geometry(f"{window_width}x{window_height}")
# Create a button widget
button = tk.Button(window, text="Click me!")

# Add a callback function to the button
def button_callback():
    label.config(text="Button clicked!")

button.config(command=button_callback)

# Add the button to the window
button.pack()

# Run the event loop
window.mainloop()
'''
'''
import re

phone_number = input("Enter a phone number: ")
pattern = r'^\+?[0-9]{0,3}[\- ]?\(?\d{1,3}\)?[\- ]?\d{3,4}[\- ]?\d{3,4}$'
match = re.match(pattern, phone_number)
if match is None:
    print("Invalid phone number")
else:
    print("Valid phone number")
'''
'''
import tkinter as tk
import re

class PhoneEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.var = self["textvariable"]
        if self.var is None:
            self.var = self["textvariable"] = tk.StringVar()
        self.var.trace_add("write", self.validate)

    def validate(self, *args):
        phone_number = self.var.get()
        pattern = r'^\+?[0-9]{0,3}[\- ]?\(?\d{1,3}\)?[\- ]?\d{3,4}[\- ]?\d{3,4}$'
        match = re.match(pattern, phone_number)
        if match is None:
            self.config(fg="red")
        else:
            self.config(fg="black")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.phone_entry = PhoneEntry(self)
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.pack()
        self.phone_entry.pack()
        self.quit_button.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
'''
'''
import tkinter as tk

def toggle_state():
    if label.cget('text') == 'OFF':
        label.config(text='ON')
    else:
        label.config(text='OFF')

root = tk.Tk()

label = tk.Label(root, text='OFF')
label.pack()

button = tk.Button(root, text='Toggle', command=toggle_state)
button.pack()

root.mainloop()
'''
'''
import tkinter as tk

# Create a window
window = tk.Tk()

# Create a group of radio buttons
radio_var = tk.StringVar()
radio_var.set("Option 1")
radio_button1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value="Option 1")
radio_button2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value="Option 2")
radio_button3 = tk.Radiobutton(window, text="Option 3", variable=radio_var, value="Option 3")
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()
# Function to save the selected value to a file
def save_to_file():
    selected_value = radio_var.get()
    with open("selected_value.txt", "w") as file:
        file.write(selected_value)

# Function to clear the radio button
def clear_radio_button():
    radio_var.set(None)

# Create a button to clear the radio button
clear_button = tk.Button(window, text="Clear", command=clear_radio_button)
clear_button.pack()

# Start the GUI
window.mainloop()
'''
'''
import re

validate_phone_number_pattern = "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
print(re.match(validate_phone_number_pattern, "+1 (615) 243-5172")) # Returns Match object
'''
'''
import re # Importing re module
n=input('Enter Mobile number :')  # Reading input from the user
r=re.fullmatch('[6-9][0-9]{9}',n) # calling fullmatch function by passing pattern and n
'''

'''
if r!=None: # checking whether it is none or not
     print('Valid Number')
else:
     print('Not a valid number')
'''

'''
import tkinter as tk
from tkinter import messagebox

def check_input():
    input_text = entry.get() # Get the user input from the text box
    if not input_text.isdigit(): # Check if the input is not a digit
        messagebox.showerror("Error", "Please enter a valid number!")
    else:
        messagebox.showinfo("Success", "You entered: " + input_text)

# Create a GUI window
root = tk.Tk()
root.title("My GUI")

# Create a label and a text box for user input
label = tk.Label(root, text="Enter a number:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to check the input
button = tk.Button(root, text="Check Input", command=check_input)
button.pack()

# Start the GUI main loop
root.mainloop()
'''

'''
import tkinter as tk

def validate_input():
    input_text = entry.get() # Get the user input from the text box
    if not input_text.isdigit(): # Check if the input is not a digit
        entry.config(validate="key", validatecommand=(validate_input_cmd, '%P'))
        entry.delete(0, tk.END)
        entry.insert(0, "*")
    else:
        entry.config(validate="key", validatecommand=(validate_input_cmd, '%P*'))

# Create a GUI window
root = tk.Tk()
root.title("My GUI")

# Create a label and a text box for user input
label = tk.Label(root, text="Enter a number:")
label.pack()
entry = tk.Entry(root, show='*')
entry.pack()

# Bind validation to the text box
validate_input_cmd = root.register(validate_input)
entry.config(validate="key", validatecommand=(validate_input_cmd, '%P*'))

# Start the GUI main loop
root.mainloop()
'''

'''
import cv2
pixel_list_cover,pixel_list_watermark = [],[]
cover_img = cv2.imread("G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code/lena_512_8bit.jpg", cv2.IMREAD_GRAYSCALE)

watermark_img = cv2.imread("G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code/watermark_256_8bit.jpg", cv2.IMREAD_GRAYSCALE)
print(cover_img.shape)
print(watermark_img.shape)
for i in range(cover_img.shape[0]):
    for j in range(cover_img.shape[1]):
        pixel_list_cover.append(int(cover_img[i,j]))
for i in range(watermark_img.shape[0]):
    for j in range(watermark_img.shape[1]):
        pixel_list_watermark.append(int(watermark_img[i,j]))

print(pixel_list_cover)
print(pixel_list_watermark)
print(len(pixel_list_cover))
print(len(pixel_list_watermark))
'''


'''
import pydicom
# Load the DICOM file
ds = pydicom.dcmread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code/m.dcm')
#ds_512 = pydicom.dcmread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code/g_512_16bit.dcm')

# Get the pixel data
pixel_data = ds.pixel_array.flatten()
print(pixel_data)
#pixel_data_512 = ds_512.pixel_array.flatten()
#print('512 dicom :',pixel_data_512)

#for i in pixel_data:
    #print(i)
print(min(pixel_data))
print(max(pixel_data))
print(len(pixel_data))
#print('512 dicom :',len(pixel_data_512))

# Get the image size
rows = int(ds.Rows)
cols = int(ds.Columns)
print(rows)
print(cols)
#rows_512 = int(ds_512.Rows)
#cols_512 = int(ds_512.Columns)
#print('512 dicom :',rows_512)
#print('512 dicom :',cols_512)


# Get the number of bits allocated per pixel
bits_allocated = int(ds.BitsAllocated)
print(bits_allocated)
#bits_allocated_512 = int(ds_512.BitsAllocated)
#print('512 dicom :',bits_allocated_512)
'''

## Watermark Embedding in GraySCale Image (Alpha Blending)
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
print(cv2.__version__)

# Load the 512x512 Stego Image
large_img = cv2.imread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/Lena_512_8bit.jpg', cv2.IMREAD_GRAYSCALE)

# Load the 256x256 grayscale image as the watermark
watermark = cv2.imread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/watermark_256_8bit.jpg', cv2.IMREAD_GRAYSCALE)
print('watermark :',watermark)
# Convert the watermark to a transparent image by setting the alpha channel to a value between 0 and 1
watermark_alpha = np.zeros((256, 256), dtype=np.uint8)
print('watermark_alpha - 0 :',watermark_alpha)

watermark_alpha[:, :] = watermark
print('watermark_alpha - 1:',watermark_alpha)

watermark_alpha[:, :] = 50  # Set the alpha channel to a value of 50 (between 0 and 255)
print('watermark_alpha - 2:',watermark_alpha)

# Resize the transparent watermark to match the size of the large image
watermark_alpha_resized = cv2.resize(watermark_alpha, (512, 512))
print(watermark_alpha_resized.shape)
print(watermark_alpha_resized)
print(large_img.shape)
print(large_img)

# Blend the transparent watermark with the large image using alpha blending
watermarked_img = cv2.addWeighted(large_img, 1, watermark_alpha_resized, 0.5, 0)
print('watermarked image')
print(watermarked_img)

# Save the watermarked image
cv2.imwrite('watermarked_alpha_resized.png', watermark_alpha_resized)
print('watermark_alpha_resized :',watermark_alpha_resized)

count1 = 0
pixel_list_ci,pixel_list_wi = [],[]
for i in range(large_img.shape[0]):
    for j in range(large_img.shape[1]):
        pixel_list_ci.append(int(large_img[i,j]))
#print('pixel_list_ci:',pixel_list_ci)
for i in range(watermarked_img.shape[0]):
    for j in range(watermarked_img.shape[1]):
        pixel_list_wi.append(int(watermarked_img[i,j]))
#print('pixel_list_wi :',pixel_list_wi)
for i,j in zip(pixel_list_ci,pixel_list_wi):
    if i == j:
        print(i,j)
        count1 += 1
print(count1)
'''

## Watermark Extraction in GraySCale Image (Watermark Detection)
'''
print('!! Watermark Extraction !!')
# Load the original 512x512 grayscale image
#large_img = cv2.imread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/Lena_512_8bit.jpg', cv2.IMREAD_GRAYSCALE)

# Load the watermarked image
#watermarked_img = cv2.imread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/watermarked_image.png', cv2.IMREAD_GRAYSCALE)

# Subtract the original image from the watermarked image to extract the watermark
watermark = cv2.absdiff(watermarked_img, large_img)
print(watermark)

# Threshold the resulting image to get a binary image of the watermark
ret, thresholded_watermark = cv2.threshold(watermark, 10, 50, cv2.THRESH_BINARY)
print(ret)
print(thresholded_watermark)


# Save the extracted watermark
cv2.imwrite('extracted_watermark.png', thresholded_watermark)
'''

## Watermark Embedding in DICOM Image (Alpha Blending)
'''
import cv2
import pydicom
import numpy as np

# Load the 512x512 DICOM image
dcm = pydicom.dcmread('Med4.dcm')
print('dcm.pixel_array :',dcm.pixel_array)

# Convert the DICOM image to a numpy array
large_img = dcm.pixel_array
print('large_img :',large_img)

# Load the 256x256 grayscale image as the watermark
watermark = cv2.imread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/watermark_256_8bit.jpg', cv2.IMREAD_GRAYSCALE)
print('watermark :',watermark)
# Convert the watermark to a transparent image by setting the alpha channel to a value between 0 and 1
watermark_alpha = np.zeros((256, 256), dtype=np.uint8)
watermark_alpha[:, :] = watermark
watermark_alpha[:, :] = 50  # Set the alpha channel to a value of 50 (between 0 and 255)

# Resize the transparent watermark to match the size of the large image
watermark_alpha_resized = cv2.resize(watermark_alpha, (512, 512))
print('watermark_alpha_resized :',watermark_alpha_resized)

# Blend the transparent watermark with the large image using alpha blending
watermarked_img = cv2.addWeighted(large_img, 1, watermark_alpha_resized, 0.5, 0,dtype=cv2.CV_16U)
print('watermarked_img :',watermarked_img)

# Convert the watermarked image back to a DICOM object
dcm.PixelData = watermarked_img.tobytes()
dcm.Rows, dcm.Columns = watermarked_img.shape

# Save the watermarked DICOM image
dcm.save_as('watermarked_image.dcm')
print('dcm :',dcm.pixel_array)
'''

## Watermark Extraction in DICOM Image (Watermark Detection)
'''
import cv2
import pydicom
import numpy as np

# Load the original 512x512 DICOM image
dcm = pydicom.dcmread('Med4.dcm')
print('dcm :',dcm.pixel_array)

# Convert the DICOM image to a numpy array
large_img = dcm.pixel_array

# Load the watermarked DICOM image
watermarked_dcm = pydicom.dcmread('watermarked_image.dcm')

# Convert the watermarked DICOM image to a numpy array
watermarked_img = watermarked_dcm.pixel_array

# Subtract the original image from the watermarked image to extract the watermark
watermark = cv2.absdiff(watermarked_img, large_img)

# Threshold the resulting image to get a binary image of the watermark
ret, thresholded_watermark = cv2.threshold(watermark, 10, 50, cv2.THRESH_BINARY)
print('thresholded_watermark :',thresholded_watermark)

# Convert the extracted watermark back to a DICOM object
dcm.PixelData = thresholded_watermark.tobytes()
dcm.Rows, dcm.Columns = thresholded_watermark.shape
print('dcm.pixel_array.flatten() :',dcm.pixel_array)
print(len(dcm.pixel_array.flatten()))

# Save the extracted watermark as a DICOM file
dcm.save_as('extracted_watermark.dcm')
'''

'''
import numpy as np
import matplotlib.pyplot as plt

# Sample data with some y values set to infinity
x1 = [1, 2, 3, 4]
y1 = [1, 4, 9, np.inf]  # One y value set to infinity
x2 = [1, 2, 3, 4]
y2 = [1, 2, 3, 4]
x3 = [1, 2, 3, 4]
y3 = [4, 3, np.inf, 1]  # Two y values set to infinity

# Create a custom y array with values from 30 to 100 and infinity
custom_y = np.concatenate([np.arange(30, 101), [np.inf]])

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot each curve separately, with clip_on=False to display infinity points
ax.scatter(x1, y1, label='Curve 1', clip_on=False)
ax.scatter(x2, y2, label='Curve 2', clip_on=False)
ax.scatter(x3, y3, label='Curve 3', clip_on=False)

# Set axis labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Multiple Curves Scatter Plot')

# Set y-axis limits
ax.set_ylim([30, None])

# Set y-ticks to custom_y array
ax.set_yticks(custom_y)

# Set y-tick labels to show only 30, 40, ..., 90, 100, and infinity
y_tick_labels = ['30'] + [''] * 7 + ['90', '100', '∞']
ax.set_yticklabels(y_tick_labels)

# Add legend
ax.legend()

# Show the plot
plt.show()
'''

'''
import matplotlib.pyplot as plt
import numpy as np

# Define x-axis values
x = np.linspace(0, 3, 100)

# Define y-axis values
y = np.concatenate((np.linspace(30, 100, 100), np.array([np.inf])))

# Create scatter plot
plt.scatter(x, y)

# Set x-axis and y-axis limits
plt.xlim(0, 3)
plt.ylim(30, np.inf)

# Set x-axis and y-axis labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show plot
plt.show()
'''

'''
## Import Required Packages
import cv2
import matplotlib.pyplot as plt

## Global Variables Declaration
global gray_scale,updated

## Initializing the Variables
gray_scale,updated = [],[]

## Load the Grayscale Image
img = cv2.imread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/watermark_256_8bit.jpg', cv2.IMREAD_GRAYSCALE)

## Get the Image Dimensions
height, width = img.shape
print('Shape of GrayScale Image :',height,width)
print()
print('Pixels of Cover Image in 2D Array :',img)
print()
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
print('First 256 Pixels of Cover Image :',img[0])
print()
s_box = [16, 32, 2, 64, 8, 128, 4, 99, 90, 232, 142, 167, 53, 81, 56, 162,70, 43, 210, 108, 233, 158, 135, 55, 17, 48, 34, 66, 72, 136, 132, 103,57, 178, 102, 41, 146, 100, 105, 154, 228, 109, 249, 190, 133, 119, 25, 176,38, 33, 18, 96, 10, 192, 12, 227, 94, 139, 212, 79, 187, 246, 13, 243,126, 137, 148, 71, 59, 242, 110, 169, 150, 7, 51, 114, 106, 202, 204, 239,189, 213, 95, 155, 244, 77, 251, 254, 141, 0, 29, 211, 124, 201, 156, 199,63, 145, 52, 65, 24, 160, 6, 35, 82, 104, 138, 196, 111, 185, 182, 5,115, 122, 234, 206, 175, 181, 85, 91, 248, 174, 165, 117, 89, 184, 166, 37,113, 58, 226, 78, 171, 214, 15, 179, 118, 9, 144, 36, 97, 26, 224, 14,163, 86, 11, 208, 44, 225, 30, 131, 84, 75, 216, 172, 229, 125, 217, 188,197, 127, 153, 180, 69, 123, 250, 238, 173, 245, 93, 219, 252, 205, 255, 157,215, 31, 147, 116, 73, 152, 164, 101, 121, 186, 230, 45, 241, 62, 129, 20,67, 88, 168, 134, 39, 49, 50, 98, 74, 200, 140, 231, 61, 209, 60, 193,28, 195, 92, 203, 220, 207, 191, 149, 87, 27, 240, 46, 161, 22, 3, 80,40, 130, 68, 107, 218, 236, 237, 253, 221, 223, 157, 151,23,19,112,42,194,76,235,222,143,183,21,83,120,170,198,47,247,177,54,1]
print('Length of s_box :',len(s_box))
print(min(s_box))
print(max(s_box))
print()
for i in range(height):
    for j in range(width):
        img[i,j] = img[i,s_box[j]]
print('Pixels of Updated Image :',img)
print()
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
'''

'''
## Loop through Each Pixel in the GrayScale Image
for y in range(height):
    for x in range(width):
        # Get the pixel value (intensity) at the current x,y location
        pixel = img[y,x]
        gray_scale.append(pixel)
print()
print('Pixels of GrayScale Image :',gray_scale)
print()
print()
plt.imshow(img, cmap=plt.cm.gray)
plt.show()


## Modifying the First Pixel
img[0,0] = 254
## Loop through Each Pixel in the Modified GrayScale Image
for y in range(height):
    for x in range(width):
        # Get the pixel value (intensity) at the current x,y location
        pixel = img[y,x]
        updated.append(pixel)
print('Pixels of Modified GrayScale Image :',updated)
plt.imshow(img, cmap=plt.cm.gray)
plt.show()

'''
