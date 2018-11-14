#-------------------------------------------------------------------------------
  # File: Work.py

  # Description: find min work value

  # Student's Name: Terry Woodard

  # Student's UT EID: tgw466

  # Course Name: CS 313E

  # Unique Number: 86325

  # Date Created: 7/25/2018

  # Date Last Modified: 7/26/2018
#-------------------------------------------------------------------------------

def find_all_solutions(n, k):
	total = n
	p = 1
	v = n // (k ** p)

	while (v > 0):
		total += v
		p += 1
		v = n // (k ** p)

	return total

def binarySearch(n, k):
  lo = 0
  hi = n
  min_v = n

  while (lo <= hi):
  	v = (lo + hi) // 2
  	if (find_all_solutions(v,k) > n):
  		if v < min_v:
  			min_v = v
  		hi = v - 1
  	elif find_all_solutions(v,k) < n:
  		lo = v + 1
  	else:
  		return v

  return min_v

def main():
	work_file = open("work.txt","r")
	num_cases = int(work_file.readline())
	code_lines = []

	for i in range (num_cases):
		line = work_file.readline().split()
		for j in range (len(line)):
			line[j] = int(line[j])
		code_lines.append(line)

	for case in code_lines:
		n,k = case[0],case[1]
		print(binarySearch(n,k))

	work_file.close()

if __name__ == '__main__':
    main()
