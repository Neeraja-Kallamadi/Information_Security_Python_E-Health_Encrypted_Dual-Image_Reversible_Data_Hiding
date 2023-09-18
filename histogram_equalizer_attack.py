## Import Required Packages
import cv2
import numpy as np

## Load the Image in Grayscale
img = cv2.imread('watermark_256_8bit.jpg', cv2.IMREAD_GRAYSCALE)

## Compute the Histogram of the Grayscale Image
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

## Compute the Cumulative Distribution Function (CDF) of the Histogram
cdf = hist.cumsum()
## Normalize the CDF to have values in the Range [0, 255]
cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())

## Replace the Intensity Values of the Pixels in the Original Image with the Normalized CDF Values
img_eq = np.interp(img.flatten(), bins[:-1], cdf_normalized).reshape(img.shape).astype('uint8') ## np.interp() --> function can be useful for filling in missing data or generating smooth curves between known data points.

## Save the Modified Image
cv2.imwrite('image_eq.jpg', img_eq)