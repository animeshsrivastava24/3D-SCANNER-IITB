import numpy as np
f=open("coord.ply","w+")
s=[]
for i in range(8):
	s.append("0")
X=[1,2,3,4]
Y=[5,3,9,6]
Z=[8,6,9,4]
s[0]="ply"
s[1]="format ascii 1.0"
s[2]="element vertex "+ str(len(X))
s[3]="property float32 x"
s[4]="property float32 y"
s[5]="property float32 z"
s[6]="element face 0"
s[7]="end_header"

#Copying the format of a .ply file into "coord.ply" file
for i in range(len(s)):
	f.write(s[i]+"\n")

#Creating a .ply file from the coordinates in the list X,Y,Z respectively	
for i in range(len(X)):
	f.write(str(X[i])+" ")
	f.write(str(Y[i])+" ")
	f.write(str(Z[i])+"\n")
	
