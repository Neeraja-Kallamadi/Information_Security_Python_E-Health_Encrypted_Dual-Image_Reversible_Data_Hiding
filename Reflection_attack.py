## Import Required Packages
import cv2
import numpy as np

## Load the Image
img = cv2.imread('watermark_256_8bit.jpg', cv2.IMREAD_GRAYSCALE)

## Create a New Image by Horizontally Flipping the Original Image using the cv2.flip() Function:
img_flipped = cv2.flip(img, 0)

## Generate Random Noise using the cv2.randn() Function:
noise = np.zeros_like(img_flipped)
cv2.randn(noise, 0, 800)

## In this example, we're generating Gaussian noise with a Mean of 0 and Standard Deviation of 20. Add the Noise to the Flipped Image using NumPy:
img_flipped_noisy = img_flipped + noise

## Clip the Pixel Values to ensure they're within the Range [0, 255]:
img_flipped_noisy = np.clip(img_flipped_noisy, 0, 255).astype(np.uint8)

## Save the Modified, Flipped Image to Disk:
cv2.imwrite('flipped_noisy.jpg', img_flipped_noisy)

