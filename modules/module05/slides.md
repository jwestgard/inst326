---
title: "Object-Oriented Programming"
subtitle: "Combining Data and Behavior"
revealjs-url: ../../lib/reveal
theme: inst326
transition: slide
---

#

<a href="https://commons.wikimedia.org/wiki/File:Geely_assembly_line_in_Beilun,_Ningbo.JPG">
  <img style="width: 80%" src="images/assemblyline.jpg">
</a>

::: notes

A good analogy for OOP is an assembly line, where many instances of a model of
car are built. The individual cars may have different options, but share a
common core set of features and means of operation.

:::

#

What are some common properties of cars?

::: incremental

* color
* wheels
* seats
* steering wheel
* engine
* doors
* accelerator
* brake

:::

#

What are some actions you can perform?

::: incremental

* open door
* start engine
* turn left/right
* accelerate
* stop
* turn off engine
* turn on cruise control

:::

#

## Overview

- Definitions
- Defining Classes
- Using Instances

::: notes

- after some general intro to OOP
- we'll talk about classes vs. instances and how to define a class
- we'll look at attributes (data) and methods (behaviors)
- we'll talk about how methods and attributes are accessed (dot notation), and how objects can interact with each other
- finally, we'll look at how a hierarchy of classes (inheritance) can be used

:::

#

## What is OOP?

::: incremental

- Nothing magical, just a different style
- Procedural (like a recipe)
- Functional (more mathematical)
- Many languages like Python combine these styles.
- OOP *encapsulates* data and behavior into *objects*
- Objects have interfaces that allow them to interact
- OOP tries to map programming to how we think about the world.

:::

#

## Classes vs. instances

::: incremental

- Objects in OOP are members of *classes*
- Features shared by members are mapped in a class definition
- Individual *instances* have their own attributes and state

:::

#

## You have already been using objects

- All data types (for example, string, list, dictionary) are objects

``` {.python .numberLines}
>>> s = 'Hello World'
>>> type(s)
<class 'str'>
>>> l = list()
>>> type(l)
<class 'list'>
>>> dir(l)
['__add__', '__class__', ...]
```

#

## In fact, in Python almost everything is an object

::: incremental

- Objects have shared behaviors defined by their classes
- At the same time, individual instances have different content
- Much of the complexity is "hidden" inside the objects

:::

#

## Defining your own class

- Define a class with the "class" keyword
- Define methods inside the class with indented "def" blocks

``` {.python .numberLines}
class Pet():
    def __init__(self, name):
        self.name = name
```

#

## Initializers

::: incremental

- The \_\_init\_\_() method is an initializer
- The double underscore (dunderscore) indicates that \_\_init\_\_ has a special purpose
- It is called automatically when a new instance is created
- Often \_\_init\_\_() is used to set up attributes (here to give each pet a name)

:::

#

## Attributes and methods

- Attributes are properties specific to the instance
- Methods are like functions defining behaviors specific to the members of a class

``` {.python .numberLines}
class Pet():
    def __init__(self, name):
        self.name = name
    def eat(self):
        print('Nom nom nom')
```

#

## Interacting with an object

``` {.python .numberLines .smaller}
class Pet():
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print(f'Nom nom. {self.name} likes {food}.')

>>> mypet = Pet('Spot')
>>> mypet.eat('dogfood')
Nom nom. Spot likes dogfood.
```

::: notes

- The 'self' is a special variable that refers to the instance
- The name self is just a convention
- Being the first parameter is what grants it a special function

:::

#

## Dot notation

::: incremental

- Notice in the previous example how eat() was called
- Notice as well how the attribute ".name" was accessed
- This is called dot notation
    - used to access attributes of the *instance*
    - used to apply methods to the *instance*
    - "self" in the class definition means particular to the *instance*

:::

#

## In summary

::: notes

This probably seems like a lot, but once you get the hang of it basic OOP can seem natural and intuitive.

:::

- Combining Data and Behavior
- Defining Classes
- Attributes and Methods
- Interacting with Instances
- [Exercise](exercise.html)
