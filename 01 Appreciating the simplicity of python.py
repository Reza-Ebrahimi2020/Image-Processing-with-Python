# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:23:28 2022

@author: Reza
"""

from skimage import io, filters
from matplotlib import pyplot as plt
img = io.imread('images/Osteosarcoma_01_25Sigma_noise.tif')

gaussian_img = filters.gaussian(img, sigma=2)

plt.imshow(gaussian_img)