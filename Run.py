'''This code is a part of the 3D Scanner project'''
'''Developed by team SAAS'''
'''Ekalavya 2017'''
'''IIT Bombay'''


#The necessary packages are imported
import Main #local package
import threading #local package


th1=threading.Thread(target=Main.Main()) #Main() defined inside Main.py is called inside a thread
th1.start() #The thread is started

'''PS:
The Developers have used threading to start processes from the very beginning of the program.
This was done to enable execution of any other process parallely with the main process during any point of the runtime.'''


