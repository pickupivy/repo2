
import numpy as np
import cv2 as cv

img = cv.imread("testraw.png")

#print(img.shape)
#print(len(img[0,0]))

# px = img[100,100]
# print( px )


# k=img[1,1]+img[2,2]
# a=k/2
# print(img[1,1])
# print(img[2,2])
# print(k)
# print(a)
for row in range(2,480):
	for col in range(2,493):
		# k=img[row-1,col-1]+img[row-1,col+1]+img[row+1,col-1]+img[row+1,col+1]
		# img[row,col]=k/4
		blue=int(img[row,col-2,0])+int(img[row-2,col,0])+int(img[row+2,col,0])+int(img[row,col+2,0])
		img[row,col,0]=blue/4
		green=int(img[row,col-2,1])+int(img[row-2,col,1])+int(img[row+2,col,1])+int(img[row,col+2,1])
		img[row,col,1]=green/4
		red=int(img[row,col-2,2])+int(img[row-2,col,2])+int(img[row+2,col,2])+int(img[row,col+2,2])
		img[row,col,2]=red/4


# cv.imshow('testWindow1',shrink_NEAREST)
# cv.imshow('testWindow2',shrink_LINEAR)
# cv.imshow('testWindow3',shrink_AREA)
# cv.imshow('testWindow4',shrink_CUBIC)
# cv.imshow('testWindow5',shrink_LANCZOS4)

cv.imshow('testWindow', img)
#cv.imwrite("testraw000.png", img)

cv.waitKey(0)
cv.destroyAllWindows()
