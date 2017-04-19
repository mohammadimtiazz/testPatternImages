# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:34:28 2017

@author: mimtiaz
"""

import numpy as np
import cv2

#16 by 16 matrix and each block is a 10 by 10 grid
height = 160        #16 *10
width = 160         #16 *10
#divSize = 2
blankImg = np.zeros((height,width), dtype = np.uint8)

gridSize = 10
init = 0
countH = 0
countW = 0

singleRowFill = np.zeros((16,width), dtype = np.uint8)

for i in range(0, 16):
    for j in range(0,width):
        if countW == gridSize:
            init = init + 1
            singleRowFill[i,j] = init
            countW = 0
            countW = countW + 1
        else:
            singleRowFill[i,j] = init
            countW = countW +1
step = 0
for i in range(0,height):
    if countH == gridSize:
        countH = 0
        step = step + 1
        blankImg[i,:] = singleRowFill[step,:]
        countH = countH + 1
    else:
        blankImg[i,:] = singleRowFill[step,:]
        countH = countH + 1
    
cv2.imwrite('smoothTransectionGrayPixBlockWise.bmp', blankImg)
    



#%%
#16 by 16 matrix and each block is a 13 by 13 grid but the middle 10 by 10 will be filled with pixel
height = 256
width = 256
#divSize = 2
blankImg = np.zeros((height,width), dtype = np.uint8)

init = 0
countH = 0
countW = 0

singleRowFill = np.zeros((16,width), dtype = np.uint8)

countIndex = 0
for i in range(0, 16):
    for j in range(0,width):
        if (countIndex <= 12):
            
            singleRowFill[i,j] = init

             
        else:
            pass
#        countIndex = countIndex + 1
        if countIndex == 15:
            countIndex = 0
            init = init + 1
        else:
            countIndex = countIndex + 1

step = 0
countIndex = 0
for i in range(0,height):
    if countIndex <= 12:
        blankImg[i,:] = singleRowFill[step,:]
    else:
        pass
    if countIndex == 15:
        countIndex = 0
        step = step + 1    
    else:
        countIndex = countIndex + 1

    
cv2.imwrite('grayTransectionWithHigherContrast.bmp', blankImg)





