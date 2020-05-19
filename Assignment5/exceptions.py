'''To raise and handle exceptions.'''

import math

# FileNotFoundError
try:
	f = open("text.txt")
except FileNotFoundError:
	print("FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'")
else:
	for line in f:
		print(line)
finally:
	print("Finally is always executed.\n")

# If no exception
try:
	f = open("file.txt")
except FileNotFoundError:
	print("FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'")
else:
	for line in f:
		print(line)
finally:
	print("Finally is always executed.\n")
				
# Keyboard Interrupt Error
try:	
	print("Press Ctrl + C or Interrupt the kernel:")
	inp = input()
except KeyboardInterrupt:
	print("Caught KeyboardInterrupt!")
else:
	print("No exception occurred!")
finally:
	print("Finally is always executed.\n")
		
# Zero Division Error
try:
	a = 100/0
	print(a)
except ZeroDivisionError:
	print("ZeroDivisionError: division by zero")
else:
	print("Success, no error!")
finally:
	print("Finally is always executed.\n")
		
# OverFlow Error
try:
	print(math.exp(1000))
except OverflowError:
	print("OverFlow Exception raised")
else:
	print("Success, no error!")
finally:
	print("Finally is always executed.\n")
		
# Assertion Error
try:
	a = 100
	b = "Python"
	assert a == b
except AssertionError:
	print("Assertion Exception raised")
else:
	print("Success, no error!")
finally:
	print("Finally is always executed.\n")
		
# Attribute Error	
class Animal(object):
	print("Animal class")
	
try:
	animal = Animal()
	print(animal.eyes)
except AttributeError:
	print("AttributeError: 'Animal' object has no attribute 'eyes'")
else:
	print("Success, no error!")
finally:
	print("Finally is always executed.\n")
			
# KeyError	
try:
	d = {'Apples':3, 'Bananas':2, 'Mangoes':4}
	print(d['Oranges'])
except LookupError:
	print("KeyError: 'Oranges'")
else:
	print("Success, no error!")	
finally:
	print("Finally is always executed.\n")
		
# IndexError
try:
	l = [45, 68, 78, 65]
	print(l[6])
except LookupError:
	print("IndexError: list index out of range")
else:
	print("Success, no error!")
finally:
	print("Finally is always executed.\n")
		
# Name Error
try:
	print(python)
except NameError:
	print("NameError: name 'python' is not defined")
else:
	print("Success, no error!")
finally:
	print("Finally is always executed.\n")
		
# Type Error
try:
	a = 100
	b = "Python"
	c = a + b
except:
	print("TypeError: unsupported operand type(s) for +: 'int' and 'str'")
else:
	print("Success, no error!")	
finally:
	print("Finally is always executed.\n")
		
# ValueError
try:
	print(float("Python"))
except ValueError:
	print("ValueError: could not convert string to float: 'Python'")
else:
	print("Success, no error!")	
finally:
	print("Finally is always executed.\n")	
	
# Custom Exception
class InvalidValueError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
		
try:
	Age = int(input("Enter your age:"))
	if(Age < 0):
		raise InvalidValueError("Age can't be negative")
except InvalidValueError as i:
	print("InvalidValueError: ", i.value)
else:
	print("Your age is ", Age)
finally:
	print("Finally is always executed.")
	
	
	
	
	
