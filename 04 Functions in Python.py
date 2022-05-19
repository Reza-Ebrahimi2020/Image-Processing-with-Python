# -*- coding: utf-8 -*-
"""
Created on Thu May 19 08:32:57 2022

@author: Reza
"""
from skimage import io, filters
from matplotlib import pyplot as plt

def gaussian_of_img(img,sigma=1):
    gaussian_img = filters.gaussian(img, sigma)
    return(gaussian_img)

my_image = io.imread('images/Osteosarcoma_01_8bit_salt_pepper_cropped.tif')

filtered = gaussian_of_img(my_image, 3)

plt.imshow(filtered)
