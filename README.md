<p align="center">
  <img width="100" height="98" src="http://www.iitb.ac.in/sites/all/themes/touchm/logo.png">
</p>

# ABOUT:
This a project of FOSSEE, IIT Bombay funded by MHRD, GoI under the guidance of Prof.D B Phatak(Patron),Rajesh Kushalkar(Project Manager, IDL, IIT Bombay) and Akshay Chipkar(Project Mentor).
The project aims at developing open source hardware and software for 3D scanning of objects.
# 3D SCANNER
A **[3D Scanner](https://en.wikipedia.org/wiki/3D_scanner)** is a device that analyses a real-world object or environment to collect data on its shape and possibly its appearance (e.g. colour). The collected data can then be used to construct digital three-dimensional models.

Many different technologies can be used to build these 3D-scanning devices; each technology comes with its own limitations, advantages and costs. Many limitations in the kind of objects that can be digitised are still present, for example, optical technologies encounter many difficulties with shiny, mirroring or transparent objects. For example, industrial computed tomography scanning can be used to construct digital 3D models, applying non-destructive testing.

Collected 3D data is useful for a wide variety of applications. These devices are used extensively by the entertainment industry in the production of movies and video games. Other common applications of this technology include industrial design, orthotics and prosthetics, reverse engineering and prototyping, quality control/inspection and documentation of cultural artifacts.
The purpose of a 3D scanner is usually to create a point cloud of geometric samples on the surface of the subject. These points can then be used to extrapolate the shape of the subject (a process called reconstruction). If colour information is collected at each point, then the colours on the surface of the subject can also be determined.

3D scanners share several traits with cameras. Like most cameras, they have a cone-like field of view, and like cameras, they can only collect information about surfaces that are not obscured. While a camera collects colour information about surfaces within its field of view, a 3D scanner collects distance information about surfaces within its field of view. The "picture" produced by a 3D scanner describes the distance to a surface at each point in the picture. This allows the three dimensional position of each point in the picture to be identified.

For most situations, a single scan will not produce a complete model of the subject. Multiple scans, even hundreds, from many different directions are usually required to obtain information about all sides of the subject. These scans have to be brought into a common reference system, a process that is usually called alignment or registration, and then merged to create a complete model. This whole process, going from the single range map to the whole model, is usually known as the 3D scanning pipeline.
src : Fausto Bernardini, [Holly E. Rushmeier (2002)](https://en.wikipedia.org/wiki/Holly_Rushmeier). "[The 3D Model Acquisition Pipeline](http://www1.cs.columbia.edu/~allen/PHOTOPAPERS/pipeline.fausto.pdf)" (pdf). Comput. Graph. Forum. 21 (2): 149–172. doi:[10.1111/1467-8659.00574](https://doi.org/10.1111%2F1467-8659.00574).

# DESCRIPTION:
The project is undertaken by four interns during the Summer of 2017 under the Ekalavya Summer Internship sponsored by the MHRD,India at Integrated Development Lab, Department of Computer Science and Engineering, IIT Bombay.
  ##  1. Sagar Satapathy, NIT Rourkela
  ##  2. Animesh Srivastava, NIT Hamirpur
  ##  3. Anchal Singh, NIT Uttarakhand
  ##  4. Soumya Sambit Rath, NIT Rourkela
  
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
  
# INSTALLATION
Download the installscript.sh file and execute it.
```
$cd "< path of the file >"
$./installscript.sh
```

# USAGE:
  
# CONTRIBUTING

# CREDITS



Copyright (c) 2017 Team SAAS , the above open source program codes are worked and tested on Ubuntu Linux 14.04.5
