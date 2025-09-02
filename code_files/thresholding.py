import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import glob 
import pickle
from plot import plot_images

def get_thresholded_sobel(image , orient = 'x' , kernel_size=3 ,threshold = (0,255)):
    if len(image.shape) == 2:
        gray = image
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    if orient =='x':
        sobel = cv2.Sobel(gray , cv2.CV_64F , 1 , 0 , ksize =kernel_size)
    elif orient =='y':
        sobel = cv2.Sobel(gray , cv2.CV_64F , 0 , 1 , ksize =kernel_size)
    sobel = np.uint8(255*np.absolute(sobel)/np.max(np.absolute(sobel)))
    binary_out = np.zeros_like(sobel)
    binary_out[(sobel >= threshold[0]) & (sobel <= threshold[1])] = 1
    return binary_out

def get_thresholed_s_channel(image , threshold = (0,255)):
    image = cv2.cvtColor(image , cv2.COLOR_RGB2HLS)
    s_channel = image[:,:,2]
    binary_out = np.zeros_like(s_channel)
    binary_out[(s_channel >= threshold[0])&(s_channel <= threshold[1])] = 1
    return binary_out


def apply_thresholding(image ,kernel_size ,sobel_threshold=(0,255) ,color_threshold=(0,255)):
    sobelx = get_thresholded_sobel(image , 'x' , kernel_size , sobel_threshold)
    s_channel = get_thresholed_s_channel(image ,color_threshold)
    thresholded_img = np.zeros_like(s_channel)
    thresholded_img[(sobelx == 1) | (s_channel == 1)] = 1
    return thresholded_img


