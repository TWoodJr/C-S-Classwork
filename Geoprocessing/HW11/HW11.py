#-------------------------------------------------------------------------------
# Name:        HW11
# Purpose:     GH method with vectors
#
# Author:      Terry Woodard
#
# Created:     08/11/2017
#-------------------------------------------------------------------------------


import arcpy
from arcpy import env
from arcpy.sa import *

path = r'E:/Geoprocessing/HW/HW11/'
env.workspace = path
arcpy.CheckOutExtension("Spatial")

#actual road
actualRd = "actual_rd.shp"
#simulated road
simRd = "ot1_line.shp"

#create output table
tab = "buffercells.dbf"
#arcpy.Delete_management(tab)

arcpy.CreateTable_management(path, tab)
arcpy.AddField_management(tab, "Buffer", "LONG", 5)
arcpy.AddField_management(tab, "Ncells", "LONG", 7)
arcpy.AddField_management(tab, "PropIn", "FLOAT", 4, 3)

#create buffer around actual road
bufroad = "bufroad.shp"
arcpy.Buffer_analysis(actualRd, bufroad, "100 Meters")

#intersect buffer with sim road
inters = "buf_intersect.shp"
arcpy.Intersect_analysis([simRd, bufroad], inters, "ALL", "", "")

#find total length of actual road
realrd = []
with arcpy.da.SearchCursor(actualRd, ["Shape_Leng"]) as cursor:
    for row in cursor:
        realrd.append(row[0])
        fullrd = sum(realrd)

#find cells of sim road in intersect


#insert values to table with insert cursor
tabcur = arcpy.da.InsertCursor(tab, ["Buffer", "Ncells", "PropIn"])
dist = 100
outRowValues = [dist, interrd, interrd/fullrd]
tabcur.insertRow(outRowValues)

del tabcur

