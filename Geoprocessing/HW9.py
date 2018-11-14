#-------------------------------------------------------------------------------
# Name:        HW9
# Purpose:     Create field in .tif files
#
# Author:      Terry Woodard
#
# Created:     20/10/2017
#-------------------------------------------------------------------------------


#import, set path, set environment, set workspace

#download files from server
#uncompress .gz files

#create list of .tif files
tifList = ...

#create new field
fname = "LCOVER"
fType = "TEXT"
fLength = ...

#loop through .tif list
for ... in list:
    arcpy.AddField_management(f, fname, fType, "", "", flength) #add new field to each .tif file
    with ... as cursor: #use update cursor to update values of new field
        for ... in cursor: #loop through update cursor
            #set attribute for each pixel value with if and elif statements
            if pixel value == 0:
                LCOVER = "Water"
            elif pixel value == 1:
                LCOVER = "Evergreen Needleleaf Forest"
            elif etc.
            #0 = Water
            #1 = Evergreen Needleleaf Forest
            #2 = Evergreen Broadleaf Forest
            #3 = Deciduous Needleleaf Forest
            #4 = Deciduoud Broadleaf Forest
            #5 = Mixed Forests
            #6 = Closed Shrublands
            #7 = Open Shrublands
            #8 = Woody Savannas
            #9 = Savannas
            #10 = Grasslands
            #11 = Permanent Wetlands
            #12 = Croplands
            #13 = Urban and Built-Up
            #14 = Cropland and natural Vegetation Mosaic
            #15 =Snow and Ice
            #16 = Barren or Sparsely Vegetated
            cursor.updateRow(...)