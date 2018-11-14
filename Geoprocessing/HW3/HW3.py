#-------------------------------------------------------------------------------
# Name:        HW3
# Purpose:     String manipulation
#
# Author:      Terry Woodard
#
# Created:     17/09/2017
#--------------------------------------------------------------------------


gcs = open('D:\Geoprocessing\HW\HW3\gcs.prj','r').read()

geo, coor, dat, sph, extra, un = gcs.split('[') #split at the bracket
cs, csd = coor.split(',') #split each part at comma
datum, datu = dat.split(',')
sphere, cir, sh, jun = sph.split(',')
unit, deg = un.split(',')

print("Coordinate System: "+cs)
print("Datum: "+datum)
print("Spheroid: "+sphere)
print("Unit: "+unit)