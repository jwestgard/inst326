INST 326:Modules and Testing
Joshua A. Westgard • 2018-10-08
UMD College of Information Studies


Overview
Structuring Python Programs
Imports
Modules
Packages

Testing Python Programs
Why test?
Building Tests with Assert
Testing Packages

Structuring Python Programs

Import statements
Standard Library Modules
Random, sys, os, re, json, csv
Installed Modules
	Pandas, numpy, lxml
Your Own Modules
	Python files that you create in the same directory


Import Examples (standard library)
# import entire module
import random
x = random.randint(1,100)		# randint() function is namespaced


# import select pieces of a module into top level
from random import randint
x = randint(1,100)			# randint() is now in top-level scope


# import module function under a different name
from random import randint as rand
x = rand(1,100)				# rand() is like an alias for random.randint()


Import Examples (installed modules)
# Modules outside of the standard library must be installed
import pandas
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'


# Install additional modules with pip/pip3 (Python Package Manager)
$ pip3 install pandas
Collecting pandas
... lots of lines ...  # pip will locate and install dependencies
  Installing collected packages: numpy, pytz, python-dateutil, pandas
Successfully installed numpy-1.15.2 pandas-0.23.4 python-dateutil-2.7.3 pytz-2018.5


Importing Your Own Modules
Imports are not just for other people’s code
Python programs become complex, making single-file programming impractical
Dividing code into modules (i.e. different files) facilitates code re-use
Your modules can be imported when needed by the main (top-level) script
Import the name of the file (but dropping the .py)

Python’s Search Path
Python searches for modules in the following locations:
Home directory (where main script is located, current dir in interactive mode)
PYTHONPATH (environment variable)
Standard library directories (located in Python installation)
.pth file directories
text file listing additional directories to search, one per line

Import Examples (your own modules)
# Create your own module, in a file called mymodule.py
def square(x):
	return x ** 2

# In interactive mode, import the square function from this module>>> import mymodule
>>> help(mymodule)				# help screen shows one function

# Call the function
>>> mymodule.square(10)
100								# function returns the square of 10

# Importing the function to global scope
>>> from mymodule import square	# function can be called directly
>>> square(2)
4

Python Packages
Modules can be grouped
A Python package is a group of modules in a directory
In order for Python to recognize a directory as a package,you must include a file named __init__.py in the directory
__init__.py can contain code but is not required to
Code it does contain is run then the package is first loaded, so it is useful for initialization tasks

Testing Python Programs

Testing Overview
There are many ways to test
Using shell tools
Build your own tests using assert statements, try/except
Leverage the if name equals main program structure
Use an external library: 
unittest (https://docs.python.org/3.7/library/unittest.html)
pytest (https://pytest.org)

Assert
Assert is a means of declaring expected state
Primary use case is for debugging
Declares an expectation, and raises “AssertionError” if expectation is False
Assert is designed to catch errors that would otherwise be missed
There is no need to test for things that would raise an exception anyway

Testing Examples (assert)
# imagine a function designed to draw a triangle
# the function has three parameters representing the interior angles

def draw_triangle(angle1, angle2, angle3):
	assert angle1 + angle2 + angle3 == 180, ‘angles must add up to 180°’
	# draw side1
	# turn angle1 degrees
	# draw side2
	# turn angle2 degrees
	# etc.

# another example, try it out
def mysum(a, b):
	return a + b
assert mysum(2,2) == 4
assert mysum(2,3) == 6  # incorrect assertion should raise error

Placing Tests in “If Name Equals Main”
For modules to be imported, the main block can be used for tests
This obviously works only for modules not designed to be run by themselves
Put tests in the “if __name__ == ‘__main__’:” block
These tests will be ignored when the module is imported
But they can conveniently be activated by running the module directly

Testing Examples (if name equals main)
# Create a new module with one function “is_prime” 

def is_prime(x):
	‘’’Return True if x is a prime number, else return False’’’
	pass


# add tests in the form of asserts to the if name equals main block

if __name__ == “__main__”:
	assert is_prime(2) == True
	assert is_prime(7) == True
	assert is_prime(4) == False

pytest
Works similarly to the use of asserts in if name equals main
Works with modules intended for import as well as those intended to be run directly
Allows you to define functions in the module named
test_*.py
*_test.py
Will execute all such functions when run against a module or an entire package
Returns detailed report of results to console
Has many advanced features, including integration with unittest

Testing Examples (pytest)
# Think back to the is_prime() example

def is_prime(x):
	if x == 2:
		return True
	else:
		for i in range(2,n):
			if x%i == 0:
				return False
		return True

# define tests as follows

def test_is_prime():
	assert is_prime(2) == True
	assert is_prime(7) == True
	assert is_prime(4) == False

Practice Exercises
Install pandas, numpy, or lxml using pip
Write a script to import getMarylandTax() and pass it input values read from a CSV 
Write tests for getMarylandTax() with assert statements
Do some TDD with pytest: write a failing test, then code the solution
