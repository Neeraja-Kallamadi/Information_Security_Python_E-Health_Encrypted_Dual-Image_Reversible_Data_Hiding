## Import Required Packages
import cv2
import numpy as np

## Function to Add Salt Pepper Noise
def add_salt_pepper_noise(image, amount):
    height, width = image.shape[:2]
    num_pixels = int(amount * height * width)
    # Add Salt Noise (White Pixels)
    salt_coords = [np.random.randint(0, i - 1, num_pixels // 2) for i in image.shape] ## salt_coords --> is a list that will store the randomly generated coordinates for the "salt" noise.
    image[salt_coords[0], salt_coords[1], :] = 255
    # Add Pepper Noise (Black Pixels)
    pepper_coords = [np.random.randint(0, i - 1, num_pixels // 2) for i in image.shape]
    image[pepper_coords[0], pepper_coords[1], :] = 0
    return image

## Load the Image
image = cv2.imread('watermark_256_8bit.jpg')
img = cv2.imread('watermark_256_8bit.jpg')

cv2.imshow('Original Image', image)

## Add Salt and Pepper Noise with amount=0.05
noisy_image = add_salt_pepper_noise(image, 0.2)

## Display the Original and Noisy Images
cv2.imshow('Original Image', img)
cv2.imshow('Noisy Image', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()