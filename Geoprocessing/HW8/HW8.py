#-------------------------------------------------------------------------------
# Name:        HW8
# Purpose:     Attribute Table Manipulation
#
# Author:      Terry Woodard
#
# Created:     15/10/2017
#-------------------------------------------------------------------------------


import arcpy
from arcpy import env
path = r'E:/Geoprocessing/HW/HW8'
env.workspace = path

feat = set()
hydro = 'hydrolg020_TX.shp'
with arcpy.da.SearchCursor(hydro, ['FEATURE']) as cursor: #search cursor
    for eachRow in cursor:
        feat.add(eachRow) #add to set

for f in feat:
    name = str(f)
    u, fil, extra = name.split("'") #get rid of extra punctuation, use fil for attribute name in where clause
    where_clause = "\"FEATURE\" = " + "\'"+fil+"\'" #where clause
    fil = fil.replace(" ","") #take out space for file name
    outFile = fil+'.shp'
    if arcpy.Exists(outFile):
        arcpy.Delete_management(outFile)
    arcpy.Select_analysis(hydro, outFile, where_clause) #create file for attribute
    print '{} created'.format(outFile)
