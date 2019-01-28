
import numpy as np
import cv2 as cv
#from matplotlib import pyplot as plt
img = cv.imread('testraw.png')
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
blur = cv.GaussianBlur(img,(5,5),0)
median = cv.medianBlur(img,5)

cv.imshow("filter2D",dst)
cv.imshow("GaussianBlur",blur)
cv.imshow("medianBlur",median)
#cv.imwrite("testraw000.png", dst)

cv.waitKey(0)
cv.destroyAllWindows()