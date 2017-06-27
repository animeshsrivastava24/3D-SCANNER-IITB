'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''
'''This code is used to plot generate scatter plots from the txt files that the software makes'''
'''The code is written to capture a frame from camera input and then parse it and then find it's respective X,Y and Z co-ordinate 
points and plot it using matplotlib.pyplot as plt'''
#import the necessary modules
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
path=raw_input("enter path")
f=open(path,'r')
data=f.read()
f.close()

#extract the coordinates from the txt file
coordinates=data.split('\n\n')

coordinates[0]=coordinates[0][1:(len(coordinates[0])-1)]
coordinates[1]=coordinates[1][1:(len(coordinates[1])-1)]

X=coordinates[0].split(',')
Y=coordinates[1].split(',')
Z=[]

for i in range(len(X)):
	X[i]=long(int(X[i]))
	Y[i]=long(int(Y[i]))
	Z.append(0)
	
#make a scatter plot
surf=ax.scatter(X,Y,Z)
plt.show()
