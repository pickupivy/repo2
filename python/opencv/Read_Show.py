import cv2
import numpy
 
img = cv2.imread("11.jpg",0)	# Load an color image in grayscale
cv2.namedWindow('hey', cv2.WINDOW_NORMAL)	#you can resize window
#cv2.namedWindow('hey', cv2.WINDOW_AUTOSIZE)

cv2.imshow("hey",img)	#"hey" is the window name; 
#if the window is not exist, then it will be created

k=cv2.waitKey(0)
#单位ms, 0表示永久

if k==27:
	cv2.destroyAllWindows()
elif k==ord('s'):
	cv2.imwrite("11.png", img)

#将img图像另存为11.png