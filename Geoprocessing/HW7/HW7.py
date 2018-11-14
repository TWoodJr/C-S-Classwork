#-------------------------------------------------------------------------------
# Name:        HW7
# Purpose:     arcpy syntax
#
# Author:      Terry Woodard
#
# Created:     06/10/2017
#-------------------------------------------------------------------------------

import arcpy
from arcpy import env
env.workspace = r'D:/Geoprocessing/HW/HW7'
env.OverwriteOutput = True
inFile = "BaileysRegions.shp"
#Project file
projFile = "baileys_albers.shp"
if arcpy.Exists(projFile):
    arcpy.Delete_management(projFile)
    print 'File exists and is being deleted'
arcpy.Project_management(inFile, projFile, "PROJCS['NAD_1983_Texas_Centric_Mapping_System_Albers',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',1500000.0],PARAMETER['False_Northing',6000000.0],PARAMETER['Central_Meridian',-100.0],PARAMETER['Standard_Parallel_1',27.5],PARAMETER['Standard_Parallel_2',35.0],PARAMETER['Latitude_Of_Origin',18.0],UNIT['Meter',1.0]]", "", "GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "NO_PRESERVE_SHAPE", "", "NO_VERTICAL")
print 'File projected'

#Select by attribute
selectFile = "great_plains.shp"
if arcpy.Exists(selectFile):
    arcpy.Delete_management(selectFile)
    print 'File exists and is being deleted'
arcpy.Select_analysis(projFile, selectFile, "\"PROVINCE\" = 'Great Plains Steppe and Shrub Province'")
print 'Attributes selected'

#Buffer
buffFile = "buffer1k_gp.shp"
if arcpy.Exists(buffFile):
    arcpy.Delete_management(buffFile)
    print 'File exists and is being deleted'
arcpy.Buffer_analysis(selectFile, buffFile, "1000 Meters")
print 'Buffer Calculated'