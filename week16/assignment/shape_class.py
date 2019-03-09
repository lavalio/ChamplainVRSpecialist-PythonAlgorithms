from math import pi
shape_list = []

class Shape:
   color = ""

   def add_shape(self, shape: Shape):
       shape_list.append(shape)

class Rectangle(Shape):
   len = 0
   height = 0
   # constructor
   def __init__(self, c, h, l):
       self.height = h
       self.len = l
       self.color = c

   def get_area(self):
       return self.len * self.height

   def get_perimeter(self):
       return 2*(self.len + self.height)

class Square(Shape):
   len = 0
   def __init__(self, c, l):
       self.len = l
       self.color = c
   def get_area(self):
       return self.len ** 2
   def get_perimeter(self):
       return self.len*4

class Circle(Shape):
   radius = 0
   # constructor
   def __init__(self, c, r):
       self.radius = r
       self.color = c

   def get_area(self):
       return pi * (self.radius ** 2)
   def get_circumference(self):
       return 2 * pi * self.radius

