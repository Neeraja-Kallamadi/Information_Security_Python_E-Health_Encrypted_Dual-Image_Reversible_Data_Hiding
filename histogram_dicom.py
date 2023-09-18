## Import Required Packages
import matplotlib.pyplot as plt
import pydicom

##Load the DICOM Cover Image and DICOM stego image
dicom_cover_image = pydicom.dcmread('Med4.dcm')
dicom_stego_image = pydicom.dcmread('dicom_stego_image.dcm')
print('Pixels of DICOM Cover Image :',dicom_cover_image.pixel_array)
print()
print()
print('Pixels of DICOM Stego Image :',dicom_stego_image.pixel_array)

## Create a Matplotlib Figure with Two Subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

## Display and Title
ax1.hist(dicom_cover_image.pixel_array.flatten(),bins=1000)
ax1.set_xlim(0,800)   #200
ax1.set_ylim(0,2000)   #500
ax1.set_xlabel('Pixel value')
ax1.set_ylabel('Frequency')
ax1.set_title('Cover Histogram')
ax2.hist(dicom_stego_image.pixel_array.flatten(),bins=30000)
ax2.set_xlim(0,800) #500
ax2.set_ylim(0,2000)  #500
ax2.set_xlabel('Pixel value')
ax2.set_ylabel('Frequency')
ax2.set_title('Stego Histogram')

## Adjust Space between SubPlots
plt.subplots_adjust(wspace=0.4)
## To Describe Elements for a Particular Area of a Graph
ax1.legend(['DICOM Cover Image'])
ax2.legend(['DICOM Stego Image'])

## Show the SubPlots
plt.show()