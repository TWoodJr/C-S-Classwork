#-------------------------------------------------------------------------------
#  File: TestBinaryTree.py

#  Description: modify the binary tree class

#  Student Name: Terry Woodard

#  Student UT EID: tgw466

# Partner's Name: Jerry Che

# Partner's UT EID: jc78222

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: 8/8/2018

#  Date Last Modified: 8/9/2018
#-------------------------------------------------------------------------------

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
        self.root = None

  # Search for a node with the key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
	if (val < current.data):
          current = current.lChild
	else:
	  current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

  # In order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      inOrder (aNode.lChild)
      print aNode.data
      inOrder (aNode.rChild)

  # Pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print aNode.data
      preOrder (aNode.lChild)
      preOrder (aNode.rChild)

  # Post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      postOrder (aNode.lChild)
      postOrder (aNode.rChild)
      print aNode.data

  def is_similar_helper(self, aNode, bNode):
    if (aNode == None) and (bNode == None):
        return True
    elif (aNode.lChild == None and aNode.rChild == None):
        if (bNode.lChild != None or bNode.rChild != None):
            return False
    elif (bNode.lChild == None and bNode.rChild == None):
        if (aNode.lChild != None or aNode.rChild != None):
          return False
    elif (aNode == None and bNode != None) or (aNode != None and bNode == None):
        return False
    elif (aNode.data != bNode.data):
        return False

    return (self.is_similar_helper(aNode.lChild, aNode.lChild) and self.is_similar_helper(aNode.rChild, aNode.rChild)) and (aNode.data == bNode.data)

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
    return self.is_similar_helper(self.root, pNode.root)


  def print_level_helper(self, printNode, level):
    if printNode == None:
        return
    if level > 1:
        return self.print_level_helper(printNode.lChild, level - 1), self.print_level_helper(printNode.rChild, level - 1)
    else:
        print str(printNode.data)

  # Prints out all nodes at the given level
  def print_level (self, level):
    self.print_level_helper(self.root, level)


  def get_height_helper(self, cNode):
    if cNode == None:
        return 0
    else:
        return 1 + max(self.get_height_helper(cNode.lChild), self.get_height_helper(cNode.rChild))

  # Returns the height of the tree
  def get_height (self):
    return self.get_height_helper(self.root)


  def num_nodes_helper(self, count):
    if count == None:
        return 0
    else:
        return 1 + self.num_nodes_helper(count.lChild) + self.num_nodes_helper(count.rChild)

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    self.num_nodes_helper(self.root)

def main():
    # Create three trees - two are the same and the third is different
    same1 = Tree()
    same2 = Tree()
    diff = Tree()

    sameList = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 96]
    for i in sameList:
        same1.insert(i)
        same2.insert(i)

    diffList = [40, 60, 30, 25, 80]
    for i in diffList:
        diff.insert(i)

    # Test your method is_similar()
    print same1.is_similar(same2)
    print same1.is_similar(diff)

    # Print the various levels of two of the trees that are different
    same1.print_level(2)
    diff.print_level(2)

    # Get the height of the two trees that are different
    print same1.get_height()
    print diff.get_height()

    # Get the total number of nodes a binary search tree
    print same1.num_nodes()

if __name__ == '__main__':
    main()
