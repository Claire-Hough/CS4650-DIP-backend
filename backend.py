# imports
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
#from PIL import Image

def gaussian_filter(img):
    gauss_img = cv2.GaussianBlur(img,(5,5),0)
    return gauss_img

def img_resize(img, size):
    width = int(img.shape[1] * size / 100)
    height = int(img.shape[0] * size / 100)
    dim = (width, height)
    resized_img = cv2.resize(img, dim)
    return resized_img

def gray_to_color(img):
    # blue
    img[:,:,0] = (img[:,:,0] * 0.59).astype(int)
    # green
    img[:,:,1] = (img[:,:,1] * 0.11).astype(int)
    #red
    img[:,:,2] = (img[:,:,2] * 0.5).astype(int)
    return img




current_image = cv2.imread("Fig1016(a)(building_original).tif")
cv2.imshow('Original Image', current_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

new_image = gaussian_filter(current_image)
#compare1 = np.concatenate((current_image, new_image), axis =1)
cv2.imshow('Gaussian Filtering', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

new_image = img_resize(current_image, 60)
#compare1 = np.concatenate((current_image, new_image), axis =1)
cv2.imshow('Image Resize', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

new_image = gray_to_color(current_image)
#compare1 = np.concatenate((current_image, new_image), axis =1)
#cv2.imshow('Gray To Color', new_image)
#plt.axis("off")
#plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
cv2.imshow('Gray to Color', new_image)
#plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

