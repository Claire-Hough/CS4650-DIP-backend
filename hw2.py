#!/usr/bin/env python
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

def meanFilter(im):
    img = im
    w = 2

    for i in range(2,im.shape[0]-2):
        for j in range(2,im.shape[1]-2):
            block = im[i-w:i+w+1, j-w:j+w+1]
            m = np.mean(block,dtype=np.float32)
            img[i][j] = int(m)
    return img

def grayConversion(image):
	grayValue = 0.07 * image[:,:,2] + 0.72 * image[:,:,1] + 0.21 * image[:,:,0]
	gray_img = grayValue.astype(np.uint8)
	return gray_img
	#gray_img = grayValue.astype(np.uint8)
	

if __name__ == "__main__":

	print('\nPart 1\n')
	img = cv2.imread('Fig0335.tif')
	imgAgain = cv2.imread('Fig0335.tif')
	median = cv2.medianBlur(img, 5)
	gauss = cv2.GaussianBlur(img, (5,5), 0)
	#compare = np.concatenate((img, median), axis=1)
	compare = np.concatenate((img, gauss), axis =1)

	print('\nGaussian, Averaging Filter\n')
	cv2.imshow('Guassian Filtering', compare)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


	print('\nMedian Filter\n')
	compare2 = np.concatenate((img, median), axis =1)
	cv2.imshow('Median Filtering', compare2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	mean_img = np.asarray(img)
	imgMean = meanFilter(mean_img)
	compare1 = np.concatenate((imgAgain, imgMean), axis =1)
	cv2.imshow('Mean Filtering', compare1)
	cv2.waitKey(0)


	print('\nPart 2\n')

	img2 = cv2.imread('Fig0338.tif')

	kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
	sharpening = cv2.filter2D(img2, -1, kernel)
	compare3 = np.concatenate((img2, sharpening), axis =1)

	cv2.imshow('Sharpning Filter', compare3)
	cv2.waitKey(0)


	print('\nPart 3\n')

	cv2.startWindowThread()

	pyr_img = cv2.imread('StanfordBunny.jpg',0)


	gaus_pyr = pyr_img.copy()
	gpA = [gaus_pyr]
	for i in range(4):
		plt.subplot(2, 2, i + 1) 

		gaus_pyr = cv2.pyrDown(gaus_pyr)
		cv2.imshow('Guassian Pyramid', gaus_pyr)
		cv2.waitKey(60000)

	cv2.destroyAllWindows()
	cv2.waitKey(60000)
	sys.exit()
	


