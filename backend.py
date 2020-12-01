# imports
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
#from PIL import Image

def gaussian_filter(img):
    gauss_img = cv2.GaussianBlur(img,(5,5),0)
    return gauss_img

#current_image = input("Enter image name:" sys.argv[1])
#current_image = Image.open(sys.argv[1])
#current_image.save(sys.argv[1])

current_image = cv2.imread(sys.argv[1])
new_image = gaussian_filter(current_image)
compare1 = np.concatenate((current_image, new_image), axis =1)
cv2.imshow('Gaussian Filtering', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

