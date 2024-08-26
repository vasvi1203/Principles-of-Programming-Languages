# PPL Assignments
### Name: Vasvi Gupta
### MIS: 111803128
### Division: 2
### [Project link](https://github.com/vasvi1203/Project-EVA)
The questions are written in the form of comments in all the programs. All Python programs are written in Python 3.
#### ***Assignment 1***
1. To run any program, execute the command: `python <filename>` or `python3 <filename>` except for `<3_block.py>`
2. To run `3_block.py` on Windows, run cmd or Windows Powershell as administrator and then python `3_block.py`.
3. To run `3_block.py` on Linux, change `hosts_path` to `/etc/hosts` and run as `sudo python 3_block.py` or `sudo python3 3_block.py`.
4. Definitions of some terms:
   - __Amicable numbers:__ A pair of numbers, each of which is the sum of the factors of the other.
   - __Armstrong numbers:__ It is a number equal to the sum of cubes of its digits.
   - __LU Decomposition:__ Let A be a square matrix. An LU factorization refers to the factorization of A, with proper row and/or column orderings or permutations, into two factors, a lower triangular matrix L and an upper triangular matrix U, A=LU.
   - __Harmonic divisor numbers:__  They are positive integers whose divisors have an integer harmonic value.
  
#### ***Assignment 2***
1. To run `recursion.c`, execute the command: `gcc factorial.c` and then `./a.out` on Linux
2. To run `smashing.c`, execute the command: `gcc recursive.c -fno-stack-protector` and then `./a.out` on Linux
2. PDFs of Stack Frames of respective programs are attached [here](https://github.com/vasvi1203/PPL/tree/master/Assignment2).

#### ***Assignment 3***
1. To run the program, execute the command: `python animals_shapes.py` or `python3 animals_shapes.py`
2. Definitions of some terms:
   - __Abstraction:__ It is about hiding unwanted details while giving out the most essential details. For example, the `class Animal()` has different methods in this program. The person executing the code will only know the names of the methods but not how they are implemented.
   - __Encapsulation:__ This means hiding the code and data in a single unit. For e.g. all the different methods are encapsulated in the `class Animal()`
   - __Public access specifier:__ All class data members and member functions are public by default. Public access specifiers are shown in `animals_shapes.py`
   - __Private access specifier:__ Private access specifiers are declared by adding a double underscore ‘__’ symbol before the data member of that class. They are accessible within the class only.
   
#### ***Assignment 4***
1. To run the program, execute the command: `python main.py` or `python3 main.py`
2. Definitions of some terms:
   - __Virtual functions:__ They are overridable functions. For e.g., in the `animals.py` file, the `def eats()` method in the `class Dog()` is a virtual function as it overwrites the default `def eats()` method in `class Animal()`
   - __Abstract class:__ It is a collection of some abstract methods as well as some concrete methods. For e.g., in the `shapes.py` file, `class Shape()` is an abstract class.
   - __Base class:__ It is the class from which it is inherited. For e.g., in the `shapes.py` file, `class Shape()` is a base class.
   - __Derived class:__ It is the class that inherits from another class. For e.g., in the `shapes.py` file, `class Ellipse()` is derived.
   - __Interface:__ It is a collection of only abstract methods. For e.g., in the `shapes.py` file, `class Instance()` is an interface.
   - __Polymorphism:__ It allows us to define methods in the derived class with the same name as defined in their base class. 
   - __Modularity:__ It is the process of decomposing a program into a set of modules. For eg. in this assignment, `animals.py` and `shapes.py` are modules that are imported into `main.py`
   - __Hierarchy:__ When more than one derived class is created from a single base, it is said to form a hierarchy, explained in the following example. For eg. in the `animals.py` file, all the derived classes are created from a single base class, i.e., the `class Animal`. Hence, there exists a hierarchy.

#### ***Assignment 5***
1. To run the program, execute the command: `python exceptions.py` or `python3 exceptions.py`
2. Different types of exceptions are demonstrated in this assignment.
3. Definitions of some terms:
   - __try:__ It will run the code block in which you expect an error to occur.
   - __except:__ The type of exception we expect in the try block (built-in or custom) is defined here.
   - __else:__  If there isn't any exception, then this code block will be executed.
   - __finally:__ Irrespective of whether there is an exception or not, this block of code will always be executed.
   
#### ***Assignment 6***
![here](https://github.com/vasvi1203/PPL/blob/master/Assignment6/Example.png)
1. Execute the following commands on Windows to install the required modules:
   - `pip install tkinter`(for python 3) or `pip install Tkinter`(for python 2)
   - `pip install pillow`
2. To run the program, execute the command: `python paint.py` or `python3 paint.py` on Windows.

#### ***Assignment 7***
1. To run the program, execute the command: `clisp <filename>` on Linux
2. PDFs of Memory layout diagrams of respective programs are attached [here](https://github.com/vasvi1203/PPL/tree/master/Assignment7).

#### ***Assignment 8***
1. To run the program, execute the command: `gprolog` on Linux and then execute the following steps in the prolog prompt:
   ```
   [flight].
   a(toronto,madrid).
   b(A,B,C,D,E). (with A and B as any 2 cities)
   c(toronto,paris).
   d(A,B,C,D,E). (with A and B as any 2 cities)
   e(A,B). (with A and B as any 2 cities)
   ```
3. Prolog program components:
      There are two types of clauses in the prolog database:
         - __Facts:__ A fact is a single piece of information. For eg. in this program, `route(toronto,london,'Air Canada',500,'360m').` is a fact telling that there is a route from Toronto to London via flight "Air Canada" whose fare is $500 and the journey time is 360 minutes.
         - __Rules:__ They generate new information from facts, other rules, and even themselves. For e.g. in this program, `flight(A,B,C,D,E) :- route(A,B,C,D,E).` is a rule generating all the flights on various routes.
  
#### ***Assignment 9***
1. To run the programs, execute the command: `gcc <filename> -lpthread` and then `./a.out` on Linux
2. The concept of threading is implemented in this assignment.
3. An array of size 3 and present time is taken for `clock.c`, and mutex lock is used for the critical sections.
