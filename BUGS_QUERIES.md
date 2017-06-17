***Please don't clear any data of the file, we will maintain it as a 
Forum Database for someone in nearby future to understand our Code better***
__________________________________________________________________________________________________________________________________________
1).File Root.py 
*Line 56 and 57*
Why a new method called as
      def setDeviceNumber(self,x): #callback function to set the VideoDeviceNumber 
		  self.VideoDeviceNumber=x
 is used , we are using
     self.VideoDeviceNumber=x in the __init__ method.And thus if we want to change the value we can change it from there using self instance, please guide
Ans :     
