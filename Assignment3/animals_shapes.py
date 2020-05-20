'''Implementation of classes for various animals and shapes (10 classes each) to learn abstraction and encapsulation, public and private access specifiers in Python.'''

import turtle
import math
import time
t = turtle.Turtle()
t.speed(2)
t.shape("turtle")
w = turtle.Screen()

# Animals
class Animal(object):
	def __init__(self):
		self.eyes = 2		# public
		self.ears = 2		# public
		self.mouth = 1		
		self.tail = 1		
		self.__beak = 0		# private
		self.__wings = 0	# private
		
	def set_bird(self, beak = 1, wings = 2):
		self.__beak = beak	
		self.__wings = wings	
		
	def get_bird(self):
		return self.__beak, self.__wings
	
	def animal_char(self):
		return ("has {} eyes, {} ears, {} mouth and {} tail. ".format(self.eyes, self.ears, self.mouth, self.tail))
		
	def bird_char(self):
		return ("has {} eyes, {} beak and {} wings. ".format(self.eyes, self.get_bird()[0], self.get_bird()[1]))

class Dog(Animal):
	def char(self):
		print("Dog", self.animal_char())

	def eats(self):
		print("Dog is an omnivore.")
		
	def sound(self):
		print("Dog barks.")

	def feature(self):
		print("Dogs are furry. They come in different breeds. They are considered to be man's best friend.")

class Cat(Animal):
	def char(self):
		print("Cat", self.animal_char())

	def eats(self):
		print("Cat is a carnivore.")
		
	def sound(self):
		print("Cat meows.")

	def feature(self):
		print("Cats are furry. They come in different breeds. They are considered to be cunning.")

class Lion(Animal):
	def char(self):
		print("Lion", self.animal_char() + "It has a mane.")

	def eats(self):
		print("Lion is a carnivore.")
		
	def sound(self):
		print("Lion roars.")

	def feature(self):
		print("Lion is the King of the jungle.")
		
class Pig(Animal):
	def char(self):
		print("Pig", self.animal_char() + "It has hooves.")

	def eats(self):
		print("Pig is a herbivore.")
		
	def sound(self):
		print("Pig snorts.")

	def feature(self):
		print("Pigs live in mud. They are considered as pets in some countries.")

class Panda(Animal):
	def char(self):
		print("Panda", self.animal_char())

	def eats(self):
		print("Panda is a herbivore. It's favourite food is sugarcane.")
		
	def sound(self):
		print("Pandas make a variety of sounds like squeak, growl, huff etc.")

	def feature(self):
		print("Pandas are black and white in colour.")

class Horse(Animal):
	def char(self):
		print("Horse", self.animal_char())

	def eats(self):
		print("Horse is a herbivore.")
		
	def sound(self):
		print("Horse neighs.")

	def feature(self):
		print("Horses come in different breeds. They run very fast.")

class Cow(Animal):
	def char(self):
		print("Cow", self.animal_char())

	def eats(self):
		print("Cow is a herbivore.")
		
	def sound(self):
		print("Cow moos.")

	def feature(self):
		print("Cows give us milk. They are also used in agricultural activities.")
		
class Parrot(Animal):
	def char(self):
		print("Parrot", self.bird_char())

	def eats(self):
		print("Parrot is an omnivore.")
		
	def sound(self):
		print("Parrot squeaks or talks.")

	def feature(self):
		print("Parrots come in a variety of colours.")

class Penguin(Animal):
	def char(self):
		print("Penguin", self.bird_char())

	def eats(self):
		print("Penguin is a carnivore.")
		
	def sound(self):
		print("Penguins make a variety of sounds.")

	def feature(self):
		print("Penguins are flightless birds. They are black and white in colour.")
		
class Ostrich(Animal):
	def char(self):
		print("Ostrich", self.bird_char())

	def eats(self):
		print("Ostrich is an omnivore.")
		
	def sound(self):
		print("Ostriches make a variety of sounds like chirp, hiss, bark etc.")

	def feature(self):
		print("Ostriches are flightless birds. Their eggs are the largest of all eggs.")


animal1 = Lion()
animal1.char()
animal1.eats()
animal1.sound()
animal1.feature()
print("\n")

animal2 = Dog()
animal2.char()
animal2.eats()
animal2.sound()
animal2.feature()
print("\n")

bird1 = Parrot()
bird1.set_bird()
bird1.char()
bird1.eats()
bird1.sound()
bird1.feature()
# print(bird1.__beak)		Gives attribute error
# print(Animal.__beak)		Gives attribute error
# print(bird1._Animal__beak)	Another way to access a private variable
print("\n")

bird2 = Ostrich()
bird2.set_bird()
bird2.char()
bird2.eats()
bird2.sound()
bird2.feature()
print("\n")



# Shapes
class Shape(object):
	def __init__(self):
		self.geometric = True
		
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
		t.speed(1)
		
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
		t.speed(1)
		t.shape("turtle")
		
class Triangle(Shape):
	def __init__(self, a = 100, b = 100, c = 100):
		self.a = a
		self.b = b
		self.c = c
		
	def set(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		
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
			t.speed(1)
		else:
			print("Invalid triangle")

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
		t.speed(1)
		
class Rectangle(Shape):
	def __init__(self, l = 100, b = 200):
		self.l = l
		self.b = b
		
	def set(self, l, b):
		self.l = l
		self.b = b
		
	def get(self):
		return self.l, self.b
		
	def perimeter(self):
		print("Perimeter of rectangle with length = {} and breadth = {} is {}".format(self.l, self.b, 2 * (self.l + self.b)))
		
	def area(self):
		print("Area of rectangle with length = {} and breadth = {} is {}".format(self.l, self.b, self.l * self.b))
		
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
		t.speed(1)
		
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
		t.speed(1)
		
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
		t.speed(1)

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
		print("Perimeter of parallelogram with length = {} and breadth = {} is {}".format(self.l, self.b, 2 * (self.l + self.b)))
		
	def area(self):
		print("Area of parallelogram with length = {} and breadth = {} is {}".format(self.l, self.b, self.l * self.b))
		
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
		t.speed(1)
		
class Cube(Shape):
	def __init__(self, a = 100):
		self.a = a
		
	def set(self, a):
		self.a = a
		
	def get(self):
		return self.a
		
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
		t.speed(1)
		
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
		t.speed(1)
		
shape1 = Circle()
shape1.set(70)
shape1.perimeter()
shape1.area()
shape1.draw()
print("\n")

shape2 = Ellipse()
shape2.set(100,50)
shape2.perimeter()
shape2.area()
shape2.draw()
print("\n")

shape3 = Triangle()
shape3.set(100, 110, 140)
shape3.perimeter()
shape3.area()
shape3.draw()
print("\n")

shape4 = Square()
shape4.set(130)
shape4.perimeter()
shape4.area()
shape4.draw()
print("\n")

shape5 = Rectangle()
shape5.set(130, 100)
shape5.perimeter()
shape5.area()
shape5.draw()
print("\n")

shape6 = Parallelogram()
shape6.set(150, 100)
shape6.perimeter()
shape6.area()
shape6.draw()
print("\n")

shape7 = Pentagon()
shape7.set(130)
shape7.perimeter()
shape7.area()
shape7.draw()
print("\n")

shape8 = Hexagon()
shape8.set(130)
shape8.perimeter()
shape8.area()
shape8.draw()
print("\n")

shape9 = Cube()
shape9.set(130)
shape9.perimeter()
shape9.area()
shape9.volume()
shape9.draw()
print("\n")

shape10 = Cuboid()
shape10.set(150, 100, 200)
shape10.perimeter()
shape10.area()
shape10.volume()
shape10.draw()
