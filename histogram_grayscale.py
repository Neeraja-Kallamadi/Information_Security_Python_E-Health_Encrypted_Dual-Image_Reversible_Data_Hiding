## Import Required Packages
import matplotlib.pyplot as plt
import cv2

##Load the GrayScale Cover Image and GrayScale Stego Image
grayscale_cover_image = cv2.imread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/Sailboat_512_8bit.jpg', cv2.IMREAD_GRAYSCALE)
grayscale_stego_image = cv2.imread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/grayscale_stego_image.png', cv2.IMREAD_GRAYSCALE)
print('Pixels of GrayScale Cover Image :',grayscale_cover_image)
print()
print()
print('Pixels of GrayScale Stego Image :',grayscale_stego_image)

## Create a Matplotlib Figure with Two Subplots
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10, 5))

## Display and Title
ax1.hist(grayscale_cover_image.flatten(),bins=256)
ax1.set_xlim(0,255,50)
ax1.set_ylim(0,10000,1000)
ax1.set_xlabel('Pixel value')
ax1.set_ylabel('Frequency')
ax1.set_title('Cover Histogram')
ax2.hist(grayscale_stego_image.flatten(),bins=256)
ax2.set_xlim(0,255,50)
ax2.set_ylim(0,10000,1000)
ax2.set_xlabel('Pixel value')
ax2.set_ylabel('Frequency')
ax2.set_title('Stego Histogram')

## Adjust Space between SubPlots
plt.subplots_adjust(wspace=0.4)
## To Describe Elements for a Particular Area of a Graph
ax1.legend(['GrayScale Cover Image'])
ax2.legend(['GrayScale Stego Image'])

## Show the SubPlots
plt.show()
