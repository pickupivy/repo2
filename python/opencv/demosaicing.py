
import numpy as np
import cv2 as cv

img = cv.imread("testraw.png")
height, width = img.shape[:2]
# tempB, tempG, tempR=img[1, 1]
# print(img[1, 1])
# print(tempB)
# print(tempG)
# print(tempR)

for row in range(1,481):
	for col in range(1,494):
		tempB, tempG, tempR=img[row, col]
		if tempG>tempB:
			if tempG>tempR:
				k=img[row,col-1]+img[row-1,col]+img[row+1,col]+img[row,col+1]
				img[row,col]=k/4
				img[row,col,1]=tempG
			else:
				blue=int(img[row-1,col-1,0])+int(img[row-1,col+1,0])+int(img[row+1,col-1,0])+int(img[row+1,col+1,0])
				img[row,col,0]=blue/4
				green=int(img[row,col-1,1])+int(img[row-1,col,1])+int(img[row+1,col,1])+int(img[row,col+1,1])
				img[row,col,1]=green/4
		else:
			if tempB>tempR:
				red=int(img[row-1,col-1,2])+int(img[row-1,col+1,2])+int(img[row+1,col-1,2])+int(img[row+1,col+1,2])
				img[row,col,2]=red/4
				green=int(img[row,col-1,1])+int(img[row-1,col,1])+int(img[row+1,col,1])+int(img[row,col+1,1])
				img[row,col,1]=green/4
			else:
				blue=int(img[row-1,col-1,0])+int(img[row-1,col+1,0])+int(img[row+1,col-1,0])+int(img[row+1,col+1,0])
				img[row,col,0]=blue/4
				green=int(img[row,col-1,1])+int(img[row-1,col,1])+int(img[row+1,col,1])+int(img[row,col+1,1])
				img[row,col,1]=green/4


cv.imshow('testWindow', img)
cv.imwrite("testraw0.png", img)

cv.waitKey(0)
cv.destroyAllWindows()
