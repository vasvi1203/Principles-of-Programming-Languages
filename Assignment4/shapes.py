from abc import ABC, abstractmethod
import turtle
import math
import time
t = turtle.Turtle()
t.speed(2)
t.shape("turtle")
w = turtle.Screen()

# Abstract base class as abstract methods as well as concrete methods are there
class Shape(object):
	def __init__(self):
		self.geometric = True
		
	def dimension(self):
		print("It is a 2-dimensional shape")

	@abstractmethod
	def get(self):
		pass
		
# Interface as only abstract methods are there		
class Instance(ABC):
	@abstractmethod
	def perimeter(self):
		pass
	
	@abstractmethod
	def area(self):
		pass
	
	@abstractmethod	
	def draw(self):
		pass

# Derived classes -->
		
class Ellipse(Shape):
	def __init__(self, a = 100, b = 50):
		self.a = a
		self.b = b
		
	def set(self, a, b):
		self.a = a
		self.b = b
		
	def get(self):
		return self.a, self.b
	
	def perimeter(self):
		self.p = 2 * math.pi * math.sqrt((self.a ** 2 + self.b ** 2)/2)
		print("Perimeter of ellipse with major axis a = {} and minor axis b = {} is {}".format(self.a, self.b, self.p))
		
	def area(self):
		print("Area of ellipse with major axis a = {} and minor axis b = {} is {}".format(self.a, self.b, math.pi * self.a * self.b))
		
	def draw(self):
		t.shape("circle")
		t.shapesize(self.b/10, self.a/10)
		t.fillcolor("white")
		time.sleep(2)
		t.reset()
		t.speed(2)
		t.shape("turtle")

class Circle(Shape):
	def __init__(self, r = 100):
		self.r = r
		
	def set(self, r):
		self.r = r
		
	def get(self):
		return self.r
	
	def perimeter(self):
		print("Perimeter of circle with radius = {} is {}".format(self.r, 2 * math.pi * self.r))
		
	def area(self):
		print("Area of circle with radius = {} is {}".format(self.r, math.pi * self.r * self.r))
		
	def draw(self):
		t.circle(self.r)
		time.sleep(2)
		t.reset()
		t.speed(2)
				
class Triangle(Shape):
	def __init__(self, a = 100, b = 100, c = 100):
		self.a = a
		self.b = b
		self.c = c
		
	def set(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	def get(self):
		return self.a, self.b, self.c 
			
	def perimeter(self):
		if (self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b):
			self.p = self.a + self.b + self.c
			print("Perimeter of triangle with sides a = {}, b = {}, c = {} is {}".format(self.a, self.b, self.c, self.p))
		else:
			print("Invalid triangle")
			
	def area(self):
		if (self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b):
			self.s = (self.a + self.b + self.c)/2
			self.h = math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))
			print("Area of triangle with sides a = {}, b = {}, c = {} is {}".format(self.a, self.b, self.c, self.h))
		else:
			print("Invalid triangle")
			
	def draw(self):
		if (self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b):
			t.forward(self.a)
			t.left(180 - ((math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2)/(2 * self.a * self.b))) * (180/math.pi)))
			t.forward(self.b)
			t.left(180 - ((math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2)/(2 * self.b * self.c))) * (180/math.pi)))
			t.forward(self.c)
			time.sleep(2)
			t.reset()
			t.speed(2)
		else:
			print("Invalid triangle")

class Parallelogram(Shape):
	def __init__(self, l = 200, b = 100):
		self.l = l
		self.b = b
		
	def set(self, l, b):
		self.l = l
		self.b = b
		
	def get(self):
		return self.l, self.b
		
	def perimeter(self):
		self.p = 2 * (self.l + self.b)
		print("Perimeter of parallelogram with length = {} and breadth = {} is {}".format(self.l, self.b, self.p))
		
	def area(self):
		self.s = self.l * self.b
		print("Area of parallelogram with length = {} and breadth = {} is {}".format(self.l, self.b, self.s))
		
	def draw(self):
		t.forward(self.l)
		t.left(60)
		t.forward(self.b)
		t.left(120)
		t.forward(self.l)
		t.left(60)
		t.forward(self.b)
		time.sleep(2)
		t.reset()
		t.speed(2)

# Hierarchy				
class Rectangle(Parallelogram):		
	def perimeter(self):
		self.p = 2 * (self.l + self.b)
		print("Perimeter of rectangle with length = {} and breadth = {} is {}".format(self.l, self.b, self.p))
		
	def area(self):
		self.s = self.l * self.b
		print("Area of rectangle with length = {} and breadth = {} is {}".format(self.l, self.b, self.s))
		
	def draw(self):
		t.forward(self.l)
		t.left(90)
		t.forward(self.b)
		t.left(90)
		t.forward(self.l)
		t.left(90)
		t.forward(self.b)
		time.sleep(2)
		t.reset()
		t.speed(2)

class Square(Shape):
	def __init__(self, a = 100):
		self.a = a
		
	def set(self, a):
		self.a = a
		
	def get(self):
		return self.a
		
	def perimeter(self):
		print("Perimeter of square with side = {} is {}".format(self.a, 4 * self.a))
		
	def area(self):
		print("Area of square with side = {} is {}".format(self.a, self.a ** 2))
		
	def draw(self):
		t.forward(self.a)
		t.left(90)
		t.forward(self.a)
		t.left(90)
		t.forward(self.a)
		t.left(90)
		t.forward(self.a)
		time.sleep(2)
		t.reset()
		t.speed(2)
				
class Pentagon(Shape):
	def __init__(self, a = 100):
		self.a = a
		
	def set(self, a):
		self.a = a
		
	def get(self):
		return self.a	
	
	def perimeter(self):
		print("Perimeter of pentagon with side = {} is {}".format(self.a, 5 * self.a))
		
	def area(self):
		self.p = (1/4) * (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (self.a ** 2))
		print("Area of pentagon with side = {} is {}".format(self.a, self.p))
	
	def draw(self):
		t.forward(self.a)
		t.left(72)
		t.forward(self.a)
		t.left(72)
		t.forward(self.a)
		t.left(72)
		t.forward(self.a)
		t.left(72)
		t.forward(self.a)
		time.sleep(2)
		t.reset()
		t.speed(2)
		
class Hexagon(Shape):
	def __init__(self, a = 100):
		self.a = a
		
	def set(self, a):
		self.a = a
		
	def get(self):
		return self.a	
	
	def perimeter(self):
		print("Perimeter of hexagon with side = {} is {}".format(self.a, 6 * self.a))
		
	def area(self):
		self.p = (3/2) * math.sqrt(3) * self.a ** 2
		print("Area of hexagon with side = {} is {}".format(self.a, self.p))
	
	def draw(self):
		t.forward(self.a)
		t.left(60)
		t.forward(self.a)
		t.left(60)
		t.forward(self.a)
		t.left(60)
		t.forward(self.a)
		t.left(60)
		t.forward(self.a)
		t.left(60)
		t.forward(self.a)
		time.sleep(2)
		t.reset()
		t.speed(2)

class Cube(Shape):
	def __init__(self, a = 100):
		self.a = a
		
	def set(self, a):
		self.a = a
		
	def get(self):
		return self.a
	
	# Virtual function
	def dimension(self):
		print("It is a 3-dimensional shape")
			
	def perimeter(self):
		print("Perimeter of cube with side = {} is {}".format(self.a, 12 * self.a))
		
	def area(self):
		print("Surface area of cube with side = {} is {}".format(self.a, 6 * self.a ** 2))
	
	def volume(self):
		print("Volume of cube with side = {} is {}".format(self.a, self.a ** 3))
		
	def draw(self):
		t.forward(self.a)
		t.left(90)
		t.forward(self.a)
		t.left(90)
		t.forward(self.a)
		t.left(90)
		t.forward(self.a)
		t.left(90)
		t.forward(self.a)
		t.left(60)
		t.forward(self.a/2)
		t.left(120)
		t.forward(self.a)
		t.left(60)
		t.forward(self.a/2)
		t.right(150)
		t.forward(self.a)
		t.right(30)
		t.forward(self.a/2)
		t.right(60)
		t.forward(self.a)
		t.right(120)
		t.forward(self.a/2)
		t.right(180)
		t.forward(self.a/2)
		t.right(150)
		t.forward(self.a)
		t.right(90)
		t.forward(self.a)
		t.right(90)
		t.forward(self.a)
		time.sleep(2)
		t.reset()
		t.speed(2)
		
class Cuboid(Shape):
	def __init__(self, l = 200, b = 200, h = 300):
		self.l = l
		self.b = b
		self.h = h
		
	def set(self, l, b, h):
		self.l = l
		self.b = b
		self.h = h
		
	def get(self):
		return self.l, self.b, self.h
	
	# Virtual function
	def dimension(self):
		print("It is a 3-dimensional shape")
			
	def perimeter(self):
		print("Perimeter of cuboid with length = {}, breadth = {} and height = {} is {}".format(self.l, self.b, self.h, 4 * (self.l + self.b + self.h)))
		
	def area(self):
		self.p = 2 * (self.l * self.b +self.b * self.h + self.l * self.h)
		print("Surface area of cuboid with length = {}, breadth = {} and height = {} is {}".format(self.l, self.b, self.h, self.p))
		
	def volume(self):
		print("Volume of cuboid with length = {}, breadth = {} and height = {} is {}".format(self.l, self.b, self.h, self.l * self.b * self.h))
		
	def draw(self):
		t.forward(self.l)
		t.left(90)
		t.forward(self.h)
		t.left(90)
		t.forward(self.l)
		t.left(90)
		t.forward(self.h)
		t.left(90)
		t.forward(self.l)
		t.left(60)
		t.forward(self.b/2)
		t.left(120)
		t.forward(self.l)
		t.left(60)
		t.forward(self.b/2)
		t.right(150)
		t.forward(self.h)
		t.right(30)
		t.forward(self.b/2)
		t.right(60)
		t.forward(self.l)
		t.right(120)
		t.forward(self.b/2)
		t.right(180)
		t.forward(self.b/2)
		t.right(150)
		t.forward(self.h)
		t.right(90)
		t.forward(self.l)
		t.right(90)
		t.forward(self.h)
		time.sleep(2)
		t.reset()
		t.speed(2)
