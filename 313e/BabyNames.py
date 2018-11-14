#-------------------------------------------------------------------------------
#  File: BabyNames.py

#  Description: list of popular baby names

#  Student Name: Terry Woodard

#  Student UT EID: tgw466

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: 7/5/2018

#  Date Last Modified: 7/6/2018
#-------------------------------------------------------------------------------

#create empty dictionary
babynames = {}

#read each line into dictionary
#baby name is key and ranks in a list as value
names_file = 'names.txt'
names_open = open(names_file)
for line in names_open:
    line = line.rstrip().split()
    babynames[line[0]] = line[1:]


#function that returns if name is in dictionary
def name_search(name):
    if name in babynames:
        return True
    else:
        return False

#return all rankings for a name
def name_ranks(name):
    return babynames[name]

#return list of names that have a rank in all decades in order
def all_decades():
    allDecadesList = []
    for name in babynames:
        if '0' not in babynames[name]:
            allDecadesList.append(name)
    allDecadesList.sort()
    print 'There are ' + str(len(allDecadesList)) + ' names that appear in each decade'
    print 'Those names are:'
    for i in allDecadesList:
        print i
    return allDecadesList

#display list of names in order of rank for a given decade
def decade_rank(year):
    decadeList = []
    rank = 1
    while rank < 1000:
        for name in babynames:
            if int(babynames[name][year]) == rank:
                decadeList.append(name)
        rank += 1

    for num in range(len(decadeList)):
        print str(decadeList[num]) + ': ' + str(babynames[decadeList[num]][year])

#display names that get more popular each decade
def more_pop():
    more_popList = []
    for name in babynames:
        if '0' not in babynames[name]:
            for value in range(len(babynames[name])):
                babynames[name][value] = int(babynames[name][value])
                if babynames[name] == sorted(babynames[name], reverse=True):
                    more_popList.append(name)
    more_popList.sort()
    print str(len(more_popList)) + ' names are more popular in every decade'
    for i in more_popList:
        print i

#display names that get less popular each decade
def less_pop():
    less_popList = []
    for name in babynames:
        if '0' not in babynames[name]:
            for value in range(len(babynames[name])):
                babynames[name][value] = int(babynames[name][value])
                if babynames[name] == sorted(babynames[name]):
                    less_popList.append(name)
    less_popList.sort()
    less_popSet = set()
    for p in less_popList:
        less_popSet.add(p)
    less_popList = list(less_popSet)
    print str(len(less_popList)) + ' names are less popular in every decade'
    for i in sorted(less_popList):
        print i


def main():
    #create loop for menu options
    #break on quit
    print 'Options:'
    print 'Enter 1 to search for names.'
    print 'Enter 2 to display data for one name.'
    print 'Enter 3 to display all names that appear in all decades.'
    print 'Enter 4 to display the name ranking for one decade'
    print 'Enter 5 to display all names that are more popular in every decade.'
    print 'Enter 6 to display all names that are less popular in every decade.'
    print 'Enter 7 to quit.'
    select = int(raw_input('Enter choice:'))
    while select > 0 and select < 8:
        if int(select) == 1:
            #call name_search
            name = str(raw_input('Enter a name:'))
            name_search(name)
            if name_search(name) == True:
                print str(name) + ' was found'
            else:
                print str(name) + ' does not appear in any decade.'
            select = int(raw_input('Enter choice:'))
        elif int(select) == 2:
            #call name_ranks
            name = str(raw_input('Enter a name:'))
            name_ranks(name)
            print name
            print '1900: ' + babynames[name][0]
            print '1910: ' + babynames[name][1]
            print '1920: ' + babynames[name][2]
            print '1930: ' + babynames[name][3]
            print '1940: ' + babynames[name][4]
            print '1950: ' + babynames[name][5]
            print '1960: ' + babynames[name][6]
            print '1970: ' + babynames[name][7]
            print '1980: ' + babynames[name][8]
            print '1990: ' + babynames[name][9]
            print '2000: ' + babynames[name][10]
            select = int(raw_input('Enter choice:'))
        elif int(select) == 3:
            #call all_decades
            all_decades()
            select = int(raw_input('Enter choice:'))
        elif int(select) == 4:
            #call decade_rank
            print 'Enter 0 for 1900'
            print 'Enter 1 for 1910'
            print 'Enter 2 for 1920'
            print 'Enter 3 for 1930'
            print 'Enter 4 for 1940'
            print 'Enter 5 for 1950'
            print 'Enter 6 for 1960'
            print 'Enter 7 for 1970'
            print 'Enter 8 for 1980'
            print 'Enter 9 for 1990'
            print 'Enter 10 for 2000'
            year = int(raw_input('Enter a year:'))
            decade_rank(year)
            select = int(raw_input('Enter choice:'))
        elif int(select) == 5:
            #call more_pop
            more_pop()
            select = int(raw_input('Enter choice:'))
        elif int(select) == 6:
            #call less_pop
            less_pop()
            select = int(raw_input('Enter choice:'))
        else:
            break

if __name__ == '__main__':
    main()
