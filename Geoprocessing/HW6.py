#-------------------------------------------------------------------------------
# Name:        HW6
# Purpose:     Find hours in each month each year from txt file
#
# Author:      Terry Woodard
#
# Created:     30/09/2017
#-------------------------------------------------------------------------------


import re
flist = r'D:\Geoprocessing\HW\HW5\file_list.txt' #import file

with open(flist) as f:
    txtlist = f.readlines() #read lines in file

days_month = {'01': 31, '02': {'common': 28, 'leap': 29}, '03': 31, '04': 30, '05': 31,
              '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
#dictionary for days in month

for datenum in txtlist:
    datenum = datenum.split('.')
    date = datenum[1] #split to only have YYYYMMDD values
    year = int(date[0:4]) #split into years
    month = date[4:6] #split into months
    daynum = days_month.get(month)
    if month == '02':
        if year%4 != 0: #check if leap year
            daynum = days_month.get('02').get('common') #common year
        elif year%100 != 0:
            daynum = days_month.get('02').get('leap') #leap year
        elif year%400 != 0:
            daynum = days_month.get('02').get('common') #common year
        else:
            daynum = days_month.get('02').get('leap') #leap year
    hours = daynum*24 #calculate hours in month
    print 'This file corresponds to year {} and month {}, and it has hours {} in a month'.format(year, month, hours)