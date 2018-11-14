#-------------------------------------------------------------------------------
# Name:        HW4
# Purpose:     Calculate semiminor axis
#
# Author:      Terry Woodard
#
# Created:     19/09/2017
#-------------------------------------------------------------------------------


#f = (a-b)/a
#a = semimajor axis b = semiminor axis
#inverse = 1/f >>> (1/f)^-1 = f
#eccentricity e^2 = 2f - f^2
#b = a*sqrt(1-e^2)
gcs = open('D:\Geoprocessing\HW\HW3\gcs.prj','r').read()
geo, coor, dat, spheroid, extra, un = gcs.split('[') #split at the bracket

import re
dir(re)
sph_num = re.findall('\d+.\d+', spheroid)
a = float(sph_num[1]) #semimajor axis
fin = float(sph_num[2]) #inverse flattening ratio
f = fin**-1 #flattening ratio

e = 2*f - f**2 #eccentricity
import math
b = a*(math.sqrt(1-e)) #semiminor axis

print('The semiminor axis is {}'.format(b))
