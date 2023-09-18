## Import Required Packages
import cv2
import matplotlib.pyplot as plt

## Global Variables Declaration
global gray_scale,updated

## Initializing the Variables
gray_scale,updated = [],[]

## Load the Grayscale Image
img = cv2.imread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/Lena_256_8bit.png', cv2.IMREAD_GRAYSCALE)

## Get the Image Dimensions
height, width = img.shape
#('Shape of GrayScale Image :',,img.shape)

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
