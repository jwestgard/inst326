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

## Testing


