
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
		# ret, frame = self.cap.read()
		# height, width = frame.shape[:2]
		if self.cap.isOpened():
			width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
			height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
		else:
			print("Video is not opened!")
		size=(int(width), int(height))
		#print(size)
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
		
	def playVideo(self, winName='window'):		#隐藏参数：播放窗口名	#附加功能：保存播放的视频
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

class DrawClass():
	
	def __init__(self, winName, imgName, isCircle):
		self.winName=winName
		self.imgName=imgName
		self.drawing=False	# true if mouse is pressed
		self.isCircle=isCircle	#if True, draw circle; else, draw rectangle
		self.ix=-1
		self.iy=-1
		self.setCalBckFunc()
		#self.print_opencv_events()
	
	# mouse callback function
	def drawCircle(self,event,x,y,flags,param):
		if event == cv.EVENT_LBUTTONDBLCLK:
			cv.circle(self.imgName,(x,y),10,(255,0,0),-1)
	
	# mouse callback function	
	def drawCircle2(self,event,x,y,flags,param):
		if event == cv.EVENT_LBUTTONDOWN:
			self.drawing = True
			self.ix,self.iy = x,y
		elif event == cv.EVENT_MOUSEMOVE:
			if self.drawing == True:
				if self.isCircle == True:
					cv.circle(self.imgName,(x,y),5,(0,0,255),-1)	#BGR		
				else:
					cv.rectangle(self.imgName,(self.ix,self.iy),(x,y),(0,255,0),1)	#BGR
		elif event == cv.EVENT_LBUTTONUP:
			self.drawing = False
			if self.isCircle == True:
				cv.circle(self.imgName,(x,y),5,(0,0,255),-1)	#BGR	
			else:
				cv.rectangle(self.imgName,(self.ix,self.iy),(x,y),(0,255,0),1)	#BGR
	
	def setCalBckFunc(self):	
		cv.setMouseCallback(self.winName,self.drawCircle2)
		#(Name of the window, Callback function for mouse events)
		
	def print_opencv_events(self):
		events = [i for i in dir(cv) if 'EVENT' in i]
		for item in events:
			print( item )
	
	def otherfunc(self):
		# Draw a diagonal blue line with thickness of 5 px
		cv.line(img,(0,0),(511,511),(255,0,0),1)
		cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
		#cv.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
		cv.circle(img,(447,63), 63, (0,0,255), -1)
		#cv.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
		cv.ellipse(img,(256,256),(100,50),0,0,180,(0,256,0),-1)
		#cv.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]	)
		pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
		#pts = pts.reshape((-1,1,2))
		cv.polylines(img,[pts],True,(0,255,255))
		font = cv.FONT_HERSHEY_SIMPLEX
		#cv.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]	)
		cv.putText(img,'OpenCV',(10,500), font, 2,(255,255,255),5,cv.LINE_AA)

# class Something():
	# def __init__(self):
		
	# def statements(self):
		# img = np.zeros((512,512,3), np.uint8)

class TrackBarClass():
	
	def __init__(self,img1,img2,winName,barName='ratio'):
		self.img1=img1
		self.img2=img2
		self.winName=winName
		self.barName=barName
		self.dst = cv.addWeighted(self.img1,0.1,self.img2,0.9,0)	#初始化值
		cv.createTrackbar(self.barName,self.winName,0,100,self.slideBar)
		#cv::createTrackbar(trackbarname,winname,start value,max value,callbackfunc)
		
	def slideBar(self,x):
		t=x/100.0
		print(x, t, 1-t)
		self.dst[:] = cv.addWeighted(self.img1,t,self.img2,1-t,0)	#切片法修改数组
		
	def imgBlend(self):
		return self.dst
		
	def getPos(self):
		cv.getTrackbarPos(self.barName,self.winName)


