---
title: Modules and Testing
revealjs-url: ../../lib/reveal
theme: inst326
transition: slide
---

## Overview

::: columns

:::: column

**Structuring Python Programs**

:::: incremental
* Imports
* Modules
* Packages
::::

::::

:::: column

**Testing Python <br> Programs**

:::: incremental
* Why test?
* Building Tests with Assert
* Testing Packages
::::

::::

:::

::: notes
Today's lecture will have two parts. In order to understand testing, we first have to talk about Python's module and import system.
:::

# Modules

## Structuring Python Programs

::: left

The Python import system can be used for:

:::

::: incremental
1. Standard Library Modules
    * _Examples: sys, os, re, json, csv_
1. Installed Modules
    * _Examples: pandas, requests, lxml_
1. Your Own Modules
    * _Python files you create in the same directory_
:::

::: notes

As you'll recall, one principle of good program design is to avoid repeated code. Python facilitates code reuse through its import system.

To reuse code from another file, you can _import_ all or part of the file into your program.  Officially, files of python code are called _modules_.

As we have seen already, Python comes with "batteries included" meaning there is a wide variety of useful modules in the standard library that can be imported.  Other modules (for example requests) need to be installed with a package manager such as pip.

But how do you reuse code that you have written?  The answer is that you can import that code in much the same way. In fact, any python file in the same directory can be imported by name (minus the .py extension). Importing files from other places is a bit more complicated.

:::

## Import Examples

::: left

Import an entire module from the standard library:

:::

``` {.python .numberLines}
import random
x = random.randint(1,100)		
```

::: fragment
Note the namespacing: "random.randint()"
:::

## Import Examples 

::: left

Import one part of a module without namespacing:

:::

``` {.python .numberLines}
from random import randint
x = randint(1,100)	
```

::: fragment
The randint() function is now in top-level scope.
:::

::: notes
Be careful you don't unintentionally override a builtin function or class! There is no built-in randint function, but consider what might happen if you imported a function called print() this way.
::: 

## Import Examples

::: left

Import a function or class under a different name

:::

``` {.python .numberLines}
from random import randint as rand
x = rand(1,100)
```

::: fragment
"rand" becomes an alias for random.randint()
:::

## Import Examples

::: left

Modules outside the standard library must be installed:

:::

``` {.python .numberLines}
>>> import pandas
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'
```

::: fragment
Unless it is installed on your system, pandas is not available.
:::

## Import Examples

::: left

You can use pip/pip3 (Python Package Manager) to install non-standard modules.

:::

``` {.python .numberLines}
$ pip3 install pandas
Collecting pandas
... lots of lines ...
Installing collected packages: ...
Successfully installed ... pandas-0.23.4 ...
```

::: fragment
Anyone who wants to run your code must similarly install pandas. This is known as a _dependency_.
:::

::: notes
Python has tools for managing dependencies and making them easier for end-users to install. Such tools are outside the scope of this course.
:::

## Importing Your Own Modules

::: incremental
* Imports are not just for other people’s code
* As programs become complex, single-file programming gets impractical
* To facilitate reuse and make code easier to understand, divide large programs into modules
* Modules are just different .py files stored together
:::

## Importing Your Own Modules

::: left

Imagine you have a module called petshop.py that depends on pets.py, which includes two classes (Cat and Dog).

:::

``` {.python .numberLines}
import pets
c = pets.Cat('Fluffy')
d = pets.Dog('Spot')
```

::: fragment
By importing "pets", the classes in pets.py become available in petshop.py.
:::


## Python’s Search Path

::: left

During imports, Python searches the following:

:::

::: incremental
1. Home directory (where main script is located)
1. PYTHONPATH (environment variable)
1. Standard library (located inside your copy of Python)
1. Locations in a .pth file (a text file listing one directory per line)
:::

## Python Packages

::: incremental
* Modules can be grouped
* A group of modules in a directory is called a _package_
* To be recognized as a package, you must include a file named \_\_init\_\_.py
* To run a package, use the -m flag at runtime
:::

## Init Files

::: incremental
* This allows Python to recognize the directory as a package
* It can contain code but is not required to
* Because it is run at load time, it is used for initialization tasks
:::

# Testing

## Many Ways to Test

::: incremental
* Using shell tools
* Build your own tests using assert statements, try/except
* In "if name equals main"
* Using an external library: 
    1. [unittest](https://docs.python.org/3.7/library/unittest.html)
    1. [pytest](https://pytest.org)
:::

## Using Assert

::: incremental
* Assert is a means of declaring expected state
* Primary use case is for debugging
* Declares an expectation, and raises "AssertionError" if expectation is False
* Assert is designed to catch errors that would otherwise be missed
* There is no need to test for things that would raise an exception anyway
:::

## Using Assert

::: left

Imagine a function designed to draw a triangle. You can create an assert statement to check that the interior angles add up to 180°:

:::

``` {.python .numberLines}
assert sum(angles) == 180, 'angles must total 180'
```

::: fragment
assert len(angles) == 3, 'must have 3 angles'
:::

::: notes
Can you think of other assertions that could be made here?
:::

## Examples (assert)

``` {.python .numberLines}

def mysum(a, b):
    return a + b

assert mysum(2,2) == 4
assert mysum(2,3) == 6  
```

::: fragment
The second (incorrect) assertion raises an error
:::


## Using "If Name Equals Main"

::: incremental
* For modules to be imported, the main block can be used for tests
* Works only for modules not designed to be run by themselves
* Put tests in the "name equals main" block
* These tests will be ignored when the module is imported
* But they can conveniently be activated by running the module directly
:::


## Examples (Name Equals Main)

::: left

Imagine a function designed to evaluate whether or not a number is prime.

:::

``` {.python .numberLines}
def is_prime(x):
    # body of function here ...

if __name__ == "__main__":
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(4) == False 

```

::: notes

When you want to use this function, you import the entire module or just the one function from the module.

When you want to test your function, you run the modules directly, which causes the code in the if name equals main block to be executed.

:::


## Testing with pytest

::: incremental
* Works similarly to the use of asserts in if name equals main
* Works with modules intended for import as well as those intended to be run directly
* Define testing functions in the module named according to one of these patterns: 'test\_\*.py' or  '\*\_test.py'
:::


## Testing with pytest (continued)

::: incremental
* Will execute all such functions when run against a module or package
* Prints a detailed report of the results to the console
* Has advanced features, including integration with unittest
:::


## Examples (pytest)

``` {.python .numberLines}
def is_prime(x):
	if x == 2:
		return True
	else:
		for i in range(2,n):
			if x%i == 0:
				return False
		return True

def test_is_prime():
	assert is_prime(2) == True
	assert is_prime(7) == True
	assert is_prime(4) == False
```

::: notes

The function checks all integers between two and the number being evaluated, returning False as soon as the number divides evenly. Once all numbers have been checked, it returns True.

A second function named according to a pytest pattern checks two cases that are prime and one that is not. Good tests seek out "edge cases" to test.

:::


