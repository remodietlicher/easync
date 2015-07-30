INFO
----
Author: Remo Dietlicher
Correspondence: remo.dietlicher@env.ethz.ch

DESCRIPTION
-----------
This is a simple GUI to visualize and edit netCDF files. It currently handles
only SCM data (variable vs time, variable vs height, time-height matrix for visualization and time-height matrix for editing)
It is easily extendable to handle global data.

CAUTION
-------
Use only on copies of your valuable data. The program opens the netCDF files with read and write access. It should make copies of the data whenever you are manipulating them and only write to the file when asked to do so, but it's not completely debugged so handle with care.

USAGE
-----
Load the GUI:
   >> python mainwindow.py

View data:
1) Use the file browser to open your *.nc file.
2) [optional] add a 'special' variable consisting of variables contained
   in the *.nc file.
   E.g.
   '(variable1+variable2)/(variable4)'
3) select the variables you want to plot and hit the 'show plot' button.
4) [Optional] Modify/Save your plot using the configuration window.

Edit data:
1) Use the file browser to open your *.nc file.
2) select the variables you want to modify and hit the 'modify data' button.
3) select timestep you want to modify and drag blue dots wherever you want.
4) [optional] hit the 'Use for all Timesteps' button to apply the current slice to all Timesteps.
5) hit the 'save' button to write the data to the .nc file you opened. Note that this overrides the file and you may want to make a copy first.

REQUIREMENTS
------------
Python,
Python modules: PyQt, numpy, matplotlib.pyplot
