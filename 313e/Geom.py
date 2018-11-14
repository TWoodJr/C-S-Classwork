#-------------------------------------------------------------------------------
#  File: Geom.py

#  Description: OOP with geometric shapes

#  Student Name: Terry Woodard

#  Student UT EID: tgw466

#  Partner Name: Jerry Che

#  Partner UT EID: jc78222

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: 6/18/2018

#  Date Last Modified: 6/21/2018
#-------------------------------------------------------------------------------

import math

class Point (object):
  # constructor
  # x and y are floats
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  # other is a Point object
  def dist (self, other):
    return math.hypot(self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  # takes no arguments
  # returns a string
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  # x, y, and radius are floats
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)


  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  # the only argument c is a Circle object
  # returns a boolean
  def does_intersect (self, c):
    distance = self.center.dist(c.center)
    return(distance < (self.radius + c.radius))

  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  # the only argument, r, is a rectangle object
  def circle_circumscribes (self, r):
    self.center.x = r.ul.x + r.length()/2
    self.center.y = r.ul.y - r.width()/2
    distance = self.center.dist(r.ul)
    return Circle(distance,self.center.x,self.center.y)

  # string representation of a circle
  # takes no arguments and returns a string
  def __str__ (self):
    return ('' + str(self.center.x) + ', ' + str(self.center.y) + ', ' + str(self.radius))

  # test for equality of radius
  # the only argument, other, is a circle
  # returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs(self.radius - other.radius) < tol)

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
    return (abs(self.lr.x - self.ul.x))

  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
    return (abs(self.lr.y - self.ul.y))

  # determine the perimeter
  # takes no arguments, returns a float
  def perimeter (self):
    return ((self.length()*2) + (self.width())*2)

  # determine the area
  # takes no arguments, returns a float
  def area (self):
    return (self.length()) * (self.width())

  # determine if a point is strictly inside the Rectangle
  # takes a point object p as an argument, returns a boolean
  def point_inside (self, p):
    distance = self.ul.dist(p)
    return ((distance < self.length()) and (distance < self.width()))

  # determine if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  def rectangle_inside (self, r):
    distance = self.ul.dist(r.ul)
    return ((distance < (self.length() - r.length())) and (distance < (self.width() - r.width())))

  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  def does_intersect (self, other):
    x_distance = self.ul.x - other.ul.x
    y_distance = self.ul.y - other.ul.y
    return ((x_distance > (self.length() + other.length())) or (y_distance > (self.width() + other.width())))

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  # takes a circle object c as input and returns a rectangle object
  def rect_circumscribe (self, c):
    ul_x = c.center.x - c.radius
    ul_y = c.center.y + c.radius
    lr_x = c.center.x + c.radius
    lr_y = c.center.y - c.radius
    return Rectangle(ul_x,ul_y,lr_x,lr_y)

  # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
    return ('' + str(self.ul.x) + ', ' + str(self.ul.y) + ', ' + str(self.lr.x) + ', ' + str(self.lr.y))

  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs((self.width() - other.width()) < tol) and (abs(self.length() - other.length()) < tol))

def main():
  # open the file geom.txt
    cord_list = []
    geom_file = open("geom.txt", "r")

    for line in geom_file:
        line = line.rstrip().split()
        cord_list.append(line)
  # create Point objects P and Q
    p = Point(float(cord_list[0][0]),float(cord_list[0][1]))
    q = Point(float(cord_list[2][0]),float(cord_list[2][1]))
  # print the coordinates of the points P and Q
    print 'Coordinates of P:', p
    print 'Coordinates of Q:', q
  # find the distance between the points P and Q
    print 'Distance between P and Q', p.dist(q)
  # create two Circle objects C and D
    c = Circle(float(cord_list[4][2]),float(cord_list[4][1]),float(cord_list[4][0]))
    d = Circle(float(cord_list[6][2]),float(cord_list[6][1]),float(cord_list[6][0]))
  # print C and D
    print 'Circle C:', c
    print 'Circle D:', d
  # compute the circumference of C
    print 'Circumference of C:', c.circumference()
  # compute the area of D
    print 'Area of D:', d.area()
  # determine if P is strictly inside C
    c.point_inside(p)
    if c.point_inside(p) == True:
        print 'P is inside C'
    else:
        print 'P is not inside C'
  # determine if C is strictly inside D
    d.circle_inside(c)
    if d.circle_inside(c) == True:
        print 'C is inside D'
    else:
        print 'C is not inside D'
  # determine if C and D intersect (non zero area of intersection)
    c.does_intersect(d)
    if c.does_intersect == True:
        print 'C does intersect D'
    else:
        print 'C does not intersect D'
  # determine if C and D are equal (have the same radius)
    c.__eq__(d)
    if c.__eq__(d) == True:
        print 'C is equal to D'
    else:
        print 'C is not equal to D'
  # create two rectangle objects G and H
    g = Rectangle(float(cord_list[8][0]),float(cord_list[8][1]),float(cord_list[8][2]),float(cord_list[8][3]))
    h = Rectangle(float(cord_list[10][0]),float(cord_list[10][1]),float(cord_list[10][2]),float(cord_list[10][3]))
  # print the two rectangles G and H
    print 'Rectangle G:', g
    print 'Rectangle H:', h
  # determine the length of G (distance along x axis)
    print 'Length of G:', g.length()
  # determine the width of H (distance along y axis)
    print 'Width of H:', h.width()
  # determine the perimeter of G
    print 'Perimeter of G:', g.perimeter()
  # determine the area of H
    print 'Area of H:', h.area()
  # determine if point P is strictly inside rectangle G
    g.point_inside(p)
    if g.point_inside(p) == True:
        print 'P is inside G'
    else:
        print 'P is not inside G'
  # determine if rectangle G is strictly inside rectangle H
    h.rectangle_inside(g)
    if h.rectangle_inside(g) == True:
        print 'G is inside H'
    else:
        print 'G is not inside H'
  # determine if rectangles G and H overlap (non-zero area of overlap)
    g.does_intersect(h)
    if g.does_intersect(h) == True:
        print 'G does overlap H'
    else:
        print 'G does not overlap H'
  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
    print 'Circle that circumscribes G:', c.circle_circumscribes(g)
  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
    print 'Rectangle that circumscribes D:', g.rect_circumscribe(d)
  # determine if the two rectangles have the same length and width
    g.__eq__(h)
    if g.__eq__(h) == True:
        print 'Rectangle G is equal to H'
    else:
        print 'Rectangle G is not equal to H'
  # close the file geom.txt
    geom_file.close()

if __name__ == "__main__":
  main()

