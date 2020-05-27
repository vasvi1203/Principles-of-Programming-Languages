# PPL Assignments
### Name : Vasvi Gupta
### MIS : 111803128
### Division : 2
### [Project link](https://github.com/vasusharma7/Project-EVA)
The questions are written in the form of comments in all the programs. All python programs are written in python 3.
#### ***Assignment 1***
1. To run any program, execute the command : 
'''python _filename_ or python3 _filename_ except for _3_block.py_'''
2. To run _3_block.py_ on windows, run cmd or windows powershell as administrator and then python _3_block.py_.
3. To run _3_block.py_ on linux, change hosts_path to "/etc/hosts" and run as sudo python _3_block.py_ or sudo python3 _3_block.py_.
4. Definitions of some terms:
   - Amicable numbers : A pair of numbers, each of which is the sum of the factors of the other.
   - Armstrong numbers : It is a number that is equal to the sum of cubes of its digits.
   - LU Decomposition : Let A be a square matrix. An LU factorization refers to the factorization of A, with proper row and/or column orderings or permutations, into two factors, a lower triangular matrix L and an upper triangular matrix U, A=LU.
   - Harmonic divisor numbers :  They are positive integers whose divisors have a integer harmonic value.
  
#### ***Assignment 2***
1. To run _recursion.c_, execute the command : gcc factorial.c and then ./a.out on linux
2. To run _smashing.c_, execute the command : gcc recursive.c -fno-stack-protector and then ./a.out on linux
2. Pdfs of Stack Frames of respective programs are attached [here](https://github.com/vasvi1203/PPL/tree/master/Assignment2).

#### ***Assignment 3***
1. To run the program, execute the command : python animals_shapes.py or python3 animals_shapes.py
2. Definitions of some terms:
   - Abstraction : It is about hiding unwanted details while giving out most essential details. For eg. in this program, the _class Animal()_ has different methods. The person executing the code will only know the names of the methods but not how they are implemented.
   - Encapsulation : It means hiding the code and data into a single unit. For eg. all the different methods are encapsulated in the _class Animal()_ 
   - Public access specifier : All data members and member functions of a class are public by default. Public access specifiers are shown in animals_shapes.py
   - Private access specifier : Private access specifiers are declared by adding a double underscore ‘__’ symbol before the data member of that class. They are accessible within the class only.
   
#### ***Assignment 4***
1. To run the program, execute the command : python main.py or python3 main.py
2. Definitions of some terms:
   - Virtual functions : They are overridable functions. For eg. in the _animals.py_ file, the _def eats()_ method in the _class Dog()_ is a virtual function as it overwrites the default _def eats()_ method in _class Animal()_
   - Abstract class : It is a collection of some abstract methods as well as some concrete methods. For eg. in the _shapes.py_ file, _class Shape()_ is an abstract class.
   - Base class : It is the class being inherited from. For eg. in the _shapes.py_ file, _class Shape()_ is a base class.
   - Derived class : It is the class that inherits from another class. For eg. in the _shapes.py_ file, _class Ellipse()_ is a derived class.
   - Interface : It is a collection of only abstract methods. For eg. in the _shapes.py_ file, _class Instance()_ is an interface.
   - Polymorphism : It allows us to define methods in the derived class with the same name as defined in their base class. 
   - Modularity : It is the process of decomposing a program into a set of modules. For eg. in this assignment, _animals.py_ and _shapes.py_ are modules which are imported into _main.py_
   - Hierarchy : There exists a hierarchy relationship between classes which is explained through the following example. For eg. in the _animals.py_ file, _class Lion()_ inherits from _class Cat()_ which in turn inherits from _class Animal()_. Hence, there exists a hierarchial relationship between the three classes.

#### ***Assignment 5***
1. To run the program, execute the command : python exceptions.py or python3 exceptions.py
2. Different types of exceptions are demonstrated in this assignment.
3. Definitions of some terms:
   - try : It will run the code block in which you expect an error to occur.
   - except : The type of exception we expect in the try block (built-in or custom) is defined here.
   - else :  If there isn't any exception, then this block of code will be executed.
   - finally : Irrespective of whether there is an exception or not, this block of code will always be executed.
   
#### ***Assignment 6***
1. Execute the following commands on windows to install the required modules:
   - _pip install tkinter_(for python 3) or _pip install Tkinter_(for python 2)
   - _pip install pillow_
2. To run the program, execute the command : python paint.py or python3 paint.py on windows.
3. A screenshot of the application is attached [here](https://github.com/vasvi1203/PPL/blob/master/Assignment6/Example.png).

#### ***Assignment 7***
1. To run the program, execute the command : clisp _filename_ on linux
2. Pdfs of Memory layout diagrams of respective programs are attached [here](https://github.com/vasvi1203/PPL/tree/master/Assignment7).

#### ***Assignment 8***
1. To run the program, execute the command : gprolog on linux and then execute the following steps in the prolog prompt:
   - [flight].
   - a(toronto,madrid).
   - b(A,B,C,D,E). with A and B as any 2 cities
   - c(toronto,paris).
   - d(A,B,C,D,E). with A and B as any 2 cities
   - e(A,B). with A and B as any 2 cities
2. Prolog program components:
      There are two types of clauses in the prolog database:
         - Facts : A fact is a single piece of information. For eg. in this program, _route(toronto,london,'Air Canada',500,'360m')._ is a fact telling that there is a route from Toronto to London via flight "Air Canada" whose fare is $500 and the journey time is 360 minutes.
         - Rules :  They are used to generate new information from facts, other rules, and even themselves. For eg. in this program, _flight(A,B,C,D,E) :- route(A,B,C,D,E)._ is a rule generating all the flights on various routes.
  
#### ***Assignment 9***
1. To run the programs, execute the command : gcc _filename_ -lpthread and then ./a.out on linux
2. The concept of threading is implemented in this assignment.
3. An array of size 3 and present time is taken for _clock.c_ and mutex lock is used for the critical sections.
