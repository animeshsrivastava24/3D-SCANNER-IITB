<p align="center">
  <img width="100" height="98" src="http://www.iitb.ac.in/sites/all/themes/touchm/logo.png">
</p>

# ABOUT:
This a project of FOSSEE, IIT Bombay funded by MHRD, GoI under the guidance of Prof.D B Phatak(Patron), Mr.Rajesh Kushalkar(Project Manager, IDL, IIT Bombay) and Mr. Akshay Chipkar(Project Mentor).
The project aims at developing open source hardware and software for 3D scanning of objects.
The code for this project were written and tested on Ubuntu 14.04.5 with python as the primary programming language.

# DESCRIPTION:
The project was undertaken by four interns during the Summer of 2017 under the Ekalavya Summer Internship sponsored by the MHRD,India at Integrated Development Lab, Department of Computer Science and Engineering, IIT Bombay.
  ##  1. [Sagar Satapathy, NIT Rourkela](https://github.com/sagarbaba)
  ##  2. [Animesh Srivastava, NIT Hamirpur](https://github.com/animeshsrivastava24)
  ##  3. [Anchal Singh Panwar, NIT Uttarakhand](https://github.com/Anchalpanwar)
  ##  4. [Soumya Sambit Rath, NIT Rourkela](https://github.com/ss-rath)
  
  
# CONTENTS:
  ## 1.Hardware Used:
  ### 1.1 Arduino UNO:          
      Microcontroller-ATmega328
      Operating Voltage- 5V
      Input Voltage (recommended)- 7-12V
      Input Voltage (limits)- 6-20V
      Digital I/O Pins- 14 (of which 6 provide PWM output)
      Analog Input Pins- 6
      DC Current per I/O Pin- 40 mA
      DC Current for 3.3V Pin- 50 mA
      Flash Memory- 32 KB of which 0.5 KB used by bootloader
      SRAM- 2 KB (ATmega328)
      EEPROM- 1 KB (ATmega328)
      Clock Speed- 16 MHz

  ### 1.2 Laser Module(INT 2549):
      Output Power:
      Min:2.5mW  
      Typical:3.0mW 
      Max:5.0mW
      Working current:
      Min:10mA
      Typical:20mA
      Max:25mA
      Working voltage:
      Min:2.3V
      Typical:4.5V
      Max:8.0V
      Wavelength:
        650nm
      Focused Dot Width:
        < 2mm spotting 3 meters away
    
  ### 1.3 Stepper Motor(28BYJ-48):
      Rated voltage ： 5V DC
      Number of Phase ： 4
      Speed Variation Ratio ： 1/64
      Stride Angle ： 5.625° /64
      Frequency : 100Hz
      DC resistance ： 200Ω±7%(25℃)
      Idle In-traction Frequency : >600Hz
      Idle Out-traction Frequency : >1000Hz
      In-traction Torque : >34.3mN.m(120Hz)
      Self-positioning Torque : >34.3mN.m
      Friction torque : 800-1800 gf.cm
      Pull in torque  : 450 gf.cm
      Insulated resistance : >10MΩ(500V)
  
  ### 1.4 Current Amplifier IC(ULN2003)
  [ULN2003 Datasheet](http://www.seeedstudio.com/document/pdf/ULN2003%20Datasheet.pdf)

  ## 2.Open Source Technologies Used:
  
  ### 2.1 Python 2.7
      Python was chosen as the default language for writing all the programs throughout the project. The version used by the developers was 2.7.6
      
  ### 2.2 PyOpenGL 
      PyOpenGL is the most common cross platform Python binding to OpenGL and related APIs. The binding is created using the standard ctypes library, and is provided under an extremely liberal BSD-style Open-Source license.
      Src: http://pyopengl.sourceforge.net/
      
  ### 2.3 OpenCV 3.2.0
      OpenCV (Open Source Computer Vision Library) is released under a BSD license and hence it’s free for both academic     and commercial use. Written in optimized C/C++, the library can take advantage of multi-core processing.
      Src: http://opencv.org/
 
  ### 2.4 Numpy 
      NumPy is the fundamental package for scientific computing with Python.Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.NumPy is licensed under the BSD license, enabling reuse with few restrictions.
      Src: http://www.numpy.org/
      
  ### 2.5 Matplotlib
      Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.
      Src: https://matplotlib.org/
      
  ### 2.6 Pygame 
      Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.
      It was used in the project for rendering the graphics in the display window.
      Src: https://www.pygame.org/news
      
  ### 2.7 Tkinter
      Tkinter is Python's de-facto standard GUI (Graphical User Interface) package.It was used for creating the windows and the widgets.
      Src: https://wiki.python.org/moin/TkInter
      
  ### 2.8 Python Imaging Library
      The Python Imaging Library (PIL) adds image processing capabilities to your Python interpreter. This library supports many file formats, and provides powerful image processing and graphics capabilities. the version that was used is 1.1.7
      Src: http://www.pythonware.com/products/pil/
      
  ### 2.9 Pyserial 
      Python Serial Port Extension package
      Since a MicroController was used, this package was used for serial communications.
      Src: https://pypi.python.org/pypi/pyserial
  
  ## 3. INSTALLATION:
      Download the installscript.sh file and execute it.
  ```
    $cd "< path of the file >"
    $bash installscript.sh
  ```

  ## 4. USAGE: 
   ### 4.1 Manufacturing:
       Die & Mould Design or Modification
       Raw Casting / Forging Inspection
       Positioning Fixtures
   ### 4.2 Automotive:
       Production Compliance Inspection
       Tool Testing and Adjustment
       Wear and Deforming monitor
   ### 4.3 Archaelogy:
       Study of Ancient remains, antiques and allied findings
       Cloning the antiques for further experimental studies
   ### 4.4 Educational:
       Innovative 3D methods to optimize research related to Image Processing and Computer Vision
       Advanced 3D rendering studies 
       Virtual Reality, 3D Graphics, Digital Preservation
   ### 4.5 Medical:
       Designing Remoulding Shoes
       Obtaining models of deformed body parts for further research and analysis
  


# CREDITS
    The developers credit their entire project to their mentor Mr. Akshay Chipkar and their program head Prof D. B. Phatak.
    The developer's team is also grateful to the Integrated Development Lab, KReSIT, IIT Bombay for providing them an opportunity to work on this project.
    

Copyright (c) 2017 Team SAAS
