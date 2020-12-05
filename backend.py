# imports
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
#from PIL import Image

def gaussian_filter(img, sigma):
    gauss_img = cv2.GaussianBlur(img,(5,5),sigma)
    return gauss_img

def img_resize(img, size):
    width = int(img.shape[1] * size / 100)
    height = int(img.shape[0] * size / 100)
    dim = (width, height)
    resized_img = cv2.resize(img, dim)
    return resized_img

def gray_to_color(img, red, green, blue):
    # blue
    img[:,:,0] = (img[:,:,0] * blue).astype(int)
    # green
    img[:,:,1] = (img[:,:,1] * green).astype(int)
    #red
    img[:,:,2] = (img[:,:,2] * red).astype(int)
    return img




current_image = cv2.imread("Fig1016(a)(building_original).tif")
cv2.imshow('Original Image', current_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

new_image = gaussian_filter(current_image, 10)
cv2.imshow('Gaussian Filtering', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

new_image = gray_to_color(current_image, 0.6, 1, 0.33)
cv2.imshow('Gray to Color', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

new_image = gray_to_color(current_image, 1.8, 0.7, 1.8)
cv2.imshow('Gray to Color', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()