from abc import ABC, abstractmethod

# Abstract base class as abstract methods as well as concrete methods are there
class Animal(ABC):
	def __init__(self):
		self.eyes = 2		
		self.ears = 2		
		self.mouth = 1		
		self.tail = 1		
		self.beak = 1		
		self.wings = 2	
	
	def animal_char(self):
		return ("has {} eyes, {} ears, {} mouth and {} tail. ".format(self.eyes, self.ears, self.mouth, self.tail))
		
	def bird_char(self):
		return ("has {} eyes, {} beak and {} wings. ".format(self.eyes, self.beak, self.wings))
	
	def eats(self):
		print("It is a herbivore.")
		
	@abstractmethod
	def char(self):
		pass
		
	@abstractmethod
	def sound(self):
		pass

# Interface as only abstract methods are there		
class Feature(ABC):
	@abstractmethod
	def feature(self):
		pass	

# Derived classes -->

class Dog(Animal, Feature):
	def char(self):
		print("Dog", self.animal_char())

	# Virtual function
	def eats(self):
		print("Dog is an omnivore.")
		
	def sound(self):
		print("Dog barks.")

	def feature(self):
		print("Dogs are furry. They come in different breeds. They are considered to be man's best friend.")

class Cat(Animal, Feature):
	def char(self):
		print("Cat", self.animal_char())
	
	# Virtual function
	def eats(self):
		print("It is a carnivore.")
		
	def sound(self):
		print("Cat meows.")

	def feature(self):
		print("Cats are furry. They come in different breeds. They are considered to be cunning.")

# Hierarchy
class Lion(Cat):
	def char(self):
		print("Lion", self.animal_char() + "It has a mane.")
		
	def sound(self):
		print("Lion roars.")

	def feature(self):
		print("Lion is the King of the jungle.")
		
class Pig(Animal, Feature):
	def char(self):
		print("Pig", self.animal_char() + "It has hooves.")
		
	def sound(self):
		print("Pig snorts.")

	def feature(self):
		print("Pigs live in mud. They are considered as pets in some countries.")

class Panda(Animal, Feature):
	def char(self):
		print("Panda", self.animal_char())

	# Virtual function
	def eats(self):
		super().eats()
		print("It's favourite food is sugarcane.")
		
	def sound(self):
		print("Pandas make a variety of sounds like squeak, growl, huff etc.")

	def feature(self):
		print("Pandas are black and white in colour.")

class Horse(Animal, Feature):
	def char(self):
		print("Horse", self.animal_char())
		
	def sound(self):
		print("Horse neighs.")

	def feature(self):
		print("Horses come in different breeds. They run very fast.")

class Cow(Animal, Feature):
	def char(self):
		print("Cow", self.animal_char())
		
	def sound(self):
		print("Cow moos.")

	def feature(self):
		print("Cows give us milk. They are also used in agricultural activities.")
		
class Parrot(Animal, Feature):
	def char(self):
		print("Parrot", self.bird_char())

	def eats(self):
		print("Parrot is an omnivore.")
		
	def sound(self):
		print("Parrot squeaks or talks.")

	def feature(self):
		print("Parrots come in a variety of colours.")

class Penguin(Animal, Feature):
	def char(self):
		print("Penguin", self.bird_char())

	def eats(self):
		print("Penguin is a carnivore.")
		
	def sound(self):
		print("Penguins make a variety of sounds.")

	def feature(self):
		print("Penguins are flightless birds. They are black and white in colour.")
		
class Ostrich(Animal, Feature):
	def char(self):
		print("Ostrich", self.bird_char())

	def eats(self):
		print("Ostrich is an omnivore.")
		
	def sound(self):
		print("Ostriches make a variety of sounds like chirp, hiss, bark etc.")

	def feature(self):
		print("Ostriches are flightless birds. Their eggs are the largest of all eggs.")



