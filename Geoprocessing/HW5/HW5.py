#-------------------------------------------------------------------------------
# Name:        HW5
# Purpose:     Rewrite .tif files to .img
#
# Author:      Terry Woodard
#
# Created:     23/09/2017
#-------------------------------------------------------------------------------

import re
flist = r'D:\Geoprocessing\HW\HW5\file_list.txt' #import file

with open(flist) as f:
    txtlist = f.readlines() #read lines in file

outPath = r'D:\Geoprocessing\HW\HW5\new_list.txt' #open output channel
outF = open(outPath,'w')

for newF in txtlist:
    newF = newF.replace('.tif','.img') #replaces .tif ending with .img
    outF.write(newF)
    print 'File name {} recorded'.format(newF) #print new file name to make sure loop works

outF.close() #close channel
