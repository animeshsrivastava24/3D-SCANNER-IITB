'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''

#import the necessary packages
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from matplotlib import cm
from matplotlib import pyplot as plt
import os
import SavePLY

class Integration(): #a class is defined
	
	def __init__(self):
		self.X=[] #this will contain the x coordinates of all the frames
		self.Y=[] #this will contain the y coordinates of all the frames
		self.Radius=[] #This will contain value of all the Rs
		self.theta=[] #This will contain all the values of theta
		self.phi=[] #This will contain the phi values of all the points
		self.X1=[]
		self.Y1=[]
		self.Z1=[]
		
	def ReadFile(self,folderpath):
		os.chdir(folderpath)
		for i in range(0,48): 
			f=open(str(i)+'.txt','r')
			data=f.read().split('\n\n')
			data[0]=data[0][1:(len(data[0])-1)]
			data[1]=data[1][1:(len(data[1])-1)]
			Xcoordinate=data[1].split(',')
			Ycoordinate=data[0].split(',')
			R=[] #this will contain the value of Radius for a single frame
			th=[] #this will contains the values of all the theta for a single frame
			for i in range(len(Xcoordinate)):
				R.append(math.sqrt(float(Xcoordinate[i])**2+float(Ycoordinate[i])**2)) # formula for calculating the value or R
				if float(Xcoordinate[i])==0:
					if float(Ycoordinate[i])>=0:
						th.append(3.14159/2) #when the Ycoordinate of the 2D frame is +ve, then X coordinate is pi/2
					else:
						th.append(3*3.14159/2) #when the Ycoordinate of the 2d frame is -ve, then X coordinate is 3*pi/2
				else:
					th.append(np.arctan(float(Ycoordinate[i])/float(Xcoordinate[i]))) #formula for calculation of theta	
			
			
			self.Radius.append(R) #append the values of the Radius in self.Radius
			self.theta.append(th) #append the values oh theta in self.theta
			
		for k in range(48):
			self.phi.append((0.1308)*k) #formula for appending the value of phi in the value of the coordinates of a particular frame
			
		print self.phi
			
	def CalculateXYZ(self): #function for calculation of X,Y,Z from R,theta,phi
		finalR=[]
		finaltheta=[]
		finalphi=[]
		for i in range(len(self.Radius)):
			for j in range(len(self.Radius[i])):
				finalR.append(float(self.Radius[i][j]))
				finaltheta.append(float(self.theta[i][j]))
				finalphi.append(float(self.phi[i]))
		
		
		for i in range(len(finalR)):
			self.X1.append(finalR[i] * np.sin(finaltheta[i]) * np.cos(finalphi[i])) #final x coordinate of the point is calculated for plotting
			self.Y1.append(finalR[i] * np.sin(finaltheta[i]) * np.sin(finalphi[i])) #final y coordinate of the point for plotting
			self.Z1.append(finalR[i] * np.cos(finaltheta[i])) #final z coordinate of the point for plotting
		
		SavePLY.SavePLY(self.X1,self.Y1,self.Z1)
		
	def PlotTrisurf(self):	#function for plotting the Surface Plot
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.plot_trisurf(self.X1, self.Y1, self.Z1)
		plt.show()
	
	def PlotScatter(self):	#function for plotting the Scatter Plot
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.scatter(self.X1, self.Y1, self.Z1)
		plt.show()
		

'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''
'''Click here https://github.com/animeshsrivastava24/3D-SCANNER-IITB/wiki/8.0-How-to-plot-the-points-to-generate-3D-cloud-point-taking-help-of-SavePLY-file-(Analysis-of-Code-of-Integration.ply)
   to understand the above code'''

		
