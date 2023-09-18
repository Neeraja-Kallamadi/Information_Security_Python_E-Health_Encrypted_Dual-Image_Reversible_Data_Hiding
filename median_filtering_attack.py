## Import Required Packages
import cv2
import numpy as np

## Load the Image
img = cv2.imread('watermark_256_8bit.jpg')
image = cv2.imread('watermark_256_8bit.jpg')

## Apply Median Filtering Attack with Kernel Size 5x5
noisy_img = cv2.medianBlur(img, 5)  ## The cv2.medianBlur() function replaces each pixel's value with the median of its neighboring pixels within the specified kernel size. Median filtering is effective in reducing various types of noise, such as salt-and-pepper noise, while preserving edges and details in the image.
                                    ## ksize (here 5) --> This parameter specifies the size of the median filter kernel or the neighborhood over which the median operation is performed. It must be a positive odd integer value. For example, setting ksize to 3 means that a 3x3 kernel will be used for filtering

## Display the Original and Noisy Images
cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image', noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()