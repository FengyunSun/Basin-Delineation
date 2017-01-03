# Basin-Delineation
Useful Tool for Basin Deliniation


Make sure you already enabled Spatial Analyst Open ArcMAP, in menu look for Customize -- Extensions -- check the box before "Spatial Analyst"

----

### Step by step precedures:
    
    1. "DEM" data should be prepared before run "BasinDelineationPart1_sun.py"
    
    2. Edit and Run script "BasinDelineationPart1_sun.py"
        2.1  Right click "BasinDelineationPart1_sun.py", select "Edit with IDLE"
        2.2 Change the dem path "E:\try\dem" (line 1) to your path and your dem name
        2.3 Change the version of ArcGIS (ArcGIS10.4 or Desktop10.4 in lines 5-9) to the same of your version
        2.4 If your ArcGIS is not installed in the default path, then change the path information accordingly.
        2.5 Press "F5" to run the script
        2.6 The fail or complete information will shown in Python Shell window, if a new blank line appears in the shell window, it succeed.
        
    3. Make "BasinOutlet" layer according to the "FlowAcc_Flow" file produced by "BasinDelineationPart1_sun.py"
    
    4. Edit and Run script "BasinDelineationPart2_sun.py"
        4.1 Right click "BasinDelineationPart2_sun.py", select "Edit with IDLE"
        4.2 Change the BasinOutlet path "C:\Delineation\BasinOutlet.shp"  (line 1) to your path and data name
        4.3 Change the version of ArcGIS (ArcGIS10.4 or Desktop10.4 in lines 5-9) to the same of your version
        4.4 If your ArcGIS is not installed in the default path, then change the path information accordingly.
        4.5 Press "F5" to run the script
        
    5. Check the result in "C:\Delineation" with ArcCatalog
    
    6. If the basin border turns out not correct, re-edit the "BasinOutlet", and re-run "BasinDelineationPart2_sun.py"

----

### Brief tips on how to prepare "DEM" and "BasinOutlet" data are listed as follows:

    1. Tips on how to prepar DEM (input of BasinDelineationPart1_sun.py)
        1.1 Download DEM (https://viewer.nationalmap.gov/basic/), elevation products(3DEP).
        DEM data with 30-meter resolusion are recomended, 10-meter data are too large for big basins, takes a lot of time to calculate.
        1.2 Mosic DEM: 
            －In catalog, right click the folder, select make a new Personal Geodatabase. 
            －Right click the Geodatabase, select make new Raster Dataset.
            －Right click the new Dataset, selct Load -- load data, selct all the downloaded DEM data

    2. Tips on how to make "BasinOutlet" layer (input of BasinDelineationPart2_sun.py)
        2.1 FlowAcc_Flow data, Layer Properties --Symbology --Classified --2 classes ...
    --Classify --set the first Break value to 5000, after these steps, the riverlines should shown.
        2.2 Make BasinOutlet data, this is the outlet the whole basin. 
            －first convert the lat and longi to degree format. Note: west longitude should be negative;
            －put lat and lon in .xls file, Arcgis has problem with .xlsx; 
            －Import the x y data, File --Add data --Add XY data, Select Geographic projection;
            －Export the imported layer as a raster layer;
            －Creat a new point shapefile with the name of "BasinOutlet";
            －Using "Editor" toolbar, edit the points according to FlowAcc_Flow data. (Note: the PourPoint should be right on the stream with 0 tolerance)

