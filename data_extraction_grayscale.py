## Import Required Packages
import datetime
import math as m
import numpy as np
import cv2
import imageio
import matplotlib.pyplot as plt
import paillier as pa
import data_embedding_grayscale as dem_grayscale
import bin_char as bc
import gui_stego_image_selection_grayscale
import gui_display_secret_message_grayscale

print("!!! DATA EXTRACTION AND IMAGE RECOVERY !!!")
print()

## Initialization of Global Variables
global start_time

## Read GrayScale Stego Image
def readGrayScaleStegoImage():
    ## Initializing Required Variables
    global ext_n,ext_NZ,ext_v1,ext_d,ext_red_NZ,path,new_path,watermarked_grayscale_stego_image,grayscale_stego_img,grayscale_stego_image,ext_watermark,ret,thresholded_watermark,flag,ext_bits_allocated,M,N,ext_pixel_list,ext_mod_value
    ext_n,ext_NZ,flag,ext_pixel_list = 5,8,0,[]
    ext_v1 = (2*ext_n)+1
    #print('ext_v1 :',ext_v1)
    ext_d = m.floor((m.log2((ext_v1)*(ext_NZ)-1)))
    #print('ext_d :',ext_d)
    ext_red_NZ = m.ceil((2**(ext_d))/(ext_v1))
    #print('ext_red_NZ :',ext_red_NZ)
    ## Take GrayScale Stego Image as Input from GUI
    gui_stego_image_selection_grayscale.selectGrayScaleStegoGUI()
    with open ("GrayScale Stego Image Selected.txt","r") as fin:
        name = fin.read()
    path = 'G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/'
    new_path = path + name
    ## Load the Watermarked GrayScale Stego Image
    watermarked_grayscale_stego_image = cv2.imread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/watermarked_grayscale_stego_image.png', cv2.IMREAD_GRAYSCALE)
    #print('Pixels of Watermarked Grayscale Stego Image :',watermarked_grayscale_stego_image)
    ## Load the GrayScale Stego Image
    grayscale_stego_img = cv2.imread(f"{new_path}", cv2.IMREAD_GRAYSCALE)
    ## Load the GrayScale Stego Image - To Plot the GrayScale Stego Image in SubPlot
    grayscale_stego_image = cv2.imread(f"{new_path}", cv2.IMREAD_GRAYSCALE)
    ## Get the Number of Bits Allocated Per Pixel in GrayScale Stego Image
    ## Subtract the GrayScale Stego Image from the Watermarked GrayScale Stego Image to Extract the Watermark (Using "Watermark Detection Technique")
    ext_watermark = cv2.absdiff(watermarked_grayscale_stego_image, grayscale_stego_image)
    ## Threshold the Resulting Image to get a Binary Image of the Watermark
    ret, thresholded_watermark = cv2.threshold(ext_watermark, 10, 50, cv2.THRESH_BINARY)
    print("Pixels of Extracted Watermark :",thresholded_watermark)
    print()
    ## Save the Extracted Watermark
    cv2.imwrite('extracted_watermark_grayscale.png', thresholded_watermark)
    for i,j in zip(dem_grayscale.watermark_alpha_resized_grayscale.flatten(),thresholded_watermark.flatten()):
        if i == j:
            flag = 1
        else :
            flag = 0
    if flag == 1:
        print("Stego Images and Secret Message are Authentic")
    else :
        print("Stego Images and Secret Message are Not Authentic")
    ext_bits_allocated = np.iinfo(grayscale_stego_img.dtype).bits
    print("Number of Bits Allocated Per Pixel in GrayScale Stego Image :",ext_bits_allocated)
    ## Get Shape of the GrayScale Stego Image
    M,N = grayscale_stego_image.shape
    print("Shape of Stego Image :",M,N)
    ## Get all the Pixel Values of a GrayScale Stego Image
    for i in range(M):
        for j in range(N):
            ext_pixel_list.append(int(grayscale_stego_image[i,j]))
    print('Total Number of Pixels that exists in GrayScale Stego Image :',len(ext_pixel_list))
    print()
    #print("All Pixels Values of GrayScale Stego Image :",ext_pixel_list)
    ## Mod Value of GrayScale Stego Image
    ext_mod_value = 2**ext_bits_allocated

## Calculate Start Time of a Program
start_time = datetime.datetime.now().time()

## Function to get Embedded x and y of SI1 and SI2 by Decryption
def getEmbeddedStegoImages():
    ## Initializing Required Variables
    global ext_x_list_p1_loc,ext_y_list_p1_loc,ext_x_list_p2_loc,ext_y_list_p2_loc,enc_ext_p1_x_list,enc_ext_p1_y_list,enc_ext_p2_x_list,enc_ext_p2_y_list,emb_p1_x,emb_p1_x_list,emb_p1_y,emb_p1_y_list,emb_p2_x,emb_p2_x_list,emb_p2_y,emb_p2_y_list,ext_p1,ext_p1_list,ext_p2,ext_p2_list
    ext_x_list_p1_loc,ext_y_list_p1_loc,ext_x_list_p2_loc,ext_y_list_p2_loc,enc_ext_p1_x_list,enc_ext_p1_y_list,enc_ext_p2_x_list,enc_ext_p2_y_list,emb_p1_x_list,emb_p1_y_list,emb_p2_x_list,emb_p2_y_list,ext_p1_list,ext_p2_list = [],[],[],[],[],[],[],[],[],[],[],[],[],[]
    ## Locations of Stego Pixels
    ext_x_list_p1_loc = dem_grayscale.x_list_p1_loc
    ext_y_list_p1_loc = dem_grayscale.y_list_p1_loc
    ext_x_list_p2_loc = dem_grayscale.x_list_p2_loc
    ext_y_list_p2_loc = dem_grayscale.y_list_p2_loc
    ## Stego Pixels
    enc_ext_p1_x_list = dem_grayscale.rhs1_p1_x_list
    enc_ext_p1_y_list = dem_grayscale.rhs1_p1_y_list
    enc_ext_p2_x_list = dem_grayscale.rhs1_p2_x_list
    enc_ext_p2_y_list = dem_grayscale.rhs1_p2_y_list
    ## Decrypt the Encrypted Embedded x and y of SI1 and SI2
    for i in range(len(enc_ext_p1_x_list)):
        #print('i :',i)
        emb_p1_x = (pa.decrypt(enc_ext_p1_x_list[i],pa.private_key,pa.public_key))
        #print('emb_p1_x (before mod) :',emb_p1_x)
        emb_p1_x = emb_p1_x % ext_mod_value
        #print('emb_p1_x (after mod) :',emb_p1_x)
        emb_p1_x_list.append(emb_p1_x)
    #print()
    for i in range(len(enc_ext_p1_y_list)):
        #print('i :',i)
        emb_p1_y = (pa.decrypt(enc_ext_p1_y_list[i],pa.private_key,pa.public_key))
        #print('emb_p1_y (before mod) :',emb_p1_y)
        emb_p1_y = emb_p1_y % ext_mod_value
        #print('emb_p1_y (after mod) :',emb_p1_y)
        emb_p1_y_list.append(emb_p1_y)
    #print()
    for i in range(len(enc_ext_p2_x_list)):
        #print('i :',i)
        emb_p2_x = (pa.decrypt(enc_ext_p2_x_list[i],pa.private_key,pa.public_key))
        #print('emb_p2_x (before mod) :',emb_p2_x)
        emb_p2_x = emb_p2_x % ext_mod_value
        #print('emb_p2_x (after mod) :',emb_p2_x)
        emb_p2_x_list.append(emb_p2_x)
    #print()
    for i in range(len(enc_ext_p2_y_list)):
        #print('i :',i)
        emb_p2_y = (pa.decrypt(enc_ext_p2_y_list[i],pa.private_key,pa.public_key))
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
readGrayScaleStegoImage()
getEmbeddedStegoImages()
extractReducedZoneAndReducedSecret()
extractSecretMessage()
getRecoveredImage()

## Print all the Required Values
print("!! Step - 1 !!")
print()
print("!! Locations of x and y of First Stego Image (GrayScale) !!")
print("Locations of x and y of SI1 :",ext_x_list_p1_loc,ext_y_list_p1_loc)
print("!! Locations of x and y of Second Stego Image (GrayScale) !!")
print("Locations of x and y of SI2 :",ext_x_list_p2_loc,ext_y_list_p2_loc)
print()
print("!! x and y of First Stego Image (GrayScale) !!")
print("Stego Pixels of x and y of SI1 :",enc_ext_p1_x_list,enc_ext_p1_y_list)
print("!! x and y of Second Stego Image (GrayScale) !!")
print("Stego Pixels of x and y of SI2 :",enc_ext_p2_x_list,enc_ext_p2_y_list)
print()
print("!! Embedded x and Embedded y of First Stego Image (GrayScale) !!")
print("Embedded x and y of SI1 :",emb_p1_x_list,emb_p1_y_list)
print("!! Embedded x and Embedded y of Second Stego Image (GrayScale) !!")
print("Embedded x and y of SI2 :",emb_p2_x_list,emb_p2_y_list)
print()
print()
print("!! Step - 2 !!")
print()
print("!! Difference of x and y of First Stego Image (GrayScale) !!")
print("Difference of x and y of SI1 :",diff_p1_list)
print("!! Difference of x and y of Second Stego Image (GrayScale) !!")
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
print("!! x and y of First Recovered Image (GrayScale) !!")
print("Pixels of x and y of RI1 :",ext_p1_x_list,ext_p1_y_list)
print("!! x and y of Second Recovered Image (GrayScale) !!")
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
    global x,y,new_value,grayscale_recovered_image,fig,axes,ax1,ax2,end_time,startdatetime,enddatetime,execution_time
    # Modify pixels
    print("!! Stego and Recovered Pixels of x of RI1 !!")
    for i in range(len(ext_x_list_p1_loc)):
        x=ext_x_list_p1_loc[i]%grayscale_stego_img.shape[1]
        y=ext_x_list_p1_loc[i]//grayscale_stego_img.shape[1]
        new_value = ext_p1_x_list[i] # Set new value for the pixel at (x,y)
        print("Stego Pixel Value :",grayscale_stego_img[y,x],end = ' ')
        grayscale_stego_img[y,x] = new_value # Update pixel value in the image
        print("Recovered Pixel Value :",grayscale_stego_img[y,x])
    print()
    print("!! Stego and Recovered Pixels of y of RI1 !!")
    for i in range(len(ext_y_list_p1_loc)):
        x=ext_y_list_p1_loc[i]%grayscale_stego_img.shape[1]
        y=ext_y_list_p1_loc[i]//grayscale_stego_img.shape[1]
        new_value = ext_p1_y_list[i]  # Set new value for the pixel at (x,y)
        print("Stego Pixel Value :",grayscale_stego_img[y,x],end = ' ')
        grayscale_stego_img[y,x] = new_value  # Update pixel value in the image
        print("Recovered Pixel Value :",grayscale_stego_img[y,x])
    print()
    print("!! Stego and Recovered Pixels of x of RI2 !!")
    for i in range(len(ext_x_list_p2_loc)):
        x=ext_x_list_p2_loc[i]%grayscale_stego_img.shape[1]
        y=ext_x_list_p2_loc[i]//grayscale_stego_img.shape[1]
        new_value = ext_p2_x_list[i]     # Set new value for the pixel at (x,y)
        print("Stego Pixel Value :",grayscale_stego_img[y,x],end = ' ')
        grayscale_stego_img[y,x] = new_value  # Update pixel value in the image
        print("Recovered Pixel Value :",grayscale_stego_img[y,x])
    print()
    print("!! Stego and Recovered Pixels of y of RI2 !!")
    for i in range(len(ext_y_list_p2_loc)):
        x=ext_y_list_p2_loc[i]%grayscale_stego_img.shape[1]
        y=ext_y_list_p2_loc[i]//grayscale_stego_img.shape[1]
        new_value = ext_p2_y_list[i]     # Set new value for the pixel at (x,y)
        print("Stego Pixel Value :",grayscale_stego_img[y,x],end = ' ')
        grayscale_stego_img[y,x] = new_value  # Update pixel value in the image
        print("Recovered Pixel Value :",grayscale_stego_img[y,x])
    print()
    ## Save the Recovered Iimage to a File
    imageio.imwrite('grayscale_recovered_image.png', grayscale_stego_img)
    grayscale_recovered_image= cv2.imread("G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/grayscale_recovered_image.png", cv2.IMREAD_GRAYSCALE)
    ## Plot the Stego and Recovered Images Side by Side
    fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
    ax1, ax2 = axes.ravel()
    ## Display the Stego Image in Left Sub Plot
    ax1.imshow(grayscale_stego_image, cmap='gray')
    ## Add the Title of Stego Image in Left Sub Plot
    ax1.set_title('GrayScale Stego image')
    ## Display the Recovered Image in Right Sub Plot
    ax2.imshow(grayscale_recovered_image, cmap='gray')
    ## Add the Title of Recovered Image in Right Sub Plot
    ax2.set_title('GrayScale Recovered image')
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
    gui_display_secret_message_grayscale.displayGrayScaleSecretMessage()
    ## Show the SubPlots
    plt.show()

## Function to Check Recovered Image and Cover Image
def checkRecoveredAndCover():
    ## Initializing Required Variables
    global pixel_list_recovered,different_pixels
    pixel_list_recovered,different_pixels = [],[]
    for i in range(grayscale_recovered_image.shape[0]):
        for j in range(grayscale_recovered_image.shape[1]):
            pixel_list_recovered.append(int(grayscale_recovered_image[i,j]))
    for i,j in zip(pixel_list_recovered,dem_grayscale.pixel_list):
        if i != j:
            different_pixels.append((i,j))
    if len(different_pixels) == 0:
        print()
        print("Successfully Recovered the Cover Image")
        print()
    else :
        print()
        print("Pixels that are different in Recovered Image and Cover Image :",different_pixels)
        print()

## Function Call
plotStegoAndRecovered()
checkRecoveredAndCover()

## Performance Metrics
print("!! PERFORMANCE METRICS !!")
print()

## Function to Calculate MSE (Mean Square Error)
def func_MSE():
    global mse
    mse = (sum((i-j)**2 for i,j in zip(dem_grayscale.pixel_list,pixel_list_recovered)))/(M*N)
    print('MSE :',mse)
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
    mu_x = (sum(i for i in dem_grayscale.pixel_list)) // (M*N)
    mu_y = (sum(j for j in dem_grayscale.pixel_list_stego)) // (M*N)
    sigma_x_square = (sum((i-mu_x)**2 for i in dem_grayscale.pixel_list))
    sigma_y_square = (sum((i-mu_y)**2 for i in dem_grayscale.pixel_list_stego))
    sigma_x_y = sum((i-mu_x)*(j-mu_y) for i,j in zip(dem_grayscale.pixel_list,dem_grayscale.pixel_list_stego)) / (M*N)
    ssim = (((2*mu_x*mu_y)+c1) * ((2*sigma_x_y)+c2)) / (((mu_x**2)+(mu_y**2)+c1) * (sigma_x_square+sigma_y_square+c2))
    print('SSIM :',ssim)
func_SSIM()

## Function to Calculate NAE (Normalized Absolute Error)
def func_NAE():
    global nae
    nae =  sum(abs(i-j) for i,j in zip(dem_grayscale.pixel_list,dem_grayscale.pixel_list_stego)) / (sum(i for i in dem_grayscale.pixel_list))
    print('NAE :',nae)
func_NAE()

## Function to Calculate NCC (Normalized Cross Correlation)
def func_NCC():
    global ncc
    ncc = sum((i*j) for i,j in zip(dem_grayscale.pixel_list,dem_grayscale.pixel_list_stego)) / (m.sqrt((sum(i**2 for i in dem_grayscale.pixel_list)) * (sum(j**2 for j in dem_grayscale.pixel_list_stego))))
    print('NCC :',ncc)
func_NCC()

## Function to Calculate EMBEDDING RATE (R)
def func_R():
    global R
    print('Pure_Payload :',dem_grayscale.num_bits_secret)
    print('2*M*N :',2*M*N)
    R = (dem_grayscale.num_bits_secret) / (2*M*N)
    print('R :',R)
func_R()

## Function to Calculate BER (Bit Error Rate)
def func_BER():
    global ber
    ber = (sum(i^j for i,j in zip(dem_grayscale.watermark_alpha_resized_grayscale.flatten(),thresholded_watermark.flatten())) * 100) / (dem_grayscale.count3 - dem_grayscale.count2)
    print('BER :',ber)
func_BER()

