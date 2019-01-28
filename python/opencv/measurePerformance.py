
import numpy as np
import cv2 as cv

img1 = cv.imread('cut.png')
# e1 = cv.getTickCount()
# for i in range(5,49,2):
	# img1 = cv.medianBlur(img1,i)

# cv.imshow('img', img1)
# cv.waitKey(0)

# e2 = cv.getTickCount()
# t = (e2 - e1)/cv.getTickFrequency()
# print( t )

#cv.setUseOptimized(False)
flag=cv.useOptimized()
print(flag)

e1 = cv.getTickCount()
res=cv.medianBlur(img1, 49)
#print(res)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )


# 1.Avoid using loops in Python as far as possible, 
# especially double/triple loops etc. 
# They are inherently slow.

# 2.Vectorize the algorithm/code to the maximum possible extent 
# because Numpy and OpenCV are optimized for vector operations.

# 3.Exploit the cache coherence.

# 4.Never make copies of array unless it is needed. 
# Try to use views instead. Array copying is a costly operation.

