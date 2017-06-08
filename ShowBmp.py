'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''

#The necessary packages are imported
import pygame, OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy

def wall(image): #it creates the OpenGL texture that has to be displayed inside the pygame frame
	glColor((1,1,1))
	glBindTexture(GL_TEXTURE_2D,image) 
	glBegin(GL_QUADS)
	glTexCoord2f(0,0)
	glVertex3f(-4,-4,-8)
	glTexCoord2f(0,1)
	glVertex3f(-4,4,-8)
	glTexCoord2f(1,1)
	glVertex3f(4,4,-8)
	glTexCoord2f(1,0)
	glVertex3f(4,-4,-8)
	glEnd()

def ShowBmp(x):
	pixl_arr = numpy.swapaxes(x, 0, 1) #the x and the y axes are swapped to make it compatible with pygame
	new_surf = pygame.pixelcopy.make_surface(pixl_arr)
	textureData = pygame.image.tostring(new_surf, "RGB", 1)
	width = new_surf.get_width()
	height = new_surf.get_height()
	
	#OpenGL functions to process the image for the pygame wall
	im = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, im)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
	glEnable(GL_TEXTURE_2D)
	glLoadIdentity()
	gluPerspective(45, 1, 0.05, 100)
	glTranslatef(0,0,-5)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	return im #surface for the wall was returned

'''Part of the project 3D Scanner'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''
