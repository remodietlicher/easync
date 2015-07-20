Info
----
Author: Remo Dietlicher
Correspondence: remo.dietlicher@env.ethz.ch

Description
-----------
This is a simple GUI to visualize netCDF files. It currently handles
only SCM data (variable vs time, variable vs height, time-height matrix).
It is easily extendable to handle global data.

Usage
-----
To load the GUI:
   >> python mainwindow.py

1) Use the file browser to open your *.nc file.
2) [Optional] add a 'special' variable consisting of variables contained
   in the *.nc file.
   E.g.
   '(variable1+variable2)/(variable4)'
3) select the variables you want to plot and hit the 'plot' button.
4) [Optional] Modify/Save your plot using the configuration window.


Requirements
------------
Python,
Python modules: PyQt, numpy, matplotlib.pyplot
