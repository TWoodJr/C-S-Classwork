#-------------------------------------------------------------------------------
#  File: Triangle.py

#  Description: greatest sum path

#  Student's Name: Terry Woodard

#  Student's UT EID: tgw466

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: 7/14/2018

#  Date Last Modified: 7/15/2018
#-------------------------------------------------------------------------------

import time
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
    num_lines = len(grid)
    num_solutions = 2 ** (num_lines - 1)
    maximum = 0

    for row in range(num_solutions):
        temp = int(grid[0][0])
        idx = 0
        for col in range(num_lines - 1):
          idx = idx + (row >> col & 1)
          temp += int(grid[col + 1][idx])
        if temp > maximum:
          maximum = temp

    return maximum

# returns the greatest path sum using greedy approach
def greedy (grid):
  gSum = 0
  rowAdd = 0
  num = 0
  for line in range(len(grid)-1):
    if len(grid[line]) > 1:
      if grid[line][num] > grid[line][num + 1]:
        rowAdd = grid[line][num]
      else:
        rowAdd = grid[line][num + 1]
        num += 1
    else:
      rowAdd = grid[line][0]
    gSum += rowAdd

  return gSum

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search_helper(grid, row, col):

  num_rows = len(grid)

  if row >= num_rows:
    return 0
  else:
    adj1 = rec_search_helper(grid, row + 1, col)
    adj2 = rec_search_helper (grid, row + 1, col + 1)
    fin = max(adj1, adj2) + int(grid[row][col])
  return fin

def rec_search (grid):
  return rec_search_helper(grid, 0, 0)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  num_lines = len(grid)

  for row in range(num_lines - 2, -1, -1):
    for col in range(row + 1):
      grid[row][col] = int(grid[row][col]) + max(int(grid[row+1][col]), int(grid[row+1][col+1]))
  val = grid[0][0]
  triangle = grid

  return val, triangle

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  triangle_list = []

  with open ("triangle.txt", "r") as in_file:
    n = int (in_file.readline ())
    for line in in_file:
      triangle_list = line.rstrip().split()
      triangle_list = [int (i) for i in triangle_list]
      triangle_list.append (triangle_list)

  return n, triangle_list

def main ():
  # read triangular grid from file
  n, triangle = read_file()
  print()

  ti = time.time()
  # output greatest path from exhaustive search
  total = exhaustive_search(triangle)
  print 'The greatest path sum through exhaustive search is ' + str(total) + '.'
  tf = time.time()
  del_t = tf - ti
  # print time taken using exhaustive search
  print 'The time taken for exhaustive search is ' + str(del_t) + ' seconds.'

  ti = time.time()
  # output greatest path from greedy approach
  total = greedy(triangle)
  print 'The greatest path sum through greedy approach is ' + str(total) + '.'
  tf = time.time()
  del_t = tf - ti
  # print time taken using greedy approach
  print 'The time taken for greedy approach is ' + str(del_t) + ' seconds.'

  ti = time.time()
  # output greatest path from divide-and-conquer approach
  total = rec_search(triangle)
  print 'The greatest path sum through divide-and-conquer approach is ' + str(total) + '.'
  tf = time.time()
  del_t = tf - ti
  # print time taken using divide-and-conquer approach
  print 'The time taken for divide-and-conquer approach is ' + str(del_t) + ' seconds.'

  ti = time.time()
  # output greatest path from dynamic programming
  total = dynamic_prog(triangle)
  print 'The greatest path sum through dynamic programming is ' + str(total) + '.'
  tf = time.time()
  del_t = tf - ti
  # print time taken using dynamic programming
  print 'The time taken for dynamic programming is ' + str(del_t) + ' seconds.'

if __name__ == "__main__":
  main()