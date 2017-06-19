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
		
	def ReadFile(self,folderpath):
		os.chdir(folderpath)
		for i in range(0,256): 
			f=open(str(i)+'.txt','r')
			data=f.read().split('\n\n')
			data[0]=data[0][1:(len(data[0])-1)]
			data[1]=data[1][1:(len(data[1])-1)]
			Xcoordinate=data[1].split(',')
			Ycoordinate=data[0].split(',')
			R=[] #this will contain the value of Radius for a single frame
			th=[] #this will contains the values of all the theta for a single frame
			for i in range(len(Xcoordinate)):
				R.append(math.sqrt(float(Xcoordinate[i])**2+float(Ycoordinate[i])**2))
				if float(Xcoordinate[i])==0:
					if float(Ycoordinate[i])>=0:
						th.append(3.14159/2)
					else:
						th.append(3*3.14159/2)
				else:
					th.append(np.arctan(float(Ycoordinate[i])/float(Xcoordinate[i])))	
			
			
			self.Radius.append(R) #append the values of the Radius in self.Radius
			self.theta.append(th) #append the values oh theta in self.theta
			#self.X.append(Xcoordinate)
			#self.Y.append(Ycoordinate)
		for k in range(256):
			self.phi.append((0.02454)*k)
			
		print self.phi
			
	def Plot3D(self):
		finalR=[]
		finaltheta=[]
		finalphi=[]
		for i in range(len(self.Radius)):
			for j in range(len(self.Radius[i])):
				finalR.append(float(self.Radius[i][j]))
				finaltheta.append(float(self.theta[i][j]))
				finalphi.append(float(self.phi[i]))
		#print finalphi
		#print self.phi
		X1=[]
		Y1=[]
		Z1=[]
		for i in range(len(finalR)):
			X1.append(finalR[i] * np.sin(finaltheta[i]) * np.cos(finalphi[i])) #final x coordinate of the point is calculated for plotting
			Y1.append(finalR[i] * np.sin(finaltheta[i]) * np.sin(finalphi[i])) #final y coordinate of the point for plotting
			Z1.append(finalR[i] * np.cos(finaltheta[i])) #final z coordinate of the point for plotting
		
		
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		SavePLY.SavePLY(X1,Y1,Z1)
		ax.scatter(X1, Y1, Z1)
		plt.show()
		

'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''

		
