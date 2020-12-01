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
    w, h = img.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, 2] =  ret[:, :, 1] =  ret[:, :, 0] =  img
    return ret

#current_image = input("Enter image name:" sys.argv[1])
#current_image = Image.open(sys.argv[1])
#current_image.save(sys.argv[1])

current_image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
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
plt.axis("off")
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

