
import numpy as np
import cv2 as cv

class VideoClass():
	
	def __init__(self, videoAddr):
		self.videoAddr=videoAddr
		self.cap = cv.VideoCapture(videoAddr)
		# = cv.VideoCapture(0)	#视频源代号，这里的0应该是电脑自带的摄像头
		# = cv.VideoCapture('../bb.mkv')		#这里的路径为斜杠/而不是反斜杠
		# = cv.VideoCapture('e:/File Repository/bb.mkv')		#可以正确识别路径中的空格
		# = cv.VideoCapture('rtsp://192.168.0.60:43794/profile1')
		self.isFlip=False
		self.isRecording=False	#标志位isRecording必须是逐帧判断的，或者是每N帧判断一次，因为无法预知用户何时打开或关闭录制功能
		self.fourcc = cv.VideoWriter_fourcc(*'XVID')
		self.size=self.videoSize()
		self.out = cv.VideoWriter('output.avi',self.fourcc, 20.0, self.size)
		
	def releaseAll(self):	#释放空间
		self.cap.release()
		self.out.release()
		
	def videoSize(self):
		ret, frame = self.cap.read()
		height, width = frame.shape[:2]
		size=(int(width), int(height))
		print(size)
		return size
		
	def keyBind(self, k):	#键盘事件的响应函数
		if k == ord('r'):
			self.isRecording= not self.isRecording
			if self.isRecording:
				print("Recording on!")
			else:
				print("Recording off!")
		elif k == ord('f'):
			self.isFlip= not self.isFlip
		
	def playVideo(self, winName='window'):
		cv.namedWindow(winName, cv.WINDOW_AUTOSIZE)	#cv.WINDOW_NORMAL-->you can resize window
		#By default, the flag is cv.WINDOW_AUTOSIZE.
		while(self.cap.isOpened()):
			# Capture frame-by-frame
			ret, frame = self.cap.read()
			#第一个参数ret的值为True或False，False代表有没有读到图片
			#第二个参数是frame，是当前截取一帧的图片。
			#read()函数返回两个参数，所以才这么写。
			if ret == True:		#不加判断可能会报错，例如：error: (-215:Assertion failed)
				if self.isFlip == True:
					#write the flipped frame
					frame = cv.flip(frame,1)
					# 0 means vertical flipping; 1 means horizontal mirror; -1 means both vertical and horizontal flip
				#frame = cv.resize(frame, (640,480), interpolation=cv.INTER_NEAREST)
				cv.imshow(winName, frame)
				#也可以灰白模式播放
				#grayF = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
				#cv.imshow(winName, grayF)
				if self.isRecording == True:	#当flag打开时，才进行录像操作
					self.out.write(frame)	#保存视频
			else:
				self.cap.release()	#释放空间
				self.out.release()
				break
			k=cv.waitKey(5)
			if k == ord('q'):
				break
			else:
				self.keyBind(k)



