#-------------------------------------------------------------------------------
#  File: TopoSort.py

#  Description: topological sort

#  Student Name: Terry Woodard

#  Student UT EID: tgw466

# Partner's Name: Jerry Che

# Partner's UT EID: jc78222

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: 8/17/2018

#  Date Last Modified: 8/18/2018
#-------------------------------------------------------------------------------

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex ( self, label):
    if not self.has_vertex (label):
      self.Vertices.append (Vertex (label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)

      # add a new row for the new Vertex in the adjacency matrix
      new_row = []
      for i in range (nVert):
        new_row.append (0)
      self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack()

    # mark vertex v as visited and push it on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    def bfs (self, v):
        bfs_list = []
        theQueue = Queue()
        self.Vertices[v].visited = True
        bfs_list.append(self.Vertices[v].label)
        theQueue.enqueue(v)

        while not theQueue.isEmpty():
          v1 = theQueue.dequeue()
          v2 = self.get_adj_unvisited_vertex(v1)
          while v2 != -1:
            self.Vertices[v2].visited = True
            bfs_list.append(self.Vertices[v2].label)
            theQueue.enqueue(v2)
            v2 = self.get_adj_unvisited_vertex(v1)
        for j in range(len(self.Vertices)):
            self.Vertices[j].visited = False
        return bfs_list

    def get_edge_weight (self, from_vertex_label, to_vertex_label):
        start = self.get_index(from_vertex_label)
        finish = self.get_index(to_vertex_label)
        weight = self.adjMat[start][finish]
        return weight

  # Hint : for any directed graph, either the graph has a directed cycle
  # OR it has a topological sort of all of its vertices (but not both)

  # Hint : try using depth first search

  # returns True if the graph has a directed cycle and False otherwise
  def has_cycle (self):
    theStack = Stack()
    for i in range(len(self.Vertices)):
        self.Vertices[i].visited = True
        theStack.push(i)
        while not theStack.isEmpty():
          if (self.get_edge_weight(theStack.peek(), i) != 0):
             return True
          u = self.get_adj_unvisited_vertex(theStack.peek())
          if u == -1:
            u = theStack.pop()
          else:
            self.Vertices[u].visited = True
            theStack.push(u)
        for j in range(len(self.Vertices)):
            self.Vertices[j].visited = False
    return False

  def noUnvistedPredecessor (self, v):
    nVert = len(self.Vertices)
    for i in range(nVert):
      if (self.adjMat[i][v] != 0) and (not self.Vertices[i].wasVisited()):
        return False
    return True

  # return a list of vertices (vertex objects) which are in order
  # of a topological sort
  # in particular if there is a directed edge from a to b, b must not be
  # before a in the list
  # you may assume there is a topological sort of all the vertices
  def topo_sort (self):
    nVert = len(self.Vertices)
    topo_list = []
    theDeque = Deque()
    if self.hasCycle():
        return None
    for i in range(nVert):
        no_predecessor = True
        for j in range(nVert):
          if self.adjMat[j][i] != 0:
              no_predecessor = False
              break
        if no_predecessor:
            self.Vertices[i].visited = True
            topo_list.append(self.Vertices[i].label)
            theDeque.append(i)

    while not theDeque.isEmpty():
      v1 = theDeque.pop()
      v2 = self.getAdjUnvisitedVertex(v1)
      if not self.noUnvistedPredecessor(v2):
          theDeque.appendLeft(v1)
      else:
          while v2 != -1:
            if self.noUnvistedPredecessor(v2):
                self.Vertices[v2].visited = True
                topo_list.append(self.Vertices[v2].label)
                theDeque.append(v2)
                v2 = self.getAdjUnvisitedVertex(v1)
            else:
              theDeque.appendLeft(v2)
              break
    for j in range(len(self.Vertices)):
            self.Vertices[j].visited = False
    return topo_list

def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  in_file = open ("topo.txt", "r")

  # read the Vertices
  num_vertices = int ((in_file.readline()).strip())
  print (num_vertices)

  for i in range (num_vertices):
    city = (in_file.readline()).strip()
    print (city)
    cities.add_vertex (city)

  # read the edges
  num_edges = int ((in_file.readline()).strip())
  print (num_edges)

  for i in range (num_edges):
    edge = (in_file.readline()).strip()
    print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (num_vertices):
    for j in range (num_vertices):
      print (cities.adjMat[i][j])
    print ()
  print()

  # read the starting vertex for dfs and bfs
  start_vertex = (in_file.readline()).strip()
  print (start_vertex)

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)
  print (start_index)

  # do depth first search
  print ("\nDepth First Search from " + start_vertex)
  cities.dfs (start_index)
  print()

  print has_cycle()

  print topo_sort()

  # close the file
  in_file.close()

if __name__ == '__main__':
    main()
