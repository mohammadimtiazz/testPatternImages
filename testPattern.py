# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:34:28 2017

@author: mimtiaz
"""

import numpy as np
import cv2

height = 100
width = 100
#divSize = 2
blankImg = np.zeros((height,width), dtype = np.uint8)

cv2.imwrite('blankImg.bmp', blankImg)

#%% Test pattern with high contrast like chass board with defined shape
blankImg1 = blankImg
init = 0
lengthBoxH = 25         
lengthBoxW = 25


#init = 0
#for i in range(0, height):
#    init = abs(init - 255)
#    for j in range(0,width):
#        blankImg1[i,j] = init
#        init = abs(init - 255)
#
#cv2.imwrite('ChaseBoardimgX.bmp', blankImg)

init = 0
countH = 0
countW = 0
for i in range(0, height):
    if countH == lengthBoxH:
        init = abs(init - 255)
        countH = 0
        countH = countH + 1
    else:
        countH = countH + 1
    for j in range(0,width):
        if countW == lengthBoxW:
            countW = 0
            init = abs(init - 255)
            blankImg1[i,j] = init
            countW = countW + 1
        else:
            blankImg1[i,j] = init
            countW = countW + 1

nameImg = 'chassBoardImg' + str(lengthBoxH) + 'by' + str(lengthBoxW) + '.bmp'
cv2.imwrite(nameImg, blankImg1)
    


#%% Test pattern of smooth transection of gray values vertically 
img = np.zeros((256,256), dtype = np.uint8)
for i in range(0,256):
    for j in range(0,256):
        img[i,j] = j
cv2.imwrite('smoothTranscitionGrayVertical.bmp', img)

#%% Test pattern of smooth transection of gray values horizentally
img = np.zeros((256,256), dtype = np.uint8)

for i in range(0,256):
    for j in range(0,256):
        img[i,j] = i
cv2.imwrite('smoothTranscitionGrayHorizental.bmp', img)


#%% Test pattern of  gray values transcition vertically with high contarst
init = 0
countH = 0
countW = 0

height = 256
width = 256
img = np.zeros((256,256), dtype = np.uint8)
singleRowFill = np.zeros((1,width), dtype = np.uint8)

for i in range(0, 1):
    for j in range(0,width):
        if countW == 16:
            init = init + 17
            singleRowFill[i,j] = init
            countW = 0
            countW = countW + 1
        else:
            singleRowFill[i,j] = init
            countW = countW +1
step = 0
for i in range(0,height):
    img[i,:] = singleRowFill[step,:]

    
cv2.imwrite('highContrastGrayTransectionVertical.bmp', img)

#%% Test pattern of  gray values transcition horizentally with high contarst
img = np.zeros((256,256), dtype = np.uint8)
singleRowFill = np.transpose(singleRowFill)
init = 0
countH = 0
countW = 0

height = 256
width = 256


step = 0
for i in range(0,height):
    img[:,i] = singleRowFill[:,step]

    
cv2.imwrite('highContrastGrayTransectionHorizental.bmp', img)



