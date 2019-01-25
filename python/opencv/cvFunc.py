
import numpy as np
import cv2 as cv

def shrink(image,w_rate,h_rate,skMode=0):
	height, width = image.shape[:2]
	#print(image.shape[:2])
	size = (int(width*0.5), int(height*0.5))
	shrink_NEAREST = cv.resize(image, size, interpolation=cv.INTER_NEAREST)
	return shrink_NEAREST
# shrink_LINEAR = cv.resize(image, size, interpolation=cv.INTER_LINEAR)
# shrink_AREA = cv.resize(image, size, interpolation=cv.INTER_AREA)
# shrink_CUBIC = cv.resize(image, size, interpolation=cv.INTER_CUBIC)
# shrink_LANCZOS4 = cv.resize(image, size, interpolation=cv.INTER_LANCZOS4)

def prtImgPrpt(image):
	print(image.shape)
	print(image.size)
	print(image.dtype)

#变量videoAddr为视频源的地址
def playVideo(videoAddr):
	cap = cv.VideoCapture(videoAddr)
	#cap = cv.VideoCapture(0)	#视频源代号，这里的0应该是电脑自带的摄像头
	#cap = cv.VideoCapture('../bb.mkv')		#这里的路径为斜杠/而不是反斜杠
	#cap = cv.VideoCapture('e:/File Repository/bb.mkv')		#可以正确识别路径中的空格
	#cap = cv.VideoCapture('rtsp://192.168.0.60:43794/profile1')
	#count=0
	cv.namedWindow('window', cv.WINDOW_NORMAL)	#you can resize window
	#By default, the flag is cv.WINDOW_AUTOSIZE.
	while(cap.isOpened()):
		# Capture frame-by-frame
		ret, frame = cap.read()
		#第一个参数ret的值为True或False，False代表有没有读到图片
		#第二个参数是frame，是当前截取一帧的图片。
		#read()函数返回两个参数，所以才这么写。
		if ret == True:
			cv.imshow('window', frame)
			#也可以灰白模式播放
			#grayF = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
			#cv.imshow('window', grayF)
		else:
			cap.release()	#窗口释放
			#cv.waitKey(0)
			#count=count+1
			#print(str(count)+"\n")
			break
		#count=count+1
		#if count >= 300:
			#break
		if cv.waitKey(5) == ord('q'):
			break

def saveVideo(videoAddr):
	cap = cv.VideoCapture(videoAddr)
	#cap = cv.VideoCapture(0)	#视频源代号，这里的0应该是电脑自带的摄像头
	#cap = cv.VideoCapture('../bb.mkv')		#这里的路径为斜杠/而不是反斜杠
	#cap = cv.VideoCapture('e:/File Repository/bb.mkv')		#可以正确识别路径中的空格
	#cap = cv.VideoCapture('rtsp://192.168.0.60:43794/profile1')
	# Define the codec and create VideoWriter object
	fourcc = cv.VideoWriter_fourcc(*'XVID')
	#FourCC code is passed as cv.VideoWriter_fourcc('M','J','P','G')or cv.VideoWriter_fourcc(*'MJPG') for MJPG.
	out = cv.VideoWriter('output.avi',fourcc, 20.0, (640,480))
	#VideoWriter (const String &filename, int fourcc, double fps, Size frameSize, bool isColor=true)
	while(cap.isOpened()):
		ret, frame = cap.read()
		#第一个参数ret的值为True或False，False代表有没有读到图片
		#第二个参数是frame，是当前截取一帧的图片。
		#read()函数返回两个参数，所以才这么写。
		if ret==True:
			#frame = cv.flip(frame,0)
			# write the flipped frame
			out.write(frame)	#保存视频
			cv.imshow('window',frame)
			if cv.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			break
	# Release everything if job is finished
	cap.release()
	out.release()


