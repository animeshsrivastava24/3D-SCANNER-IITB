'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''

import Tkinter as tk
import Main

#this is a function that opens a pop-up window
def About():
	PopupWindow=tk.Tk()
	PopupWindow.title("About")
	label1 =tk.Label(PopupWindow, text=Main.AboutText) #it will show the text defined in the variable Main.AboutText
	label1.pack()
