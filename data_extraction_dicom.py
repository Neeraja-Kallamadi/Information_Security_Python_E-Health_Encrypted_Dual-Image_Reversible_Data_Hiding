## Import Required Packages
import datetime
import math as m
import numpy as np
import pydicom
import cv2
import imageio
import matplotlib.pyplot as plt
import paillier as pa
import data_embedding_dicom as dem_dicom
import bin_char as bc
import gui_stego_image_selection_dicom
import gui_display_secret_message_dicom

print("!!! DATA EXTRACTION AND IMAGE RECOVERY !!!")
print()

## Initialization of Global Variables
global start_time

## Read GrayScale Stego Image
def readDICOMStegoImage():
    ## Initializing Required Variables
    global ext_n,ext_NZ,ext_v1,ext_d,ext_red_NZ,path,new_path,watermarked_dicom_stego_image,dicom_stego_wimg,dicom_stego_img,dicom_stego_image,ext_watermark,ret,thresholded_watermark,flag,ext_bits_allocated,ext_pixel_list,ext_mod_value,M,N
    ext_n,ext_NZ,flag,ext_pixel_list = 5,8,0,[]
    ext_v1 = (2*ext_n)+1
    #print('ext_v1 :',ext_v1)
    ext_d = m.floor((m.log2((ext_v1)*(ext_NZ)-1)))
    #print('ext_d :',ext_d)
    ext_red_NZ = m.ceil((2**(ext_d))/(ext_v1))
    #print('ext_red_NZ :',ext_red_NZ)
    ## Take Stego Image as Input from GUI
    gui_stego_image_selection_dicom.selectDICOMStegoGUI()
    with open ("DICOM Stego Image Selected.txt","r") as fin:
        name = fin.read()
    path = 'G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/'
    new_path = path + name
    ## Load the Watermarked DICOM Stego Image
    watermarked_dicom_stego_image = pydicom.dcmread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/watermarked_dicom_stego_image.dcm')
    ## Load the DICOM Stego Image
    dicom_stego_wimg = pydicom.dcmread(f'{new_path}')
    ## Load the DICOM Stego Image
    dicom_stego_img = pydicom.dcmread(f'{new_path}')
    ## Load the DICOM Stego Image - To Plot the DICOM Stego Image in SubPlot
    dicom_stego_image = pydicom.dcmread(f'{new_path}')
    ## Subtract the dicom_stego_img from watermarked_dicom_stego_image to Extract Watermark using "Alpha Blending Technique"
    ext_watermark = cv2.absdiff(watermarked_dicom_stego_image.pixel_array, dicom_stego_wimg.pixel_array)
    ## Threshold the Resulting Image to get a Binary Image of the Watermark
    ret, thresholded_watermark = cv2.threshold(ext_watermark, 10, 50, cv2.THRESH_BINARY)
    print("Pixels of Extracted Watermark :",thresholded_watermark)
    ## Convert the Extracted Watermark back to a DICOM Object
    dicom_stego_wimg.PixelData = thresholded_watermark.tobytes()
    dicom_stego_wimg.Rows,dicom_stego_wimg.Columns = thresholded_watermark.shape
    ## Save the Extracted Watermark as a DICOM File
    dicom_stego_wimg.save_as('extracted_watermark_dicom.dcm')
    for i,j in zip(dem_dicom.watermark_alpha_resized.flatten(),thresholded_watermark.flatten()):
        if i == j:
            flag = 1
        else :
            flag = 0
    if flag == 1:
        print("Stego Images and Secret Message are Authentic")
    else :
        print("Stego Images and Secret Message are Not Authentic")
    ## Get the Number of Bits Allocated Per Pixel in DICOM Stego Image
    ext_bits_allocated = dicom_stego_image.BitsAllocated
    print("Number of Bits Allocated Per Pixel in DICOM Stego Image :",ext_bits_allocated)
    ## Get all the Pixel Values of a DICOM Stego Image
    for i in dicom_stego_image.pixel_array.flatten(): #pixel_array -> gives all pixel values in 2D array
                                        #flatten() -> converts 2D array to 1D array
        ext_pixel_list.append(int(i))
    print('Total Number of Pixels that exists in DICOM Stego Image :',len(ext_pixel_list))
    #print("All Pixels Values of DICOM Stego Image :",ext_pixel_list)
    ## Mod Value of DICOM Stego Image
    ext_mod_value = 2 ** ext_bits_allocated
    ## Get Shape of DICOM Cover Image
    M,N = dicom_stego_image.pixel_array.shape   #shape -> gives dimensions of the image
    print("Shape of DICOM Cover Image :",M,N)
    print()

## Calculate Start Time of a Program
start_time = datetime.datetime.now().time()

## Function to get Embedded x and y of SI1 and SI2 by Decryption
def getEmbeddedStegoImages():
    ## Initializing Required Variables
    global ext_x_list_p1_loc,ext_y_list_p1_loc,ext_x_list_p2_loc,ext_y_list_p2_loc,enc_ext_p1_x_list,enc_ext_p1_y_list,enc_ext_p2_x_list,enc_ext_p2_y_list,emb_p1_x,emb_p1_x_list,emb_p1_y,emb_p1_y_list,emb_p2_x,emb_p2_x_list,emb_p2_y,emb_p2_y_list,ext_p1,ext_p1_list,ext_p2,ext_p2_list
    ext_x_list_p1_loc,ext_y_list_p1_loc,ext_x_list_p2_loc,ext_y_list_p2_loc,enc_ext_p1_x_list,enc_ext_p1_y_list,enc_ext_p2_x_list,enc_ext_p2_y_list,emb_p1_x_list,emb_p1_y_list,emb_p2_x_list,emb_p2_y_list,ext_p1_list,ext_p2_list = [],[],[],[],[],[],[],[],[],[],[],[],[],[]
    ## Locations of Stego Pixels
    ext_x_list_p1_loc = dem_dicom.x_list_p1_loc
    ext_y_list_p1_loc = dem_dicom.y_list_p1_loc
    ext_x_list_p2_loc = dem_dicom.x_list_p2_loc
    ext_y_list_p2_loc = dem_dicom.y_list_p2_loc
    ## Stego Pixels
    enc_ext_p1_x_list = dem_dicom.rhs1_p1_x_list
    enc_ext_p1_y_list = dem_dicom.rhs1_p1_y_list
    enc_ext_p2_x_list = dem_dicom.rhs1_p2_x_list
    enc_ext_p2_y_list = dem_dicom.rhs1_p2_y_list
    ## Decrypt the Encrypted Embedded x and y of SI1 and SI2
    for i in range(len(enc_ext_p1_x_list)):
        #print('i :',i)
        emb_p1_x = (pa.decrypt(enc_ext_p1_x_list[i],pa.private_key,pa.public_key)) % ext_mod_value
        #print('emb_p1_x (before mod) :',emb_p1_x)
        #print('emb_p1_x (after mod) :',emb_p1_x)
        emb_p1_x = emb_p1_x % ext_mod_value
        emb_p1_x_list.append(emb_p1_x)
    #print()
    for i in range(len(enc_ext_p1_y_list)):
        #print('i :',i)
        emb_p1_y = (pa.decrypt(enc_ext_p1_y_list[i],pa.private_key,pa.public_key)) % ext_mod_value
        #print('emb_p1_y (before mod) :',emb_p1_y)
        emb_p1_y = emb_p1_y % ext_mod_value
        #print('emb_p1_y (after mod) :',emb_p1_y)
        emb_p1_y_list.append(emb_p1_y)
    #print()
    for i in range(len(enc_ext_p2_x_list)):
        #print('i :',i)
        emb_p2_x = (pa.decrypt(enc_ext_p2_x_list[i],pa.private_key,pa.public_key)) % ext_mod_value
        #print('emb_p2_x (before mod) :',emb_p2_x)
        emb_p2_x = emb_p2_x % ext_mod_value
        #print('emb_p2_x (after mod) :',emb_p2_x)
        emb_p2_x_list.append(emb_p2_x)
    #print()
    for i in range(len(enc_ext_p2_y_list)):
        #print('i :',i)
        emb_p2_y = (pa.decrypt(enc_ext_p2_y_list[i],pa.private_key,pa.public_key)) % ext_mod_value
        #print('emb_p2_y (before mod) :',emb_p2_y)
        emb_p2_y = emb_p2_y % ext_mod_value
        #print('emb_p2_y (after mod) :',emb_p2_y)
        emb_p2_y_list.append(emb_p2_y)
    #print()
    for i,j in zip(emb_p1_x_list,emb_p1_y_list):
        ext_p1 = i+j
        ext_p1_list.append(ext_p1)
    for i,j in zip(emb_p2_x_list,emb_p2_y_list):
        ext_p2 = i+j
        ext_p2_list.append(ext_p2)

## Function to Extract Reduced Zone and Reduced Secret Message in Decimal
def extractReducedZoneAndReducedSecret():
    ## Initializing Required Variables
    global diff_p1,diff_p1_list,diff_p2,diff_p2_list,ext_red_z_list,ext_red_w_list
    diff_p1_list,diff_p2_list,ext_red_z_list,ext_red_w_list = [],[],[],[]
    for i,j,k,l in zip(emb_p1_x_list,emb_p1_y_list,emb_p2_x_list,emb_p2_y_list):
        diff_p1 = i - j
        diff_p1_list.append(diff_p1)
        diff_p2 = k - l
        diff_p2_list.append(diff_p2)
    for i in diff_p1_list:
        if i % 2 == 0:
            i = i//2
        else:
            i = (i+1)//2
        ext_red_z_list.append(i)
    for i in diff_p2_list:
        if i % 2 == 0:
            i = i//2
        else:
            i = (i+1)//2
        ext_red_w_list.append(i)

## Function to Extract Secret Message
def extractSecretMessage():
    ## Initializing Required Variables
    global ext_z,ext_z_list,ext_num,ext_num_list,ext_w_list,ext_w_temp,multiples_eight,ext_w
    ext_w,ext_w_temp,ext_z_list,ext_num_list,ext_w_list, = '','',[],[],[]
    for i in ext_red_z_list:
        ext_z = i + m.floor((ext_red_NZ)/2)
        ext_z_list.append(ext_z)
    for i,j in zip(ext_z_list,ext_red_w_list):
        ext_num = (((ext_v1)*(i))+j)+ext_n
        ext_num_list.append(ext_num)
        ext_w_list.append(bin(ext_num).replace("0b", "").zfill(ext_d))
    for i in ext_w_list :
        ext_w_temp += i
    #print('ext_w_temp (modified binary for sake of algorithm) :',ext_w_temp)
    multiples_eight = [i for i in range(len(ext_w_temp) + 1) if i%8 == 0]
    #print('Number of extra leading zeros added :',len(ext_w_temp),max(multiples_eight),(len(ext_w_temp) - max(multiples_eight)))
    if len(ext_w_temp) not in multiples_eight :
        #print(len(ext_w_temp),"is not multiple eight")
        for i in range((len(ext_w_temp) - max(multiples_eight))):
            ext_w = ext_w_temp[(len(ext_w_temp) - max(multiples_eight)):]
    else :
        ext_w = ext_w_temp[(len(ext_w_temp) - max(multiples_eight)):]
    #print('ext_w (actual binary) :',ext_w)

## Function to get Pixels of GrayScale Recovered Images
def getRecoveredImage():
    global ext_p1_x_list,ext_p1_y_list,ext_p2_x_list,ext_p2_y_list,ext_p_list
    ext_p1_x_list,ext_p1_y_list,ext_p2_x_list,ext_p2_y_list,ext_p_list = [],[],[],[],[]
    for i in range(len(emb_p1_x_list)):
        ext_p1_x_list.append((emb_p1_x_list[i] + emb_p1_y_list[i])//2)
        ext_p1_y_list.append(ext_p1_list[i] - ext_p1_x_list[i])
        ext_p2_x_list.append((emb_p2_x_list[i] + emb_p2_y_list[i])//2)
        ext_p2_y_list.append(ext_p2_list[i] - ext_p2_x_list[i])
        ext_p_list.append((ext_p1_list[i] + ext_p2_list[i])//2)
    return (ext_p1_x_list,ext_p1_y_list,ext_p2_x_list,ext_p2_y_list)

## Function Call
readDICOMStegoImage()
getEmbeddedStegoImages()
extractReducedZoneAndReducedSecret()
extractSecretMessage()
getRecoveredImage()

## Print all the Required Values
print("!! Step - 1 !!")
print()
print("!! Locations of x and y of First Stego Image (DICOM) !!")
print("Locations of x and y of SI1 :",ext_x_list_p1_loc,ext_y_list_p1_loc)
print("!! Locations of x and y of Second Stego Image (DICOM) !!")
print("Locations of x and y of SI2 :",ext_x_list_p2_loc,ext_y_list_p2_loc)
print()
print("!! x and y of First Stego Image (DICOM) !!")
print("Stego Pixels of x and y of SI1 :",enc_ext_p1_x_list,enc_ext_p1_y_list)
print("!! x and y of Second Stego Image (DICOM) !!")
print("Stego Pixels of x and y of SI2 :",enc_ext_p2_x_list,enc_ext_p2_y_list)
print()
print("!! Embedded x and Embedded y of First Stego Image (DICOM) !!")
print("Embedded x and y of SI1 :",emb_p1_x_list,emb_p1_y_list)
print("!! Embedded x and Embedded y of Second Stego Image (DICOM) !!")
print("Embedded x and y of SI2 :",emb_p2_x_list,emb_p2_y_list)
print()
print()
print("!! Step - 2 !!")
print()
print("!! Difference of x and y of First Stego Image (DICOM) !!")
print("Difference of x and y of SI1 :",diff_p1_list)
print("!! Difference of x and y of Second Stego Image (DICOM) !!")
print("Difference of x and y of SI2 :",diff_p2_list)
print()
print("!! Extracted Reduced Zone and Reduced Secret Message in Decimal !!")
print("Extracted Reduced Zone Values :",ext_red_z_list)
print("Extracted Reduced Secret Message in Decimal :",ext_red_w_list)
print()
print()
print("!! Step - 3 !!")
print()
print("!! Extracted Zone and Secret Message in Decimal !!")
print("Extracted Zone Values :",ext_z_list)
print("Extracted Secret Message in Decimal :",ext_num_list)
print("!! Extracted Secret Message in Binary !!")
#print("Extracted Secret Message in Binary (Before Removing Leading Zeros) :",ext_w_temp)
print("Extracted Secret Message in Binary :",ext_w)
print()
print("!! x and y of First Recovered Image (DICOM) !!")
print("Pixels of x and y of RI1 :",ext_p1_x_list,ext_p1_y_list)
print("!! x and y of Second Recovered Image (DICOM) !!")
print("Pixels of x and y of RI2 :",ext_p2_x_list,ext_p2_y_list)
print()
print("!! Pixels of First Recovered Image (GrayScale) !!")
print('ext_p1_list :',ext_p1_list)
print("!! Pixels of Second Recovered Image (GrayScale) !!")
print('ext_p2_list :',ext_p2_list)
print("!! Pixels of Recovered Image (GrayScale) !!")
print("ext_p_list :",ext_p_list)
print()
print()

## Function to Plot Stego Image and Recovered Image
def plotStegoAndRecovered():
    ## Initializing Required Variables
    global x,y,new_value,dicom_recovered_image,fig,axes,ax1,ax2,end_time,startdatetime,enddatetime,execution_time
    # Modify pixels
    print("!! Stego and Recovered Pixels of x of RI1 !!")
    for i in range(len(ext_x_list_p1_loc)):
        x=ext_x_list_p1_loc[i]%dicom_stego_img.pixel_array.shape[1]
        y=ext_x_list_p1_loc[i]//dicom_stego_img.pixel_array.shape[1]
        new_value = ext_p1_x_list[i] # Set new value for the pixel at (x,y)
        print("Stego Pixel Value :",dicom_stego_img.pixel_array[y,x],end = ' ')
        dicom_stego_img.pixel_array[y,x] = new_value # Update pixel value in the image
        print("Recovered Pixel Value :",dicom_stego_img.pixel_array[y,x])
    print()
    print("!! Stego and Recovered Pixels of y of RI1 !!")
    for i in range(len(ext_y_list_p1_loc)):
        x=ext_y_list_p1_loc[i]%dicom_stego_img.pixel_array.shape[1]
        y=ext_y_list_p1_loc[i]//dicom_stego_img.pixel_array.shape[1]
        print("Stego Pixel Value :",dicom_stego_img.pixel_array[y,x],end = ' ')
        new_value = ext_p1_y_list[i]  # Set new value for the pixel at (x,y)
        dicom_stego_img.pixel_array[y,x] = new_value  # Update pixel value in the image
        print("Recovered Pixel Value :",dicom_stego_img.pixel_array[y,x])
    print()
    print("!! Stego and Recovered Pixels of x of RI2 !!")
    for i in range(len(ext_x_list_p2_loc)):
        x=ext_x_list_p2_loc[i]%dicom_stego_img.pixel_array.shape[1]
        y=ext_x_list_p2_loc[i]//dicom_stego_img.pixel_array.shape[1]
        print("Stego Pixel Value :",dicom_stego_img.pixel_array[y,x],end = ' ')
        new_value = ext_p2_x_list[i]     # Set new value for the pixel at (x,y)
        dicom_stego_img.pixel_array[y,x] = new_value  # Update pixel value in the image
        print("Recovered Pixel Value :",dicom_stego_img.pixel_array[y,x])
    print()
    print("!! Stego and Recovered Pixels of y of RI2 !!")
    for i in range(len(ext_y_list_p2_loc)):
        x=ext_y_list_p2_loc[i]%dicom_stego_img.pixel_array.shape[1]
        y=ext_y_list_p2_loc[i]//dicom_stego_img.pixel_array.shape[1]
        print("Stego Pixel Value :",dicom_stego_img.pixel_array[y,x],end = ' ')
        new_value = ext_p2_y_list[i]     # Set new value for the pixel at (x,y)
        dicom_stego_img.pixel_array[y,x] = new_value  # Update pixel value in the image
        print("Recovered Pixel Value :",dicom_stego_img.pixel_array[y,x])
    print()
    ## Update the DICOM Object with the Modified Pixel Data
    dicom_stego_img.PixelData = dicom_stego_img.pixel_array.tobytes()
    ## Save the Updated DICOM Object to a New File or Overwrite the Original File
    dicom_stego_img.save_as("dicom_recovered_image.dcm")
    ## Read the DICOM image
    dicom_recovered_image = pydicom.dcmread("dicom_recovered_image.dcm")
    ## Get the pixel data from each DICOM object
    pixel_array1 = dicom_stego_image.pixel_array
    pixel_array2 = dicom_recovered_image.pixel_array
    ## Plot the Stego and Recovered Images Side by Side
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ## Display the Stego Image in Left Sub Plot
    ax1.imshow(pixel_array1, cmap='gray')
    ## Add the Title of Stego Image in Left Sub Plot
    ax1.set_title("DICOM Stego Image")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ## Display the Recovered Image in Right Sub Plot
    ax2.imshow(pixel_array2, cmap='gray')
    ## Add the Title of Recovered Image in Right Sub Plot
    ax2.set_title("DICOM Recovered Image")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ## Calculate End Time of a Program
    end_time = datetime.datetime.now().time()
    ## Calculate Starting Date and Time of Execution of Program
    startdatetime = datetime.datetime.combine(datetime.date.today(), start_time)
    ## Calculate Ending Date and Time of Execution of Program
    enddatetime = datetime.datetime.combine(datetime.date.today(), end_time)
    ## Calculate the Execution Time
    execution_time = enddatetime - startdatetime
    print("The current time before execution of GrayScale Embedding is :", start_time)
    print("The current time after execution of GrayScale Embedding is :", end_time)
    print("Total Execution Time for GrayScale Embedding :",execution_time)
    ## Write Output Binary Data to Text File (Through GUI)
    with open('ext_input.txt', 'w') as file_out:
        file_out.write(ext_w)
    bc.bin_chars()
    ## Get Extracted Secret Message in GUI
    gui_display_secret_message_dicom.displayDICOMSecretMessage()
    ## Show the SubPlots
    plt.show()

## Function to Check Recovered Image and Cover Image
def checkRecoverImageAndCoverImage():
    ## Initializing Required Variables
    global pixel_list_recovered,different_pixels
    pixel_list_recovered,different_pixels = [],[]
    for i in range(dicom_recovered_image.pixel_array.shape[0]):
        for j in range(dicom_recovered_image.pixel_array.shape[1]):
            pixel_list_recovered.append(int(dicom_recovered_image.pixel_array[i,j]))
    for i,j in zip(pixel_list_recovered,dem_dicom.pixel_list):
        if i != j:
            different_pixels.append((i,j))
    #print("Pixels that are different in Recovered Image and Cover Image :",different_pixels)
    if len(different_pixels) == 0:
        print()
        print("Successfully Recovered the Cover Image")
        print()
    else :
        return different_pixels

## Function Call
plotStegoAndRecovered()
checkRecoverImageAndCoverImage()

## Performance Metrics
print("!! PERFORMANCE METRICS !!")
print()

## Function to Calculate MSE (Mean Square Error)
def func_MSE():
    global mse
    mse = (sum((i-j)**2 for i,j in zip(dem_dicom.pixel_list,pixel_list_recovered)))/(M*N)
    print('mse :',mse)
func_MSE()

## Function to Calculate PSNR (Peak Signal to Noise Ratio)
def func_PSNR():
    global psnr
    try :
        psnr = 10*(m.log10((255**2)/mse))
    except:
        print('PSNR is Infinity')
func_PSNR()

## Function to Calculate SSIM (Structural Similarity Index Measure)
def func_SSIM():
    global k1,k2,L,c1,c2,mu_x,mu_y,sigma_x_square,sigma_y_square,sigma_x_y,ssim
    k1,k2,L = 0.01,0.03,((2**8)-1)
    c1 = (k1*L)**2
    c2 = (k2*L)**2
    mu_x = (sum(i for i in dem_dicom.pixel_list)) // (M*N)
    mu_y = (sum(j for j in dem_dicom.pixel_list_stego)) // (M*N)
    sigma_x_square = (sum((i-mu_x)**2 for i in dem_dicom.pixel_list))
    sigma_y_square = (sum((i-mu_y)**2 for i in dem_dicom.pixel_list_stego))
    sigma_x_y = sum((i-mu_x)*(j-mu_y) for i,j in zip(dem_dicom.pixel_list,dem_dicom.pixel_list_stego)) / (M*N)
    ssim = (((2*mu_x*mu_y)+c1) * ((2*sigma_x_y)+c2)) / (((mu_x**2)+(mu_y**2)+c1) * (sigma_x_square+sigma_y_square+c2))
    print('SSIM :',ssim)
func_SSIM()

## Function to Calculate NAE (Normalized Absolute Error)
def func_NAE():
    global nae
    nae =  sum(abs(i-j) for i,j in zip(dem_dicom.pixel_list,dem_dicom.pixel_list_stego)) / (sum(i for i in dem_dicom.pixel_list))
    print('NAE :',nae)
func_NAE()

## Function to Calculate NCC (Normalized Cross Correlation)
def func_NCC():
    global ncc
    ncc = sum((i*j) for i,j in zip(dem_dicom.pixel_list,dem_dicom.pixel_list_stego)) / (m.sqrt((sum(i**2 for i in dem_dicom.pixel_list)) * (sum(j**2 for j in dem_dicom.pixel_list_stego))))
    print('NCC :',ncc)
func_NCC()

## Function to Calculate EMBEDDING RATE (R)
def func_R():
    global R
    print('Pure_Payload :',dem_dicom.num_bits_secret)
    print('2*M*N :',2*M*N)
    R = (dem_dicom.num_bits_secret) / (2*M*N)
    print('R :',R)
func_R()

## Function to Calculate BER (Bit Error Rate)
def func_BER():
    global ber
    ber = (sum(i^j for i,j in zip(dem_dicom.watermark_alpha_resized.flatten(),thresholded_watermark.flatten())) * 100) / (dem_dicom.count3 - dem_dicom.count2)
    print('BER :',ber)
func_BER()
