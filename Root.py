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
import Integration

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
		self.X=[]
		self.Y=[]
		self.redlow=240
		self.redup=255
		self.greenlow=150
		self.greenup=255
		self.bluelow=235
		self.blueup=255

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
	
	def StopCapture(self):
		self.FlagValue=0 # makes the flag value to 0 to stop the capturing of frames
			
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
			a=(str(i[0]).split('['))[1].split(']')[0] #Extract the information between two square brackets
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
			self.X.append(int(temp[0]))
			self.Y.append(-int(temp[1]))	
		f.write(str(self.X)+'\n\n')
		f.write(str(self.Y)+'\n\n')
	
	def SetRGBValues(self):
		self.redlow=int(self.rlow.get())
		self.redup=int(self.rup.get())
		self.greenlow=int(self.glow.get())
		self.greenup=int(self.gup.get())
		self.bluelow=int(self.blow.get())
		self.blueup=int(self.bup.get())
		
	def Show3D(self):
		ScannedObject=Integrate.Integrate()
		ScannedObject.ReadFile('./'+self.FolderName)
		ScannedObject.Plot3D()
			
	def ShowFrame(self):
		try:
				del self.embed
		except:
				pass
		self.cap = cv2.VideoCapture(self.VideoDeviceNumber) #Video Device(webcam) is opened
		self.embed = tk.Frame(self.root, width=Root.w, height=Root.h)#a frame called 'embed' is created that hosts the pygame graphics
		self.embed.pack() #The frame is packed
		self.button=tk.Button(self.root, text="Start Capturing", command=self.Capture) #Button is created 
		self.button.pack() #Button is packed in left side
		self.button=tk.Button(self.root, text="Stop Capturing" , command=self.StopCapture) #Button is created 
		self.button.pack() #Button is packed in right side
		self.button=tk.Button(self.root, text="Show 3D" , command=self.Show3D) #Button is created 
		self.button.pack() #Button is packed in right side
		#variables to set the lower and the upper values of RGB are initialised
		self.rlow=tk.StringVar(self.root)
		self.rlow.set(230)
		self.entry_rlow=tk.Entry(self.root, textvariable=self.rlow)
		self.entry_rlow.pack()
		self.rup=tk.StringVar(self.root)
		self.rup.set(255)
		self.entry_rup=tk.Entry(self.root, textvariable=self.rup)
		self.entry_rup.pack()
		self.glow=tk.StringVar(self.root)
		self.glow.set(150)
		self.entry_glow=tk.Entry(self.root, textvariable=self.glow)
		self.entry_glow.pack()
		self.gup=tk.StringVar(self.root)
		self.gup.set(255)
		self.entry_gup=tk.Entry(self.root, textvariable=self.gup)
		self.entry_gup.pack()
		self.blow=tk.StringVar(self.root)
		self.blow.set(150)
		self.entry_blow=tk.Entry(self.root, textvariable=self.blow)
		self.entry_blow.pack()
		self.bhigh=tk.StringVar(self.root)
		self.bhigh.set(255)
		self.entry_bhigh=tk.Entry(self.root, textvariable=self.bhigh)
		self.entry_bhigh.pack()
		self.SetButton=tk.Button(self.root, text="Set RGB Values", command=self.SetRGBValues) #Button is created 
		self.SetButton.pack() #Button is packed in left side
		
		os.environ['SDL_WINDOWID'] = str(self.embed.winfo_id())# Tell pygame's SDL window which window ID to use
		self.root.update() #the window is updated
		pg.display.init()# Usual pygame initialization
		pg.display.set_mode((640,480), DOUBLEBUF|OPENGL|HWSURFACE|RESIZABLE) #refer to https://www.pygame.org/docs/ref/display.html
		while 1:
			_, self.frame = self.cap.read() #Read the video device input
			#self.frame = cv2.flip(self.frame, 1) #This should be uncommented to get the miiror image of the actual frame
			self.lower = np.array([self.bluelow,self.greenlow,self.redlow]) #lower limit of BGR values of the laser line
			self.upper= np.array([self.blueup,self.greenup,self.redup]) #upper limit of BGR values of the laser line
			self.mask = cv2.inRange(self.frame, self.lower, self.upper) #create a mask within the specified values of RED
			self.output_img = self.frame.copy() #a copy of the main frame is created
			self.output_img[np.where(self.mask==0)] = 0 #where the mask value is 0, make those coordinates black
			self.output_img[np.where(self.mask>100)] =255 #The target points, or the points which belong to the laser line are displayed in white
			#try an alternative with the Bitwise and in newer version
			self.gray = cv2.cvtColor(self.output_img, cv2.COLOR_BGR2GRAY)
			self.gray = cv2.GaussianBlur(self.gray, (5, 5), 0)
			self.thresh = cv2.threshold(self.gray, 45, 255, cv2.THRESH_BINARY)[1]
			self.thresh = cv2.erode(self.thresh, None, iterations=2)
			self.thresh = cv2.dilate(self.thresh, None, iterations=2)
			#The dilatation makes the object in white bigger.And the erosion makes the object in white smaller.
			#So overall no change after these two commands , check and see.
			
			#finding the contours with RED colour
			self.cnts = cv2.findContours(self.thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
			self.cnts = self.cnts[0] if imutils.is_cv2() else self.cnts[1]
			#self.c=self.cnts[0]
			for i in range(len(self.cnts)):
				self.c=self.cnts[i]
				cv2.drawContours(self.output_img, [self.c], -1, (0, 255, 255), 2) #Draw all the contours with a blue background
				if (self.FlagValue==1):
						self.plot()	
			self.im=ShowBmp(self.output_img) #process the output_img with OpenGL functions defined inside ShowBmp
			wall(self.im) #create the wall to be displayed in pygame
			pg.display.flip()# Update the pygame display
			
			if (self.FlagValue==1 and self.FrameCount<1024):
				ser=serial.Serial('/dev/'+self.Boards[self.BoardNumber-1], 9600) #open the serial port
				ser.write(b'1') #write serial data
				cv2.imwrite(str(self.FrameCount)+'.png',self.output_img) #save the .png image
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
