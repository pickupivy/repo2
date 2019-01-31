
import numpy as np
import cv2 as cv
from cvClass import *

#img=cv.imread('cut.png')
img=cv.imread('color.jpg')

#np.set_printoptions(suppress=True)
originCCM=np.mat([[332,-76,0],[-64,400,-80],[0,-172,428]])
temp=CCM(1,60,originCCM)
#temp.prtSome()
temp.adjPic(img)
cv.imshow('cut.png',img)

#img=cv.imread('33.png')
# prtImgPrpt(img)
# for pixel in img[0:4, 0:1]:
	# print(pixel)
#cv.namedWindow('window7')
#click=DrawClass('window7', img)
#prtImgPrpt(img)

# ball = img[380:440, 330:390]
# img[273:333, 100:160] = ball

# cv.imshow('ha', img)
# k=cv.waitKey(0)

# img1 = cv.imread('cut.png')
# prtImgPrpt(img1)
# img2 = cv.imread('cut2.png')
# prtImgPrpt(img2)
# dst = cv.addWeighted(img1,0.7,img2,0.3,0)
# cv.imshow('dst',dst)

# img=cv.imread("testraw.png")
# dst=shrink(img)
# cv.imshow("1", img)
# cv.imshow("2", dst)
#cv.imwrite("testraw0.png", img)
#videoAddr='rtsp://192.168.0.60:43794/profile1'
# videoAddr='bb.mkv'
# video1=VideoClass(videoAddr)
# video1.playVideo('RealCam')

# img1 = cv.imread('cut.png')
# img2 = cv.imread('cut2.png')
# cv.namedWindow('dstWd')
# bar1=TrackBarClass(img1,img2,'dstWd')

while(1):
	# #dst = cv.addWeighted(img1,t,img2,k,0)
	# #cv.imshow('dstWd',bar1.imgBlend())
	# #print("changed")
	# cv.imshow('window7', img)
	k = cv.waitKey(1)
	if k == 27:
		break



#cv.waitKey(0)
cv.destroyAllWindows()
