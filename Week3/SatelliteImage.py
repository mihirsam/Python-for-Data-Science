# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:59:46 2018

@author: Xenon
"""
import imageio
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

from skimage import data
photo_data = imageio.imread('Numpy/wifire/sd-3layers.jpg')

photo_copy =  photo_data.copy()

rowArray = np.arange(0, 3725, 250)
colArray = np.arange(0, 3725, 250)
print(rowArray.shape, colArray.shape)

a = 0
b = 0
count = 1
for i, j in zip(rowArray, colArray):
        print(i, j, count)
        if count % 2 == 0:
            photo_copy[a:i, b:j] = 255
            count += 1
        else:
            photo_copy[a:i, b:j] = 0
            count += 1
            
        a = i.copy()
        b = j.copy()

plt.figure(figsize=(10, 10))
plt.imshow(photo_data)
        
plt.figure(figsize=(10, 10))
plt.imshow(photo_copy)