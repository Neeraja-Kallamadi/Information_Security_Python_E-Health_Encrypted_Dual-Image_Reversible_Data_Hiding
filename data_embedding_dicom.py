## Importing Required Packages
import datetime
import math as m
import random as rand
import numpy as np
import pydicom
import cv2
import imageio
import matplotlib.pyplot as plt
import paillier as pa
import char_bin as cb
import gui_embedding_dicom

print("!!! DATA EMBEDDING !!!")
print()

## Initialization of Global Variables
global start_time

## Function to Read DICOM Cover Image
def readDICOMCoverImage():
    ## Initializing Required Variables
    global n,NZ,w,v1,d,red_NZ,no_pixel_list,path,new_path,dicom_cover_img,dicom_cover_image,bits_allocated,pixel_list,pix_loc_dict,min_pixel,max_pixel,mod_value,unique_list,M,N,num_bits_secret,no_pixel_list
    no_pixel_list,pixel_list,pix_loc_dict = [],[],{}
    n,NZ,w = 5,8,''
    v1 = (2*n)+1
    d = m.floor(m.log2((v1*NZ)-1))
    red_NZ = m.ceil((2**d)/v1)
    no_pixel_list = [i for i in range(n)]
    #print('no_pixel_list :',no_pixel_list)
    #print("List of Pixel Values that we cannot use for Embedding :",no_pixel_list)
    ## Take Input Secret Message and DICOM Cover Image from GUI
    gui_embedding_dicom.createDICOMEmbedGUI()
    with open ("DICOM Cover Image Selected.txt","r") as fin:
        name = fin.read()
    path = 'G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/'
    new_path = path + name
    ## Load the DICOM Stego Image
    dicom_cover_img = pydicom.dcmread(f"{new_path}")
    ## Load the DICOM Cover Image - To Plot the DICOM Cover Image in SubPlot
    dicom_cover_image = pydicom.dcmread(f"{new_path}")
    ## Get the Number of Bits Allocated Per Pixel in DICOM Cover Image
    bits_allocated = dicom_cover_image.BitsAllocated
    print("Number of Bits Allocated Per Pixel in DICOM Cover Image :",bits_allocated)
    ## Get all the Pixel Values of a DICOM Cover Image
    for i in dicom_cover_image.pixel_array.flatten(): #pixel_array -> Gives all pixel values in 2D array
                                        #flatten() -> Converts 2D array to 1D array
        pixel_list.append(int(i))
    print('Total Number of Pixels that exists in DICOM Cover Image :',len(pixel_list))
    #print("All Pixels Values of DICOM Cover Image :",pixel_list)
    ## Get the Minimum Pixel Value of the DICOM Cover Image
    min_pixel = min(pixel_list)
    print("Minimum Pixel Value in DICOM Cover Image :",min_pixel)
    ## Get the Maximum Pixel Value of the DICOM Cover Image
    max_pixel = max(pixel_list)
    print("Maximum Pixel Value in DICOM Cover Image :",max_pixel)
    ## Dictionary to get Locations of all Pixels in DICOM Cover Image
    for i in range(max_pixel+1):
        new_list=[]
        for j in range(len(pixel_list)):
            if i == pixel_list[j]:
                new_list.append(j)
        pix_loc_dict[i]=new_list
    #print('All Pixels and their Respective Addresses in DICOM Cover Image :',pix_loc_dict)
    ## Mod Value of DICOM Cover Image
    mod_value = 2**bits_allocated
    print("Mod Value of DICOM Cover Image :",mod_value)
    ## Get all the Unique Pixels Values of the DICOM Cover Image
    unique_list=list(set(pixel_list))
    #print("Unique Pixels Values of DICOM Cover Image :",unique_list)
    ## Get Shape of DICOM Cover Image
    M,N = dicom_cover_image.pixel_array.shape   #shape -> gives dimensions of the image
    print("Shape of DICOM Cover Image :",M,N)
    ## Get Input Binary Data from Text File (Through GUI)
    #gui_embedding_dicom.create_gui()
    cb.char_binary()
    with open('emb_output.txt', 'r') as file:
        w=file.read()
    #print('Actual Secret Message that needs to Embed in DICOM Cover Image :',w)
    ## Get Length of the Actual Secret Message
    num_bits_secret = len(w)
    #print('Length of the Actual Secret Message :',num_bits_secret)
    ## Fill Number of Zeros infront of the Actual Secret Message that needed for Base Paper Algorithm
    w = w.zfill(m.ceil(num_bits_secret/d) * d)
    #print('Secret Message after filling required Number of Zeros :',w)
    print()

## Calculate Start Time of a Program
start_time = datetime.datetime.now().time()

## Function to Choose a Pixel from DICOM Cover Image and dividing it into x and y according to the Base Paper Algorithm
def choosePixel():
    ## Initializing Required Variables
    global p,x,y,flag
    ## Choose random pixel from DICOM Cover Image
    p = rand.choice(pixel_list)
    while p in no_pixel_list:
        p = rand.choice(pixel_list)
    x = m.floor(p/2)
    y = p - x
    while (x in no_pixel_list) or (y in no_pixel_list):
        p = rand.choice(pixel_list)
        x = m.floor(p/2)
        y = p - x
    p = x + y
    if p % 2 == 0 :
        flag = 0
    else :
        flag = 1
    return (p,x,y)

## Function to Choose a Pixel until the Required Conditions are met
def chooseRightPixel():
    ## Initializing Required Variables
    global count1
    count1 = 0
    choosePixel()
    count1 += 1
    while ((len(pix_loc_dict[p]) < 2) or ((flag == 0)and(len(pix_loc_dict[x]) < 4)) or ((flag == 1)and((len(pix_loc_dict[x]) < 2)or(len(pix_loc_dict[y]) < 2)))):
        choosePixel()
        count1 += 1
    return (p,x,y)

## Function to Create Dual Images according to the Base Paper Algorithm
def createDualImages():
    ## Initializing Required Variables
    global p,x1,y1,p_list,p1_list,x_list_p1,y_list_p1,p2_list,x_list_p2,y_list_p2,a,b,x_list_p1_loc,y_list_p1_loc,x_list_p2_loc,y_list_p2_loc
    p_list,p1_list,x_list_p1,y_list_p1,p2_list,x_list_p2,y_list_p2,x_list_p1_loc,y_list_p1_loc,x_list_p2_loc,y_list_p2_loc = [],[],[],[],[],[],[],[],[],[],[]
    for i in range(m.ceil(num_bits_secret/d)):
        p,x1,y1 = chooseRightPixel()
        p_list.append(p)
        p1_list.append(p)
        x_list_p1.append(x1)
        y_list_p1.append(y1)
        p2_list.append(p)
        x_list_p2.append(x1)
        y_list_p2.append(y1)
        a=pix_loc_dict[x_list_p1[i]]
        b=a.pop(a.index(rand.choice(a)))
        pix_loc_dict[x_list_p1[i]]=a
        x_list_p1_loc.append(b)
        a=pix_loc_dict[y_list_p1[i]]
        b=a.pop(a.index(rand.choice(a)))
        pix_loc_dict[y_list_p1[i]]=a
        y_list_p1_loc.append(b)
        a=pix_loc_dict[x_list_p2[i]]
        b=a.pop(a.index(rand.choice(a)))
        pix_loc_dict[x_list_p2[i]]=a
        x_list_p2_loc.append(b)
        a=pix_loc_dict[y_list_p2[i]]
        b=a.pop(a.index(rand.choice(a)))
        pix_loc_dict[y_list_p2[i]]=a
        y_list_p2_loc.append(b)

## Function to get Encrypted CI1 and Encrypted CI2
def getEncryptedDualImages():
    ## Initializing Required Variables
    global enc_x_p1,enc_y_p1,enc_p1_x_list,enc_p1_y_list,enc_x_p2,enc_y_p2,enc_p2_x_list,enc_p2_y_list
    enc_p1_x_list,enc_p1_y_list,enc_p2_x_list,enc_p2_y_list = [],[],[],[]
    for i in range(len(x_list_p1)):
        enc_x_p1,enc_y_p1 = (pa.encrypt(x_list_p1[i],pa.public_key)) , (pa.encrypt(y_list_p1[i],pa.public_key))
        enc_x_p1,enc_y_p1 = enc_x_p1 % mod_value , enc_y_p1 % mod_value
        enc_p1_x_list.append(enc_x_p1) , enc_p1_y_list.append(enc_y_p1)
        enc_x_p2,enc_y_p2 = (pa.encrypt(x_list_p2[i],pa.public_key)) , (pa.encrypt(y_list_p2[i],pa.public_key))
        enc_x_p2,enc_y_p2 = enc_x_p2 % mod_value , enc_y_p2 % mod_value
        enc_p2_x_list.append(enc_x_p2) , enc_p2_y_list.append(enc_y_p2)
    return (enc_p1_x_list,enc_p1_y_list,enc_p2_x_list,enc_p2_y_list)

## Function to get Encrypted Reduced Zone and Encrypted Reduced Secret Message
def getEncryptedZoneAndSecret(w):
    ## Initializing Required Variables
    global temp1,sub_w,num,num_list,z,CZ,z_list,red_z,red_w,red_z_list,red_w_list,enc_red_z,enc_red_w,enc_red_z_list,enc_red_w_list
    temp1,sub_w,num_list,z_list,red_z_list,red_w_list,enc_red_z_list,enc_red_w_list= 0,'',[],[],[],[],[],[]
    for i in w:
        temp1 += 1
        sub_w += i
        if temp1 == d:
            num = int(sub_w,2)
            num_list.append(str(num))
            temp1,sub_w = 0,''
    for i in range(len(num_list)):
        z = m.floor(int(num_list[i])/v1)
        CZ = (z*v1)+n
        z_list.append(z)
        red_z , red_w = z - (m.floor((red_NZ)/2)) , (int(num_list[i]))-CZ
        red_z_list.append(red_z) , red_w_list.append(red_w)
        enc_red_z,enc_red_w = pa.encrypt(red_z,pa.public_key) , pa.encrypt(red_w,pa.public_key)
        enc_red_z,enc_red_w = enc_red_z % mod_value,enc_red_w % mod_value
        enc_red_z_list.append(enc_red_z) , enc_red_w_list.append(enc_red_w)
    return (enc_red_z_list,enc_red_w_list)

## Function to get Stego Images SI1 and SI2
def getStegoImages():
    ## Initializing Required Variables
    global enc_emb_p1_x,enc_emb_p1_y,t_p1_x_list,t_p1_y_list,enc_emb_p2_x,enc_emb_p2_y,t_p2_x_list,t_p2_y_list,rhs1_p1_x,rhs1_p1_x_mod,rhs1_p1_y,rhs1_p1_y_mod,lhs1_p1_x,lhs1_p1_y,rhs1_p1_x_list,rhs1_p1_y_list,enc_emb_p1_x_list,enc_emb_p1_y_list,lhs2_p1_x,lhs2_p1_y,lhs2_p1_x_list,lhs2_p1_y_list,rhs2_p1,rhs2_p1_list,rhs1_p2_x,rhs1_p2_x_mod,rhs1_p2_y,rhs1_p2_y_mod,lhs1_p2_x,lhs1_p2_y,rhs1_p2_x_list,rhs1_p2_y_list,enc_emb_p2_x_list,enc_emb_p2_y_list,lhs2_p2_x,lhs2_p2_y,lhs2_p2_x_list,lhs2_p2_y_list,rhs2_p2,rhs2_p2_list
    t_p1_x_list,t_p1_y_list,t_p2_x_list,t_p2_y_list,rhs1_p1_x_list,rhs1_p1_y_list,enc_emb_p1_x_list,enc_emb_p1_y_list,lhs2_p1_x_list,lhs2_p1_y_list,rhs2_p1_list,rhs1_p2_x_list,rhs1_p2_y_list,enc_emb_p2_x_list,enc_emb_p2_y_list,lhs2_p2_x_list,lhs2_p2_y_list,rhs2_p2_list = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    ## Embedding in First Cover Image
    for i in range(len(enc_p1_x_list)):
        enc_emb_p1_x , enc_emb_p1_y = enc_p1_x_list[i] + enc_red_z_list[i] , enc_p1_y_list[i] - enc_red_z_list[i]
        #print('i :',i)
        #print('enc_emb_p1_x , enc_emb_p1_y (before mod) :',enc_emb_p1_x , enc_emb_p1_y)
        enc_emb_p1_x , enc_emb_p1_y = enc_emb_p1_x % mod_value , enc_emb_p1_y % mod_value
        #print('enc_emb_p1_x , enc_emb_p1_y (after mod) :',enc_emb_p1_x , enc_emb_p1_y)
        #print()
        t_p1_x_list.append(enc_emb_p1_x) , t_p1_y_list.append(enc_emb_p1_y)
    ## Embedding in Second Cover Image
    for i in range(len(enc_p2_x_list)):
        enc_emb_p2_x , enc_emb_p2_y = enc_p2_x_list[i] + enc_red_w_list[i] , enc_p2_y_list[i] - enc_red_w_list[i]
        #print('i :',i)
        #print('enc_emb_p2_x , enc_emb_p2_y (before mod) :',enc_emb_p2_x , enc_emb_p2_y)
        enc_emb_p2_x , enc_emb_p2_y = enc_emb_p2_x % mod_value , enc_emb_p2_y % mod_value
        #print('enc_emb_p2_x , enc_emb_p2_y (after mod) :',enc_emb_p2_x , enc_emb_p2_y)
        #print()
        t_p2_x_list.append(enc_emb_p2_x) , t_p2_y_list.append(enc_emb_p2_y)
    ## First Cover Image
    ## Condition Check - 1 : Encrypted (x of CI1) + Encrypted (Reduced Zone) = Encrypted Value of (x of CI1 + Reduced Zone)
    for i in range(len(t_p1_x_list)):
        rhs1_p1_x = (pa.encrypt((x_list_p1[i] + red_z_list[i]),pa.public_key))
        rhs1_p1_x_mod = rhs1_p1_x % mod_value
        rhs1_p1_y = (pa.encrypt((y_list_p1[i] - red_z_list[i]),pa.public_key))
        rhs1_p1_y_mod = rhs1_p1_y % mod_value
        lhs1_p1_x = t_p1_x_list[i]
        while (lhs1_p1_x != rhs1_p1_x_mod) :
            rhs1_p1_x = (pa.encrypt((x_list_p1[i] + red_z_list[i]),pa.public_key))
            rhs1_p1_x_mod = rhs1_p1_x % mod_value
        lhs1_p1_y = t_p1_y_list[i]
        while (lhs1_p1_y != rhs1_p1_y_mod) :
            rhs1_p1_y = (pa.encrypt((y_list_p1[i] - red_z_list[i]),pa.public_key))
            rhs1_p1_y_mod = rhs1_p1_y % mod_value
        #print('i :',i)
        #print('lhs1_p1_x,rhs1_p1_x_mod (Condition Check - 1) :',lhs1_p1_x,rhs1_p1_x_mod)
        #print('lhs1_p1_y,rhs1_p1_y_mod (condition Check - 1) :',lhs1_p1_y,rhs1_p1_y_mod)
        #print('x_list_p1[i] :',x_list_p1[i])
        #print('y_list_p1[i] :',y_list_p1[i])
        rhs1_p1_x_list.append(rhs1_p1_x)
        rhs1_p1_y_list.append(rhs1_p1_y)
        enc_emb_p1_x_list.append(rhs1_p1_x_mod)
        enc_emb_p1_y_list.append(rhs1_p1_y_mod)
    ## Condition Check - 2 : Encrypted (Embedded x of CI1 + Embedded y of CI1) = (Encrypted (Embedded x of CI1) * Encrypted (Embedded y of CI1))
        ## or
    ## Condition Check - 2 : (Embedded x of CI1 + Embedded y of CI1) = Decrypted ((Encrypted (Embedded x of CI1) * Encrypted (Embedded y of CI1)))
        lhs2_p1_x = (pa.decrypt(rhs1_p1_x,pa.private_key,pa.public_key)) % mod_value
        lhs2_p1_y = (pa.decrypt(rhs1_p1_y,pa.private_key,pa.public_key)) % mod_value
        lhs2_p1_x_list.append(lhs2_p1_x)
        lhs2_p1_y_list.append(lhs2_p1_y)
        rhs2_p1 = (pa.decrypt((rhs1_p1_x * rhs1_p1_y),pa.private_key,pa.public_key)) % mod_value
        #print('lhs2_p1_x,lhs2_p1_y,rhs2_p1 (Condition Check - 2) :',lhs2_p1_x,lhs2_p1_y,rhs2_p1)
        #print()
        rhs2_p1_list.append(rhs2_p1)
    ## Second Cover Image
    ## Condition Check - 1 : Encrypted (x of CI2) + Encrypted (Reduced Zone) = Encrypted Value of (x of CI2 + Reduced Zone)
    for i in range(len(t_p2_x_list)):
        rhs1_p2_x = (pa.encrypt((x_list_p2[i] + red_w_list[i]), pa.public_key))
        rhs1_p2_x_mod = rhs1_p2_x % mod_value
        rhs1_p2_y = (pa.encrypt((y_list_p2[i] - red_w_list[i]), pa.public_key))
        rhs1_p2_y_mod = rhs1_p2_y % mod_value
        lhs1_p2_x = t_p2_x_list[i]
        while (lhs1_p2_x != rhs1_p2_x_mod) :
            rhs1_p2_x = (pa.encrypt((x_list_p2[i] + red_w_list[i]),pa.public_key))
            rhs1_p2_x_mod = rhs1_p2_x % mod_value
        lhs1_p2_y = t_p2_y_list[i]
        while (lhs1_p2_y != rhs1_p2_y_mod) :
            rhs1_p2_y = (pa.encrypt((y_list_p2[i] - red_w_list[i]),pa.public_key))
            rhs1_p2_y_mod = rhs1_p2_y % mod_value
        #print('i :',i)
        #print('lhs1_p2_x,rhs1_p2_x_mod (Condition Check - 1) :',lhs1_p2_x,rhs1_p2_x_mod)
        #print('lhs1_p2_y,rhs1_p2_y_mod (Condition Check - 1) :',lhs1_p2_y,rhs1_p2_y_mod)
        #print('x_list_p2[i] :',x_list_p2[i])
        #print('y_list_p2[i] :',y_list_p2[i])
        rhs1_p2_x_list.append(rhs1_p2_x)
        rhs1_p2_y_list.append(rhs1_p2_y)
        enc_emb_p2_x_list.append(rhs1_p2_x_mod)
        enc_emb_p2_y_list.append(rhs1_p2_y_mod)
    ## Condition Check - 2 : Encrypted (Embedded x of CI2 + Embedded y of CI2 = (Encrypted (Embedded x of CI2) * Encrypted (Embedded y of CI2))
        ## or
    ## Condition Check - 2 : (Embedded x of CI2 + Embedded y of CI2) = Decrypted ((Encrypted (Embedded x of CI2) * Encrypted (Embedded y of CI2)))
        lhs2_p2_x = (pa.decrypt(rhs1_p2_x,pa.private_key,pa.public_key)) % mod_value
        lhs2_p2_y = (pa.decrypt(rhs1_p2_y,pa.private_key,pa.public_key)) % mod_value
        lhs2_p2_x_list.append(lhs2_p2_x)
        lhs2_p2_y_list.append(lhs2_p2_y)
        rhs2_p2 = (pa.decrypt((rhs1_p2_x * rhs1_p2_y),pa.private_key,pa.public_key)) % mod_value
        #print('lhs2_p2_x,lhs2_p2_y,rhs2_p2 (Condition Check - 2) :',lhs2_p2_x,lhs2_p2_y,rhs2_p2)
        #print()
        rhs2_p2_list.append(rhs2_p2)
    ## Printing Encrypted Embedded x of CI1 (before mod value)
    #print("Encrypted Embedded x of CI1 (before mod value) :",rhs1_p1_x_list)
    ## Printing Encrypted Embedded y of CI1 (before mod value)
    #print("Encrypted Embedded y of CI1 (before mod value) :",rhs1_p1_y_list)
    ## Printing Encrypted Embedded x of CI1
    #print("Encrypted Embedded x of CI1 (after mod value) :",enc_emb_p1_x_list)
    ## Printing Encrypted Embedded y of CI1
    #print("Encrypted Embedded y of CI1 (after mod value) :",enc_emb_p1_y_list)
    ## Printing Embedded x of CI1
    #print("Embedded x of CI1 :",lhs2_p1_x_list)
    ## Printing Embedded y of CI1
    #print("Embedded y of CI1 :",lhs2_p1_y_list)
    ## Printing Decrypted ((Encrypted(Embedded x of CI1)) * (Encrypted(Embedded y of CI1)))
    #print("Decrypted ((Encrypted(Embedded x of CI1)) * (Encrypted(Embedded y of CI1))) :",rhs2_p1_list)
    #print()
    ## Printing Encrypted Embedded x of CI2 (before mod value)
    #print("Encrypted Embedded x of CI2 (before mod value) :",rhs1_p2_x_list)
    ## Printing Encrypted Embedded y of CI2 (before mod value)
    #print("Encrypted Embedded y of CI2 (before mod value) :",rhs1_p2_y_list)
    ## Printing Encrypted Embedded x of CI2
    #print("Encrypted Embedded x of CI2 :",enc_emb_p2_x_list)
    ## Printing Encrypted Embedded y of CI2
    #print("Encrypted Embedded y of CI2 :",enc_emb_p2_y_list)
    ## Printing Embedded x of CI2
    #print("Embedded x of CI2 :",lhs2_p2_x_list)
    ## Printing Embedded y of CI2
    #print("Embedded y of CI2 :",lhs2_p2_y_list)
    ## Printing Decrypted ((Encrypted(Embedded x of CI2)) * (Encrypted(Embedded y of CI2)))
    #print("Decrypted ((Encrypted(Embedded x of CI2)) * (Encrypted(Embedded y of CI2))) :",rhs2_p2_list)
    #print()
    ## Print all the Required Values
    if (len(enc_emb_p1_x_list) == len(enc_p1_x_list)) or (len(enc_emb_p2_x_list) == len(enc_p2_x_list)) :
        print("!!! Step - 1 !!!")
        print()
        print("Total Number of Iteration Occured to Choose Right Pixels according to the Base Paper Algorithm :",count1)
        print()
        print("!! Pixels of Cover Image (DICOM) !!")
        print("Pixels of CI :",p_list)
        print("!! Pixels of First Cover Image (DICOM) !!")
        print("Pixels of CI1 :",p1_list)
        print("!! Pixels of Second Cover Image (DICOM) !!")
        print("Pixels of CI2 :",p2_list)
        print()
        print("!! x and y of First Cover Image (DICOM) !!")
        print("Pixels of x and y of CI1 :", x_list_p1, y_list_p1)
        print("!! x and y of Second Cover Image (DICOM) !!")
        print("Pixels of x and y of CI2 :", x_list_p2, y_list_p2)
        print()
        print("!! Locations of x and y of First Cover Image (DICOM) !!")
        print("Locations of x and y of CI1 :",x_list_p1_loc,y_list_p1_loc)
        print("!! Locations of x and y of Second Cover Image (DICOM) !!")
        print("Locations of x and y of CI2 :",x_list_p2_loc,y_list_p2_loc)
        print()
        print("!! Encrypted x and Encrypted y of DICOM Cover Images !!")
        print("Pixels of Encrypted x and Encrpted y of CI1 :", enc_p1_x_list, enc_p1_y_list)
        print("Pixels of Encrypted x and Encrpted y of CI2 :", enc_p2_x_list, enc_p2_y_list)
        print()
        print()
        print("!!! Step - 2 !!!")
        print()
        print("!! Secret Message in Binary !!")
        print(w)
        print()
        print("!! Secret Message in Decimal !!")
        print(num_list)
        print()
        print("!! Zone Values !!")
        print(z_list)
        print()
        print("!! Reduced Zone Values !!")
        print(red_z_list)
        print()
        print("!! Reduced Secret Messages in Decimal !!")
        print(red_w_list)
        print()
        print("!! Encrypted Reduced Zone and Encrypted Reduced Secret Message in Decimal !!")
        print("Encrypted Values of Reduced Zone :", enc_red_z_list)
        print("Encrypted Values of Reduced Secret Message in Decimal :", enc_red_w_list)
        print()
        print()
        print("!!! Step - 3 !!!")
        print()
        print("!! GrayScale Stego Images !!")
        print("Stego Pixels of x and y of SI1 :", enc_emb_p1_x_list, enc_emb_p1_y_list)
        print("Stego Pixels of x and y of SI2 :", enc_emb_p2_x_list, enc_emb_p2_y_list)
        print()
        print()
    return (enc_emb_p1_x_list,enc_emb_p1_y_list,enc_emb_p2_x_list,enc_emb_p2_y_list)

## Function to Plot Cover Image and Stego Image
def plotDICOMCoverAndEncrpted():
    ## Initializing Required Variables
    global x,y,new_value,dicom_encrypted_image
    ## Modify pixels
    print("!! Original and Encrypted Pixels of x of CI1 !!")
    for i in range(len(x_list_p1_loc)):
        x=x_list_p1_loc[i]%dicom_cover_img.pixel_array.shape[1]
        y=x_list_p1_loc[i]//dicom_cover_img.pixel_array.shape[1]
        new_value = enc_p1_x_list[i] # Set new value for the pixel at (x,y)
        print("Original Pixel Value :",dicom_cover_img.pixel_array[y,x],end = ' ')
        dicom_cover_img.pixel_array[y,x] = new_value # Update pixel value in the image
        print("Encrypted Pixel Value :",dicom_cover_img.pixel_array[y,x])
    print()
    print("!! Original and Encrypted Pixels of y of CI1 !!")
    for i in range(len(y_list_p1_loc)):
        x=y_list_p1_loc[i]%dicom_cover_img.pixel_array.shape[1]
        y=y_list_p1_loc[i]//dicom_cover_img.pixel_array.shape[1]
        print("Original Pixel Value :",dicom_cover_img.pixel_array[y,x],end = ' ')
        new_value = enc_p1_y_list[i]  # Set new value for the pixel at (x,y)
        dicom_cover_img.pixel_array[y,x] = new_value  # Update pixel value in the image
        print("Encrypted Pixel Value :",dicom_cover_img.pixel_array[y,x])
    print()
    print("!! Original and Encrypted Pixels of x of CI2 !!")
    for i in range(len(x_list_p2_loc)):
        x=x_list_p2_loc[i]%dicom_cover_img.pixel_array.shape[1]
        y=x_list_p2_loc[i]//dicom_cover_img.pixel_array.shape[1]
        print("Original Pixel Value :",dicom_cover_img.pixel_array[y,x],end = ' ')
        new_value = enc_p2_x_list[i]     # Set new value for the pixel at (x,y)
        dicom_cover_img.pixel_array[y,x] = new_value  # Update pixel value in the image
        print("Encrypted Pixel Value :",dicom_cover_img.pixel_array[y,x])
    print()
    print("!! Original and Encrypted Pixels of y of CI2 !!")
    for i in range(len(y_list_p2_loc)):
        x=y_list_p2_loc[i]%dicom_cover_img.pixel_array.shape[1]
        y=y_list_p2_loc[i]//dicom_cover_img.pixel_array.shape[1]
        print("Original Pixel Value :",dicom_cover_img.pixel_array[y,x],end = ' ')
        new_value = enc_p2_y_list[i]     # Set new value for the pixel at (x,y)
        dicom_cover_img.pixel_array[y,x] = new_value  # Update pixel value in the image
        print("Encrypted Pixel Value :",dicom_cover_img.pixel_array[y,x])
    print()
    ## Update the DICOM Object with the Modified Pixel Data
    dicom_cover_img.PixelData = dicom_cover_img.pixel_array.tobytes()
    ## Save the Updated DICOM Object to a New File or Overwrite the Original File
    dicom_cover_img.save_as("dicom_encrypted_image.dcm")
    ## Read the DICOM Image
    dicom_encrypted_image = pydicom.dcmread("dicom_encrypted_image.dcm")

## Function to Plot Cover Image and Stego Image
def plotDICOMEncryptedAndStego():
    ## Initializing Required Variables
    global x,y,new_value,dicom_stego_image,pixel_array1,pixel_array2,pixel_array3,pixel_list_stego,watermark,watermark_alpha,watermark_alpha_resized,watermarked_img,watermarked_dicom_stego_image,dicom_stego_wimg,fig,axes,ax1,ax2,ax3,ax4,count2,count3,pixel_list_watermarked,end_time,startdatetime,enddatetime,execution_time
    pixel_list_stego,count2,count3,pixel_list_watermarked = [],0,0,[]
    ## Modify pixels
    print("!! Encrypted and Modified Pixels of x of CI1 !!")
    for i in range(len(x_list_p1_loc)):
        x=x_list_p1_loc[i]%dicom_cover_img.pixel_array.shape[1]
        y=x_list_p1_loc[i]//dicom_cover_img.pixel_array.shape[1]
        new_value = enc_emb_p1_x_list[i] # Set new value for the pixel at (x,y)
        print("Encrypted Pixel Value :",dicom_cover_img.pixel_array[y,x],end = ' ')
        dicom_cover_img.pixel_array[y,x] = new_value # Update pixel value in the image
        print("Modified Pixel Value :",dicom_cover_img.pixel_array[y,x])
    print()
    print("!! Encrypted and Modified Pixels of y of CI1 !!")
    for i in range(len(y_list_p1_loc)):
        x=y_list_p1_loc[i]%dicom_cover_img.pixel_array.shape[1]
        y=y_list_p1_loc[i]//dicom_cover_img.pixel_array.shape[1]
        print("Encrypted Pixel Value :",dicom_cover_img.pixel_array[y,x],end = ' ')
        new_value = enc_emb_p1_y_list[i]  # Set new value for the pixel at (x,y)
        dicom_cover_img.pixel_array[y,x] = new_value  # Update pixel value in the image
        print("Modified Pixel Value :",dicom_cover_img.pixel_array[y,x])
    print()
    print("!! Encrypted and Modified Pixels of x of CI2 !!")
    for i in range(len(x_list_p2_loc)):
        x=x_list_p2_loc[i]%dicom_cover_img.pixel_array.shape[1]
        y=x_list_p2_loc[i]//dicom_cover_img.pixel_array.shape[1]
        print("Encrypted Pixel Value :",dicom_cover_img.pixel_array[y,x],end = ' ')
        new_value = enc_emb_p2_x_list[i]     # Set new value for the pixel at (x,y)
        dicom_cover_img.pixel_array[y,x] = new_value  # Update pixel value in the image
        print("Modified Pixel Value :",dicom_cover_img.pixel_array[y,x])
    print()
    print("!! Encrypted and Modified Pixels of y of CI2 !!")
    for i in range(len(y_list_p2_loc)):
        x=y_list_p2_loc[i]%dicom_cover_img.pixel_array.shape[1]
        y=y_list_p2_loc[i]//dicom_cover_img.pixel_array.shape[1]
        print("Encrypted Pixel Value :",dicom_cover_img.pixel_array[y,x],end = ' ')
        new_value = enc_emb_p2_y_list[i]     # Set new value for the pixel at (x,y)
        dicom_cover_img.pixel_array[y,x] = new_value  # Update pixel value in the image
        print("Modified Pixel Value :",dicom_cover_img.pixel_array[y,x])
    print()
    ## Update the DICOM Object with the Modified Pixel Data
    dicom_cover_img.PixelData = dicom_cover_img.pixel_array.tobytes()
    ## Save the Updated DICOM Object to a New File or Overwrite the Original File
    dicom_cover_img.save_as("dicom_stego_image.dcm")
    ## Read the DICOM image
    dicom_stego_image = pydicom.dcmread("dicom_stego_image.dcm")
    #print('dicom_stego_image :',dicom_stego_image.pixel_array)
    ## Read the DICOM image - Copy For Sake of Watermark
    dicom_stego_wimg = pydicom.dcmread("dicom_stego_image.dcm")
    #print('dicom_stego_wimg (Before Watermarked) :',dicom_stego_wimg.pixel_array)
    ## Get the Pixel Data from Each DICOM Object
    pixel_array1 = dicom_cover_image.pixel_array
    pixel_array2 = dicom_encrypted_image.pixel_array
    pixel_array3 = dicom_stego_image.pixel_array
    ## Get all the Pixel Values of a DICOM Stego Image
    for i in dicom_stego_image.pixel_array.flatten(): #pixel_array -> Gives all pixel values in 2D array
                                        #flatten() -> Converts 2D array to 1D array
        pixel_list_stego.append(int(i))
    #print('Total Number of Pixels that exists in DICOM Stego Image :',len(pixel_list_stego))
    #print("All Pixels Values of DICOM Stego Image :",pixel_list_stego)
    ## Printing DICOM Cover Image Pixel and DICOM Stego Image Pixel
    for i,j in zip(pixel_list,pixel_list_stego):
        if i != j:
            #print('Cover Image Pixel,Stego Image Pixel (DICOM):',i,j)
            pass
    # Load the 256x256 Grayscale Image as the Watermark
    watermark = cv2.imread('G:/6th Sem Related Documents(SASTRA)/Mini Project - Anushiadevi.R/Code and Input Images/Code/watermark_256_8bit.jpg', cv2.IMREAD_GRAYSCALE)
    # Convert the Watermark to a Transparent Image by setting the Alpha Channel to a value between 0 and 1
    watermark_alpha = np.zeros((256, 256), dtype=np.uint8)
    watermark_alpha[:, :] = watermark
    watermark_alpha[:, :] = 50  # Set the alpha channel to a value of 50 (between 0 and 255)
    # Resize the Transparent Watermark to match the Size of the  dicom_stego_image
    watermark_alpha_resized = cv2.resize(watermark_alpha, dicom_stego_wimg.pixel_array.shape)
    print("Pixels of Embedded Watermark :",watermark_alpha_resized)
    print()
    # Blend the Transparent Watermark with the dicom_stego_image using "Alpha Blending Technique"
    watermarked_img = cv2.addWeighted(dicom_stego_wimg.pixel_array, 1, watermark_alpha_resized, 0.5, 0,dtype=cv2.CV_16U)
    # Convert the Watermarked DICOM Stego Image back to a DICOM Object
    dicom_stego_wimg.PixelData = watermarked_img.tobytes()
    dicom_stego_wimg.Rows, dicom_stego_wimg.Columns = watermarked_img.shape
    # Save the watermarked DICOM image
    dicom_stego_wimg.save_as('watermarked_dicom_stego_image.dcm')
    #print('dicom_stego_wimg (After Watermarked) :',dicom_stego_wimg.pixel_array)
    ## Create a Matplotlib Figure with Four Subplots
    fig,(ax1, ax2, ax3, ax4) = plt.subplots(nrows=1, ncols=4, figsize=(13, 5))
    ## Display the Cover Image in Left Sub Plot
    ax1.imshow(pixel_array1, cmap='gray')
    ## Add the DICOM Cover Image Title in Left Sub Plot
    ax1.set_title("DICOM Cover Image")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ## Display the Encrypted Image in Middle Sub Plot
    ax2.imshow(pixel_array2, cmap='gray')
    ## Add the DICOM Encrypted Image Title in middle Sub Plot
    ax2.set_title("DICOM Encrypted Image")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ## Display the Stego Image in Middle Sub Plot
    ax3.imshow(pixel_array3, cmap='gray')
    ## Add the DICOM Stego Image Title in Middle Sub Plot
    ax3.set_title("DICOM Stego Image")
    ax3.set_xlabel("X")
    ax3.set_ylabel("Y")
    ## Display the Stego Image in Right Sub Plot
    ax4.imshow(pixel_array3, cmap='gray')
    ## Add the DICOM Stego Image Title in Right Sub Plot
    ax4.set_title("Watermarked DICOM Stego Image")
    ax4.set_xlabel("X")
    ax4.set_ylabel("Y")
    ## Get all the Pixel Values of a Watermarked DICOM Stego Image
    for i in dicom_stego_wimg.pixel_array.flatten(): #pixel_array -> Gives all pixel values in 2D array
                                        #flatten() -> Converts 2D array to 1D array
        pixel_list_watermarked.append(int(i))
    #print("Total Number of Pixels in Watermarked DICOM Stego Image :",len(pixel_list_watermarked))
    for i,j in zip(pixel_list_stego,pixel_list_watermarked):
        if i == j:
            #print(i,j)
            count2 += 1
        if i != j:
            count3 += 1
    print('Total Number of Pixels Watermarked :',count3 - count2)
    print()
    ## Calculate End Time of a Program
    end_time = datetime.datetime.now().time()
    ## Calculate Starting Date and Time of Execution of Program
    startdatetime = datetime.datetime.combine(datetime.date.today(), start_time)
    ## Calculate Ending Date and Time of Execution of Program
    enddatetime = datetime.datetime.combine(datetime.date.today(), end_time)
    ## Calculate the Execution Time
    execution_time= enddatetime - startdatetime
    print("The current time befor execution is:", start_time)
    print("The current time after execution is:", end_time)
    print("total time taken for execution is:",execution_time)
    print()
    print()
    print()
    ## Show the SubPlots
    plt.show()

## Function Call
readDICOMCoverImage()
createDualImages()
getEncryptedDualImages()
getEncryptedZoneAndSecret(w)
getStegoImages()
plotDICOMCoverAndEncrpted()
plotDICOMEncryptedAndStego()




