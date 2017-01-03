BasinOutlet = r'C:\DemOutlet\outlet.shp'

import sys
sys.path.append(r'C:\Python27\ArcGIS10.4\Lib\site-packages')
sys.path.append(r'C:\Program Files (x86)\ArcGIS\Desktop10.4\arcpy')
sys.path.append(r'C:\Program Files (x86)\ArcGIS\Desktop10.4\ArcToolbox\Scripts')
sys.path.append(r'C:\Program Files (x86)\ArcGIS\Desktop10.4\bin')
sys.path.append(r'C:\Python27\ArcGIS10.4\lib')

import arcpy
# Set the path of input data
FlowDir_fill = r'C:\Delineation\FlowDir_fill'
FlowAcc_Flow = r'C:\Delineation\FlowAcc_Flow'
SnapOutlet = r'C:\Delineation\SnapOutlet'
BasinBorder = r'C:\Delineation\BasinBorder.shp'
Basin_Flow = r'C:\Delineation\Basin_Flow'
arcpy.CheckOutExtension("spatial")
# Process: Snap Pour Point
arcpy.gp.SnapPourPoint_sa(BasinOutlet, FlowAcc_Flow, SnapOutlet, "0", "FID")
# Process: Watershed
arcpy.gp.Watershed_sa(FlowDir_fill, SnapOutlet, Basin_Flow, "Value")
# Process: Raster to Polygon
arcpy.RasterToPolygon_conversion(Basin_Flow, BasinBorder, "NO_SIMPLIFY", "VALUE")
arcpy.CheckInExtension("spatial")
