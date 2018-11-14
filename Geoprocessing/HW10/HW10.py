#-------------------------------------------------------------------------------
# Name:        HW10
# Purpose:     add RGB and veg type fields
#
# Author:      Terry Woodard
#
# Created:     28/10/2017
#-------------------------------------------------------------------------------



import arcpy
from arcpy import env
import os

path = r'E:\Geoprocessing\HW\HW10\EcosysTiffs'

env.workspace = path

tifList = [f for f in os.listdir(path) if f.endswith(".tif")] #list .tif files
#dictionary: red, green, blue, veg
atts = {1: {'red': 255, 'blue': 0, 'green': 0, 'veg': "Deforested"}, 2: {'red': 209, 'green': 255, 'blue': 115, 'veg': "Semi-deciduous forest"},\
        3: {'red': 85, 'green': 255, 'blue': 0, 'veg': "Highland forest"}, 4: {'red': 112, 'green': 168, 'blue': 0, 'veg': "Piedmont forest"},\
        5: {'red': 190, 'green': 255, 'blue': 232, 'veg': "Flooded forest"}, 6: {'red': 255, 'green': 211, 'blue': 127, 'veg': "Piedmont plam forest"},\
        7: {'red': 0, 'green': 255, 'blue': 0, 'veg': "Wetland forest"}, 8: {'red': 0, 'green': 99, 'blue': 0, 'veg': "Evergreen forest"},\
        9: {'red': 214, 'green': 157, 'blue': 188, 'veg': "Sub-Andean evergreen forest"}, 10: {'red': 197, 'green': 0, 'blue': 255, 'veg': "Successional riparian complex"},\
        11: {'red': 0, 'green': 77, 'blue': 168, 'veg': "Open water"}, 12: {'red': 0, 'green': 132, 'blue': 168, 'veg': "Herbaceous dominated wetlands"},\
        13: {'red': 190, 'green': 210, 'blue': 255, 'veg': "Palm dominated wetlands"}, 14: {'red': 255, 'green': 170, 'blue': 0, 'veg': "White sand vegetation"},\
        17: {'red': 255, 'green': 170, 'blue': 0, 'veg': "White sand vegetation"}}


for f in tifList: #add red values
    #arcpy.DeleteField_management(f, "RED")
    arcpy.AddField_management(f, "RED", "DOUBLE", 8, 3) #add new attribute
    with arcpy.da.UpdateCursor(f, ["Value", "RED"]) as cursor:
        for row in cursor:
            red = atts.get(row[0]).get('red') #get pixel value
            row[1] = red/255.0 #set new attribute
            cursor.updateRow(row)
    print 'RED value added to file {}'.format(f)

for f in tifList: #add green values
   #arcpy.DeleteField_management(f, "GREEN")
   arcpy.AddField_management(f, "GREEN", "DOUBLE", 8, 3) #add new attribute
   with arcpy.da.UpdateCursor(f, ["Value", "GREEN"]) as cursor:
        for row in cursor:
            green = atts.get(row[0]).get('green')#get pixel value
            row[1] = green/255.0 #set new attribute
            cursor.updateRow(row)
   print 'GREEN value added to file {}'.format(f)

for f in tifList: #add blue values
   #arcpy.DeleteField_management(f, "BLUE")
   arcpy.AddField_management(f, "BLUE", "DOUBLE", 8, 3) #add new attribute
   with arcpy.da.UpdateCursor(f, ["Value", "BLUE"]) as cursor:
        for row in cursor:
            blue = atts.get(row[0]).get('blue') #get pixel value
            row[1] = blue/255.0 #set new attribute
            cursor.updateRow(row)
   print 'BLUE value added to file {}'.format(f)

for f in tifList: #add veg type
   #arcpy.DeleteField_management(f, "VEGTYPE")
   arcpy.AddField_management(f, "VEGTYPE", "TEXT", "", "", 50) #add new attribute
   with arcpy.da.UpdateCursor(f, ["Value", "VEGTYPE"]) as cursor:
        for row in cursor:
            veg = atts.get(row[0]).get('veg') #get pixel value
            row[1] = veg #set new attribute
            cursor.updateRow(row)
   print 'VEGTYPE added to file {}'.format(f)