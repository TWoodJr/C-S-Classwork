#-------------------------------------------------------------------------------
#  File: Josephus.py

#  Description: circular linked list in josephus problem

#  Student Name: Terry Woodard

#  Student UT EID: tgw466

# Partner's Name: Jerry Che

# Partner's UT EID: jc78222

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: 8/1/2018

#  Date Last Modified: 8/2/2018
#-------------------------------------------------------------------------------

class Link(object):
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class CircularList(object):
  # Constructor
  def __init__(self):
    self.first = None

  # Insert an element (value) in the list
  def insert(self, item):
    newLink = Link(item)
    current = self.first
    if current == None:
      self.first = newLink
      newLink.next = self.first
      return
    while current.next != self.first:
      current = current.next
    current.next = newLink
    newLink.next = self.first

  # Find the link with the given key (value)
  def find(self, key):
    current = self.first
    if current == None:
        return None
    while current.data != key:
        if current.next == self.first:
            return None
        else:
            current = current.next
    return current.data

  # Delete a link with a given key (value)
  def delete(self, key):
    previous = self.first
    current = self.first
    if current == None:
        return None
    while current.data != key:
        if current.next == self.first:
            return None
        else:
            previous = current
            current = current.next
    if current == self.first:
        self.first = self.first.next
    elif current.next == self.first:
        previous.next = self.first
    else:
        previous.next = current.next
    return current.data

  # Delete the nth link starting from the Link start
  # Return the next link from the deleted Link
  def delete_after(self, start, n):
    current = self.first
    count = 0
    if current == None:
        return None
    while current.data != start:
        current = current.next
    while count != n:
        current = current.next
        count += 1
    self.delete(current.data)
    return current.next

  # Return a string representation of a Circular List
  def __str__(self):
    current = self.first
    s = ''
    if current == None:
        return s
    while current != self.last:
        s += str(current.data) + '  '
        current = current.next
    return s

def main():
    with open ("josephus.txt", "r") as jo_file:
        n = int(jo_file.readline().strip())
        start = int(jo_file.readline().strip())
        kill = int(jo_file.readline().strip())
    soldiers = CircularList()
    for i in range(start, n+1):
        soldiers.insert(i)
    while (soldiers.first.next != soldiers.first):
        nextStart = soldiers.delete_after(start, kill)
        print nextStart.data

if __name__ == '__main__':
    main()
