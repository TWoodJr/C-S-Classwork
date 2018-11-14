#-------------------------------------------------------------------------------
  # File: Boxes.py

  # Description: largest subset of nested boxes

  # Student's Name: Terry Woodard

  # Student's UT EID: tgw466

  # Partner's Name: Jerry Che

  # Partner's UT EID: jc78222

  # Course Name: CS 313E

  # Unique Number: 86325

  # Date Created: 7/22/2018

  # Date Last Modified: 7/23/2018
#-------------------------------------------------------------------------------

def read_txt():
	boxes = []

	with open ('boxes.txt', 'r') as box_file:
		n = int(box_file.readline ())
		for line in box_file:
			line = line.rstrip().split()
			line = [int(i) for i in line]
			line.sort()
			boxes.append(line)
	boxes.sort()

	return n, boxes

#check if box can be nested in another
def compare(box1, box2):
    return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

#subset of list
def subset(a, b, n, lo):
    sub = []
    if lo == n:
        sub.append(b)
    else:
        c = b[:]
        b.append(a[lo])
        return subset(a, b, n, lo+1) + subset(a, c, n, lo+1)
    return sub

#find largest subset which contains boxes that can be nested
def big_subset(sub_list):
	largest_sub = []
	fit = []
	len_sub = 0

	#confirm subsets in largest_subset contain nested boxes
	for sub in range(len (sub_list)):
		if len(sub_list[sub]) > 1:
			for box in range(1, len(sub_list[sub])):
				if compare(sub_list[sub][box - 1], sub_list[sub][box]):
					if box + 1 == len(sub_list[sub]):
						fit.append(sub_list[sub])
                else:
                    break
        else:
            pass

	#find largest subset length
	for sub in range (len(fit)):
		if len(fit[sub]) >= len_sub:
			len_sub = len(fit[sub])
		else:
			continue

	#add subsets with length equal to the largest subset length
   	for sub in range (len(fit)):
		if (len(fit[sub]) == len_sub):
			largest_sub.append(fit[sub])
		else:
			continue


	return largest_sub

def main():
	biggest_nest = []
	sub_list = []

	n, boxes = read_txt()

	sub_list = subset(boxes, sub_list, n, 0)

	biggest_nest = big_subset(sub_list)

	if len (biggest_nest[0]) > 1:
		print ('Largest Subset of Nesting Boxes')
		for sub in range(len(biggest_nest)):
			for box in range(len(biggest_nest[sub])):
				print(biggest_nest[sub][box])
			print ()
	else:
		print ("No Nesting Boxes")


if __name__ == '__main__':
    main()
