from math import pi

class Shape:
   def __init__(self, color):
       self._color = color

class Rectangle(Shape):
   def __init__(self, color, height, width):
       self._height = height
       self._width = width
       super().__init__(color)

   def get_area(self):
       return self._width * self._height

   def get_width(self):
       return self._width

   def get_height(self):
       return self._height

class Square(Rectangle):
   def __init__(self, color, width):
       super().__init__(color,width,width)

class Circle(Shape):
   def __init__(self, color, radius):
       self.__radius = radius
       super().__init__(color)

   def get_area(self):
       return pi * (self.__radius ** 2)

   def get_circumference(self):
       return 2 * pi * self.__radius

class Shapes:

   shape_list = []

   def add(self, shape: Shape):
       self.shape_list.append(shape)

   def clear(self):
       self.shape_list.clear()

   def get_total_area(self):
       total_area = 0
       for shape in self.shape_list:
           total_area += shape.get_area()
       return  total_area
