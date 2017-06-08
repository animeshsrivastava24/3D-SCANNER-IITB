'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''

#The necessary packages are imported

#Downloaded packages
import pygame as pg
from pygame.locals import *
import numpy as np
import cv2
import Image, ImageTk
import imutils
import matplotlib.pyplot as plt

#local packages
from About import *
from ShowBmp import *
import ValueSelected

#python inbuilt packages
import Tkinter as tk
import os
import time
import serial
import threading
from time import gmtime, strftime


class Root(): #A class called Root is defined
	
	w,h=800,600 #local variables w(width) and h(height) are specified
	
	def __init__(self,x,y,z,a,n): #constructor of the class
		#values are assigned to the instance variables
		self.VideoDeviceNumber=x
		self.Names=y
		self.Dict=z
		self.Boards=a
		self.BoardNumber=n
		self.root = tk.Tk()
		self.FlagValue=0
		self.FrameCount=0

	def setDeviceNumber(self,x): #callback function to set the VideoDeviceNumber 
		self.VideoDeviceNumber=x
		
	def func(self): #callback function when 'Settings' is selected
		self.cap.release() #camera is made inactive
		obj=ValueSelected.ComboBox(self.Names,self.Dict,self.Boards) #a combobox object is created 
		obj.CreateComboBox()#combobox is created
		self.VideoDeviceNumber = obj.d #VideoDeviceNumber is assigned
		self.BoardNumber = obj.b #Arduino's BoardNumber is assigned
		print "Opening Device Number:", self.VideoDeviceNumber #Prints a message about the selection of the camera by the user
		self.CreateMainWindow() #The mainwindow is created again
	
	def Capture(self): #callback function to start the rotation of the stepper motor and save the .png files and coordinates in .txt files
		
		self.FlagValue=1 #FlagValue is a flag that is turned 0 to stop the stepper and the saving of images and 1 to start
		self.FrameCount=0 #It is a counter variable used to count the number of frames captured
		self.FolderName=strftime("%Y-%m-%d %H:%M:%S", gmtime()) #string to store the folder name "<CurrentDate CurrentTime>"
		os.mkdir('./'+self.FolderName) #creates a folder in the local directory
		os.chdir('./'+self.FolderName) #changes the directory to the created directory

		
	def thread2(self):
		self.th2=threading.Thread(target=self.Capture) #a thread is initiated to call the self.Capture() function
		self.th2.start() #the thread is started
	
	def plot(self):
		#some local variables are created
		X=[]
		Y=[]
		temp1=[]
		temp=[]
		towrite=[]
		#the under written functions are for extracting the coordinates from numpy.ndarray datatype
		for i in range(len(self.c)):
			temp1.append(self.c[i][0])
		for i in range(len(temp1)):
			temp.append(str(temp1[i]).split(','))
		for i in temp:
			a=(str(i[0]).split('['))[1].split(']')[0]
			towrite.append(a)
		
		#A file is opened to write the coordinates of the contour
		f=open(str(self.FrameCount)+".txt", 'w') 
		for i in towrite:
			i=str(i)
			i=i.strip()
			i=i.replace('   ',' ')
			i=i.replace('  ', ' ')
			i=i.strip()
			temp=i.split(' ')
			X.append(int(temp[0]))
			Y.append(-int(temp[1]))	
		f.write(str(X)+'\n\n')
		f.write(str(Y)+'\n\n')
		
			
			
	def ShowFrame(self):
		try:
				del self.embed
		except:
				pass
		self.cap = cv2.VideoCapture(self.VideoDeviceNumber) #Video Device(webcam) is opened
		self.embed = tk.Frame(self.root, width=Root.w, height=Root.h)#a frame called 'embed' is created that hosts the pygame graphics
		self.embed.pack() #The frame is packed
		self.button=tk.Button(self.root, text="Start Capturing", command=self.Capture) #Button is created 
		self.button.pack() #Button is packed
		os.environ['SDL_WINDOWID'] = str(self.embed.winfo_id())# Tell pygame's SDL window which window ID to use
		self.root.update() #the window is updated
		pg.display.init()# Usual pygame initialization
		pg.display.set_mode((640,480), DOUBLEBUF|OPENGL|HWSURFACE|RESIZABLE) #refer to https://www.pygame.org/docs/ref/display.html
		while 1:
				_, self.frame = self.cap.read() #Read the video device input
				#self.frame = cv2.flip(self.frame, 1) #This should be uncommented to get the miiror image of the actual frame
				self.img_hsv=cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV) #change the format of the image from BGR to HSV
				self.lower_red = np.array([0,50,50]) #lower limit of "RED" in lower range of Hue in HSV format
				self.upper_red = np.array([10,255,255]) #upper limit of "RED" in lower range of Hue in HSV format
				self.mask0 = cv2.inRange(self.img_hsv, self.lower_red, self.upper_red) #create a mask within the specified values of RED
				self.lower_red = np.array([170,50,50]) #lower limit of "RED" in upper range of Hue in HSV format
				self.upper_red = np.array([180,255,255]) #upper limit of "RED" in upper range of Hue in HSV format
				self.mask1 = cv2.inRange(self.img_hsv, self.lower_red, self.upper_red) #create a mask within the specified values of RED
				self.mask = self.mask0+self.mask1 #both the masks are added and a new mask is created
				self.output_img = self.frame.copy() #a copy of the main frame is created
				self.output_img[np.where(self.mask==0)] = 0 #where the mask value is 0, make those coordinates black
				self.output_img[np.where(self.mask>100)] =255 #The target points, or the points which are RED in colour are displayed in white
				
				self.gray = cv2.cvtColor(self.output_img, cv2.COLOR_BGR2GRAY)
				self.gray = cv2.GaussianBlur(self.gray, (5, 5), 0)
				self.thresh = cv2.threshold(self.gray, 45, 255, cv2.THRESH_BINARY)[1]
				self.thresh = cv2.erode(self.thresh, None, iterations=2)
				self.thresh = cv2.dilate(self.thresh, None, iterations=2)
				
				#finding the contours with RED colour
				self.cnts = cv2.findContours(self.thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
				self.cnts = self.cnts[0] if imutils.is_cv2() else self.cnts[1]
				
				for i in range(len(self.cnts)):
					self.c=self.cnts[i]
					cv2.drawContours(self.output_img, [self.c], -1, (0, 255, 255), 2) #Draw all the contours with a blue background
						
				self.im=ShowBmp(self.output_img) #process the output_img with OpenGL functions defined inside ShowBmp
				wall(self.im) #create the wall to be displayed in pygame
				pg.display.flip()# Update the pygame display
				
				if (self.FlagValue==1 and self.FrameCount<1024):
					ser=serial.Serial('/dev/'+self.Boards[self.BoardNumber-1], 9600) #open the serial port
					ser.write(b'1') #write serial data
					cv2.imwrite(str(self.FrameCount)+'.png',self.output_img) #save the .png image
					self.plot()
					time.sleep(0.01) #pause the code for 10ms
					self.FrameCount+=1 #increase the frame counter
				
				elif (self.FlagValue==1 and self.FrameCount==1023): 
					self.FlagCount=0
					self.FrameCount=0
				self.root.update()# Update the Tk display
	
	def CreateMainWindow(self):
		self.root.wm_title("Webcam Interface") #assign title to the root window
		menubar = tk.Menu(self.root) #Menubar widget is created
		filemenu = tk.Menu(menubar, tearoff=0) #Filemenu is created
		filemenu.add_command(label="Exit", command=self.root.destroy)
		menubar.add_cascade(label="File", menu=filemenu)
		editmenu = tk.Menu(menubar, tearoff=0)
		menubar.add_cascade(label="Edit", menu=editmenu)
		self.VideoDeviceName=tk.StringVar()		
		editmenu.add_radiobutton(label="Settings", command=self.func)
		helpmenu = tk.Menu(menubar, tearoff=0)
		helpmenu.add_command(label="About", command=About)
		menubar.add_cascade(label="Help", menu=helpmenu)
		self.root.config(menu=menubar)#menubar is packed in the frame
		self.ShowFrame()

'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''		
