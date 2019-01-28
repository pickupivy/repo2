
import cv2 as cv
import numpy as np

# Load two images
img1 = cv.imread('11.jpg')
img2 = cv.imread('opencv.jpg')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
#print(img2.shape)

#You can access a pixel value by its row and column coordinates. 
#For BGR image, it returns an array of Blue, Green, Red values.
# px = img[100,100]
# print( px )
# [157 166 200]

# # accessing only blue pixel
# blue = img[100,100,0]
# print( blue )
# 157

roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
#cv.imshow("img2gray", img2gray)
ret, mask = cv.threshold(img2gray, 200, 255, cv.THRESH_BINARY)	#开黑窗	#if >200 then =255; else =0;
#cv.imshow("mask", mask)
mask_inv = cv.bitwise_not(mask)		#开白窗
cv.imshow("mask_inv", mask_inv)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask)
cv.imshow("img1_bg", img1_bg)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask_inv)
cv.imshow("img2_fg", img2_fg)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv.imshow('res',img1)

cv.waitKey(0)
cv.destroyAllWindows()