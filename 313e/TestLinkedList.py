#-------------------------------------------------------------------------------
#  File: TestLinkedList.py

#  Description: linked list class and functions

#  Student Name: Terry Woodard

#  Student UT EID: tgw466

# Partner's Name: Jerry Che

# Partner's UT EID: jc78222

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: 7/29/2018

#  Date Last Modified: 8/1/2018
#-------------------------------------------------------------------------------

class Link(object):
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class LinkedList(object):
  def __init__(self):
    self.first = None

  # get number of links
  def getNumLinks (self):
    current = self.first
    count = 0
    if current == None:
        return 0
    while current != None:
        count += 1
        current = current.next
    return count

  # Add data at the beginning of the list
  def addFirst(self, data):
    new_link = Link(data)
    new_link.next = self.first
    self.first = new_link

  # Add data at the end of a list
  def addLast(self, data):
    newLink = Link(data)
    current = self.first
    if current == None:
      self.first = newLink
      return
    while current.next != None:
      current = current.next
    current.next = newLink

  # Add data in an ordered list in ascending order
  def addInOrder(self, data):
    new_link = Link(data)
    prev = self.first
    current = self.first
    if current == None:
        self.first = new_link
        return
    while current.data < data:
        prev = current
        current = current.next
    prev.next = new_link
    new_link.next = current

  # Search in an unordered list, return None if not found
  def findUnordered(self, data):
    current = self.first
    if current == None:
        return None
    while current.data != data:
        if current.next == None:
            return None
        else:
            current = current.next
    return current.data

  # Search in an ordered list, return None if not found
  def findOrdered(self, data):
    current = self.first
    if current == None:
        return None
    while current.data != data:
        if current.next == None:
            return None
        elif current.data > data:
            return None
        else:
            current = current.next
    return current.data

  # Delete and return Link from an unordered list or None if not found
  def delete(self, data):
    previous = self.first
    current = self.first
    if current == None:
        return None
    while current.data != data:
        if current.next == None:
            return None
        else:
            previous = current
            current = current.next
        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
    return current.data

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__(self):
    current = self.first
    s = ''
    count = 0
    if current == None:
        return s
    while current != None:
        s += str(current.data) + '  '
        current = current.next
        count += 1
        if count % 10 == 0:
            s += '\n'
            count = 0
    return s

  # Copy the contents of a list and return new list
  def copyList(self):
    current = self.first
    new_list = LinkedList()
    while current != None:
        new_list.addLast(current.data)
        current = current.next
    return new_list

  # Reverse the contents of a list and return new list
  def reverseList(self):
    current = self.first
    new_list = LinkedList()
    while current != None:
        new_list.addFirst(current.data)
        current = current.next
    return new_list

  # Sort the contents of a list in ascending order and return new list
  def sortList(self):
    new_list = LinkedList()
    current = self.first
    while current != None:
        new_list.addInOrder(current.data)
        current = current.next
    return new_list

  # Return True if a list is sorted in ascending order or False otherwise
  def isSorted(self):
    current = self.first
    if current == None:
        return True
    while current.next != None:
        if current.next.data < current.data:
            return False
        else:
            current = current.next
    return True

  # Return True if a list is empty or False otherwise
  def isEmpty(self):
    if self.first == None:
        return True
    else:
        return False

  # Merge two sorted lists and return new list in ascending order
  def mergeList(self, b):
    new_list = LinkedList()
    current = self.first
    other = b.first
    if current == None:
        return b
    elif other == None:
        return self
    else:
        while current != None:
            new_list.addInOrder(current.data)
            current = current.next
        while other != None:
            new_list.addInOrder(other.data)
            other = other.next
    return new_list


  # Test if two lists are equal, item by item and return True
  def isEqual(self, b):
    current = self.first
    same = b.first
    while current != None:
        while same != None:
            if current.data != same.data:
                return False
            else:
                current = current.next
                same = same.next
    return True

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def removeDuplicates(self):
    new_list = LinkedList()
    current = self.first
    while current != None:
        if new_list.findOrdered(current.data):
            current = current.next
        else:
            new_list.addLast(current.data)
            current = current.next
    return new_list

def main():
  # Test methods addFirst() and __str__() by adding more than
  # 10 items to a list and printing it.
  test_link = LinkedList()
  test_link.addFirst(1)
  test_link.addFirst(2)
  test_link.addFirst(3)
  test_link.addFirst(4)
  test_link.addFirst(5)
  test_link.addFirst(6)
  test_link.addFirst(7)
  test_link.addFirst(8)
  test_link.addFirst(9)
  test_link.addFirst(10)
  test_link.addFirst(11)
  test_link.addFirst(12)
  test_link.addFirst(13)
  test_link.addFirst(14)
  print test_link

  # Test method addLast()
  test_link.addLast(100)
  print test_link

  # Test method addInOrder()
  order_link = LinkedList()
  order_link.addLast(1)
  order_link.addLast(4)
  order_link.addLast(5)
  print order_link
  order_link.addInOrder(3)
  print order_link

  # Test method getNumLinks()
  print order_link.getNumLinks()

  # Test method findUnordered()
  # Consider two cases - item is there, item is not there
  print test_link.findUnordered(4)
  print test_link.findUnordered(19)

  # Test method findOrdered()
  # Consider two cases - item is there, item is not there
  print order_link.findOrdered(3)
  print order_link.findOrdered(2)

  # Test method delete()
  # Consider two cases - item is there, item is not there
  print test_link.delete(100)
  print test_link
  print test_link.delete(50)

  # Test method copyList()
  original = LinkedList()
  original.addLast(1)
  original.addLast(2)
  original.addLast(3)
  print original
  copy = LinkedList()
  copy = original.copyList()
  print copy

  # Test method reverseList()
  forward = LinkedList()
  forward.addLast(1)
  forward.addLast(2)
  forward.addLast(3)
  forward.addLast(4)
  print forward
  rev = LinkedList()
  rev = forward.reverseList()
  print rev

  # Test method sortList()
  test_sort = LinkedList()
  test_sort.addLast(5)
  test_sort.addLast(3)
  test_sort.addLast(7)
  test_sort.addLast(6)
  sorted_list = LinkedList()
  sorted_list = test_sort.sortList()
  print sorted_list

  # Test method isSorted()
  # Consider two cases - list is sorted, list is not sorted
  print sorted_list.isSorted()
  print test_sort.isSorted()

  # Test method isEmpty()
  test_link.isEmpty()
  empty = LinkedList()
  print empty.isEmpty()
  print test_link.isEmpty()

  # Test method mergeList()
  merge1 = LinkedList()
  merge1.addLast(1)
  merge1.addLast(3)
  merge1.addLast(5)
  merge2 = LinkedList()
  merge2.addLast(2)
  merge2.addLast(4)
  merge2.addLast(7)
  merge2.addLast(8)
  merge_list = merge1.mergeList(merge2)
  print merge_list

  # Test method isEqual()
  # Consider two cases - lists are equal, lists are not equal
  same_link = LinkedList()
  same_link.addLast(1)
  same_link.addLast(2)
  equal_link = LinkedList()
  equal_link.addLast(1)
  equal_link.addLast(2)
  print same_link.isEqual(equal_link)
  print test_link.isEqual(order_link)

  # Test removeDuplicates()
  remove_test = LinkedList()
  remove_test.addLast(1)
  remove_test.addLast(3)
  remove_test.addLast(1)
  remove_test.addLast(1)
  remove_test.addLast(3)
  remove_test.addLast(5)
  print remove_test
  no_dup = LinkedList()
  no_dup = remove_test.removeDuplicates()
  print no_dup

if __name__ == "__main__":
  main()
