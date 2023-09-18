## Import Required Packages
import cv2
import numpy as np

## Load the Image
img = cv2.imread('watermark_256_8bit.jpg')

## Generate Random Gaussian Noise with Mean 0 and Standard Deviation 50
noise = np.random.normal(0, 50, img.shape)

## In this updated version of the code, we first generate the noise array as before. However, we then use the astype() method to convert the data type of the noise array to int16. This is because OpenCV's add() function expects arrays of the same data type, and we will add noise to the uint8 img array later.
## After generating the noise as int16, we clip the pixel values of noise to be in the range [0, 255] using np.clip(), and convert it to uint8 using the astype() method again.
## Finally, we add the noise array to the img array using cv2.add(), and display the original and noisy images.
noise = np.clip(noise, 0, 255).astype(np.uint8)
print(img.dtype)
print(noise.dtype)
cv2.imshow('Original Image', img)

## Add the Noise to the Image
noisy_img = cv2.add(img, noise)

## Display the original and noisy images
cv2.imshow('Noisy Image', noisy_img)
cv2.waitKey(0) ## waitKey(0) --> is used at the end of a program to keep the displayed window open until the user closes it by pressing a key. It allows the user to view the image or video frame and interact with the program as needed.
cv2.destroyAllWindows()