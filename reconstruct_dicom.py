## Import Required Packages
import pydicom
import matplotlib.pyplot as plt


## Global Variable Declaration
global pixel_list

## Initializing the Variables
pixel_list = []

## Load the DICOM File
dcm = pydicom.dcmread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/Dicom_Sample.dcm')

## Get the Pixel Data as a Numpy Array
print('Pixels of DICOM Image (In Array) :',dcm.pixel_array)
print()
print()

c = 0
## Get the Pixel Data as a List
for i in dcm.pixel_array.flatten():
    pixel_list.append(int(i))
    c += 1
print(c)
print(dcm.pixel_array.shape)
print(dcm.BitsAllocated)
#print('Pixels of DICOM Image (In List):',pixel_list)

# Display the DICOM Image
plt.imshow(dcm.pixel_array, cmap=plt.cm.gray)
plt.show()


## Modifying the First Pixel
dcm.pixel_array[0,0] = 10000

# Display the Modified DICOM Image
plt.imshow(dcm.pixel_array, cmap=plt.cm.gray)
plt.show()

