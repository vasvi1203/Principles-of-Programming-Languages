# PPL Assignments
### Name : Vasvi Gupta
### MIS : 111803128
### Division : 2

The questions are written in the form of comments in all the programs. All python programs are written in python 3.
#### ***Assignment 1***
1. To run any program, execute the command : python _filename_ or python3 _filename_
2. Definitions of some terms:
   - Amicable numbers : A pair of numbers, each of which is the sum of the factors of the other.
   - Armstrong numbers : It is a number that is equal to the sum of cubes of its digits.
   - LU Decomposition : Let A be a square matrix. An LU factorization refers to the factorization of A, with proper row and/or column orderings or permutations, into two factors, a lower triangular matrix L and an upper triangular matrix U, A=LU.
   - Harmonic divisor numbers :  They are positive integers whose divisors have a integer harmonic value.
  
#### ***Assignment 2***


#### ***Assignment 3***
1. To run the program, execute the command : python animals_shapes.py or python3 animals_shapes.py
2. Definitions of some terms:
   - Abstraction : It is about hiding unwanted details while giving out most essential details. For eg. in this program, the _class Animal()_ has different methods. The person executing the code will only know the names of the methods but not how they are implemented.
   - Encapsulation : It means hiding the code and data into a single unit. For eg. all the different methods are encapsulated in the _class Animal()_ 
   - Public access specifier : All data members and member functions of a class are public by default. Public access specifiers are shown in animals_shapes.py
   - Private access specifier : Private access specifiers are declared by adding a double underscore ‘__’ symbol before the data member of that class. They are accessible within the class only.
   
#### ***Assignment 4***
1. To run the program, execute the command : python animals_shapes.py or python3 main.py
2. Definitions of some terms:
   - Virtual functions : They are overridable functions. For eg. in the _animals.py_ file, the _def eats()_ method in the _class Dog()_ is a virtual function as it overwrites the default _def eats()_ method in _class Animal()_
   - Abstract class : It is a collection of some abstract methods as well as some concrete methods. For eg. in the _shapes.py_ file, _class Shapes()_ is an abstract class.
   - Base class : It is the class being inherited from. For eg. in the _shapes.py_ file, _class Shapes()_ is a base class.
   - Derived class : It is the class that inherits from another class. For eg. in the _shapes.py_ file, _class Ellipse()_ is a derived class.
   - Interface : It is a collection of only abstract methods. For eg. in the _shapes.py_ file, _class Instance()_ is an interface.
   - Polymorphism : It allows us to define methods in the derived class with the same name as defined in their base class. 
   - Modularity : It is the process of decomposing a program into a set of modules. For eg. in this assignment, _animals.py_ and _shapes.py_ are modules which are imported into _main.py_
   - Hierarchy : There exists a hierarchy relationship between classes which is explained through the following example. For eg. in the _animals.py_ file, _class Lion()_ inherits from _class Cat()_ which in turn inherits from _class Animal()_. Hence, there exists a hierarchial relationship between the three classes.
