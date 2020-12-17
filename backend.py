# imports
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import ImageEnhance

def gaussian_filter(img, sigma):
    gauss_img = cv2.GaussianBlur(img,(5,5),sigma)
    return gauss_img

# def img_resize(img, size):
#     width = int(img.shape[1] * size / 100)
#     height = int(img.shape[0] * size / 100)
#     dim = (width, height)
#     resized_img = cv2.resize(img, dim)
#     return resized_img

def change_red(img, red):
    img[:,:,2] = (img[:,:,2] * (red/100)).astype(int)
    return img

def change_green(img, green):
    img[:,:,1] = (img[:,:,1] * (green/100)).astype(int)
    return img

def change_blue(img, blue):
    img[:,:,0] = (img[:,:,0] * (blue/100)).astype(int)
    return img

def grayConversion(img):
    grayValue = (0.07 * img[:,:,2]).astype(int) + (0.72 * img[:,:,1]).astype(int) + (0.21 * img[:,:,0]).astype(int)
    img[:,:,0] = grayValue
    img[:,:,1] = grayValue
    img[:,:,2] = grayValue
    return img

# def histogram_equalization(image):
#     equ = cv2.equalizeHist(image)
#     res = np.hstack((image,equ)) #stacking images side-by-side
   

def sharpChanged(image):
    #factor = self.sharpSlide.value()
    # if(factor <= 3):
    #     sharp_kernel = np.array([[-1,-1,-1], [1,7,-1], [-1,-1,-1]])
    
    # if(factor >= 4 or factor <= 8):
    sharp_kernel = np.array([[-1,-1,-1], [1,7,-1], [-1,-1,-1]])
   # sharp_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]) 
    
    # if(factor >=8 ):
    #     sharp_kernel = np.array([[1,1,1], [-1,-3,-1], [1,1,1]])
    #   #  sharp_kernel = np.array([[1,1,1], [1,-7,1], [1,1,1]])

    sharpen = cv2.filter2D(image, -1, sharp_kernel)   
    return sharpen