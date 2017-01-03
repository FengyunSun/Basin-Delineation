dem = r'C:\DemOutlet\dem'

import os, sys
#print sys.path
sys.path.append(r'C:\Python27\ArcGIS10.4\Lib\site-packages')
sys.path.append(r'C:\Program Files (x86)\ArcGIS\Desktop10.4\arcpy')
sys.path.append(r'C:\Program Files (x86)\ArcGIS\Desktop10.4\ArcToolbox\Scripts')
sys.path.append(r'C:\Program Files (x86)\ArcGIS\Desktop10.4\bin')
sys.path.append(r'C:\Python27\ArcGIS10.4\lib')
newpath = r'C:\Delineation'
if not os.path.exists(newpath):
    os.makedirs(newpath)
import arcpy
# Set the path of input data
fill_dem = r'C:\Delineation\fill_dem'
FlowDir_fill = r'C:\Delineation\FlowDir_fill'
FlowAcc_Flow = r'C:\Delineation\FlowAcc_Flow'
SnapPou_Pour = r'C:\Delineation\SnapPou_Pour'
Watersh_Flow = r'C:\Delineation\Watersh_Flow'
ShedBorder = r'C:\Delineation\ShedBorder'
arcpy.CheckOutExtension("spatial")
# Process: Fill
arcpy.gp.Fill_sa(dem, fill_dem, "") # Commond line 1 
# Process: Flow Direction
arcpy.gp.FlowDirection_sa(fill_dem, FlowDir_fill, "NORMAL", "") # Commond line 2
# Process: Flow Accumulation
arcpy.gp.FlowAccumulation_sa(FlowDir_fill, FlowAcc_Flow, "", "FLOAT") # Commond line 3
arcpy.CheckInExtension("spatial")
