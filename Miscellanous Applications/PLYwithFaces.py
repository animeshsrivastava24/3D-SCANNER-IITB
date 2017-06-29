'''Plot the point cloud from any .ply file with ASCII encoding using matplotlib and mplot3d'''
'''Team SAAS, Ekalavya 2017, IIT Bombay'''


#import the necessary packages
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator
import numpy as np
import matplotlib.tri as mtri
from scipy.spatial import Delaunay

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
path=raw_input("Enter the path of the file\n") #path for opening the file is asked to the user

X=[]
Y=[]
Z=[]
StartIndex=0

f=open(path,'r')
lines=f.readlines()
f.close()

#coordinates of the point cloud vertices are extracted from the file
for i in lines:
	temp=i.split(' ')
	if (temp[0]=='element'):
		if (temp[1]=='vertex'):
			vertices=long(int(temp[2]))
		if (temp[1]=='face'):
			face=long(int(temp[2]))
print "The given file has %d number of vertices and %d number of faces" %(vertices,face)

coordinates=[]

for i in range(len(lines)):
	temp=lines[i]
	if (temp=='end_header\n'):
		StartIndex=i+1
		break

for i in range(StartIndex,(StartIndex+vertices)):
			coordinates.append(lines[i])

#the coordinates are appended in the list X, Y, Z
for i in coordinates:
	point=i.split(' ')
	X.append(float(point[0]))
	Y.append(float(point[1]))
	Z.append(float(point[2]))

#a scatter plot is created
surf = ax.scatter(X, Y, Z, zdir='y') 

#a window is created showing the scatter plot
#plt.show()


f=open("coord.ply","w+")
s=[]
for i in range(9):
	s.append("0")
'''X=[1,2,3,4]
Y=[5,3,9,6]
Z=[8,6,9,4]
'''

u=np.array(X)
v=np.array(Y)
z=np.array(Z)
tri = Delaunay(np.array([u,v]).T)
num=len(tri.simplices)
s[0]="ply"
s[1]="format ascii 1.0"
s[2]="element vertex "+ str(len(X))
s[3]="property float32 x"
s[4]="property float32 y"
s[5]="property float32 z"
s[6]="element face "+str(num)
s[7]="property list uint8 int32 vertex_indices"
s[8]="end_header"
for i in range(len(s)):
	f.write(s[i]+"\n")
for i in range(len(X)):
	f.write(str(X[i])+" ")
	f.write(str(Y[i])+" ")
	f.write(str(Z[i])+"\n")

for vert in tri.simplices:
    f.write("3 "+str(vert[0])+" ")
    f.write(str(vert[1])+" ")
    f.write(str(vert[2])+"\n")
"""
Link update : https://github.com/animeshsrivastava24/3D-SCANNER-IITB/wiki/VI-b)-.-Analysis-of-PLY-file-with-Faces
GO to the link for detailed info"""
