---
title: Python Data Structures
subtitle: Strings, Lists, Dictionaries, Tuples
revealjs-url: ../../lib/reveal
theme: inst326
transition: slide
---

## From atoms to molecules

::: incremental

* We have already introduced some of the basic building blocks of data (integers, floats, booleans, strings)
* Python also supports combining bits of data into larger _data structures_
* You can think of the building blocks as atoms and the structures as molecules

:::

---

## Strings again?

::: incremental

* We discussed strings already, but they are so important that we'll talk about them some more today
* Strings have something in common with both atomic bits of data and larger data structures

:::

---

## Everything is an object

::: incremental

* Under the hood, all of these data types are objects 
* This means that they share some fundamental characteristics _and_
* You can use some common commands to learn about them:
  * type(): _returns an object's class_
  * dir(): _returns list of available methods_
  * help(): _opens built-in documentation pages_

:::

---

## Try it out (interactive mode)

:::

``` {.python}
>>> s = "To be or not to be."
>>> type(s)
<class 'str'>
>>> help(s)
...
>>> dir(s)
...
```

:::

---

# Strings

---

## What are strings?


::: incremental

* Strings are textual data
* Strings are ordered sequences of characters
* The characters that make up a string are mapped or ["encoded"](https://en.wikipedia.org/wiki/Character_encoding) in a particular character set
* In Python (starting with v3), strings are encoded by default in [unicode](https://unicode.org), which means there is automatic support for any writing system (well, _almost_ any...)

:::

---

## Creating strings

``` {.python .numberLines}
s = "To be or not to be"
```

::: incremental

* We create strings using quotation marks
* You can use single (\') or double (") quotes
* You cannot _mix_ single/double quotes when creating a string, but you can _nest_ them (useful if you need to make quotation marks part of a string)

:::

---

## Accessing strings

::: incremental

* Strings are sequences of characters
* By default the variable returns the whole sequence
* Parts of strings (called substrings) are accessed by index
* The first position of a string has an offset of zero

:::

::: fragment

``` {.python}
>>> x = 'To be or not to be.'
>>> x[3]
```

:::

::: fragment
**b**
:::

---

## String indices and slices

* The index is an integer representing the distance (offset) from the beginning of the string
* Sequences can be accessed by slicing (beginning and end separated by colon)

```python
>>> lyric = "Another one bites the dust."
>>> lyric[12:17]
```

::: fragment
**bites**
:::

---

## "Modifying" strings

::: incremental

* Strings are _immutable_ which means they do not change.
* However it's common to reassign a string variable.

:::

::: fragment

``` {.python .numberLines}
>>> x = 'hello'
>>> x = x.upper()  # reassigns x 
>>> print(x)
```

:::

::: fragment
**HELLO**
:::

---

## String Methods

::: left

[Strings](https://docs.python.org/3/library/string.html) have lots of useful
methods like *upper()* which you just saw.  Here are a few more, but try using
*dir* and *help* to learn about them.

:::

::: columns

:::: column 

* lower()
* upper()
* split(s)
* join(words)

::::

* capitalize()
* replace(old, new)
* find(s)
* format(args)

:::: column

::::

:::

---

# Lists

---

## What are lists?

::: incremental

* Lists are ordered sequences of other objects
* Lists are what are called "arrays" in some other languages
* Lists can be nested (e.g. a list of lists, or a list of dictionaries)
* Lists can be made up of heterogenous elements

:::

---

## Creating lists

::: incremental

* Create a list with list() or with square brackets (empty or not)
  * x = list()
  * x = []
  * x = ['hello', 'world']
* Notice how the items of a list are separated by commas

:::

---

## Accessing lists

::: incremental

* Like strings, lists are an ordered sequence
* Like strings, elements can be accessed by index position: `my_list[2]`
* Like strings, lists can be sliced: `my_list[2:5]`
* Use **len()** to find out how many elements are in a list: `len(my_list)`

:::

---

## Loops and Lists

And the **for loop** is super handy for operating on lists:

``` {.python .numberLines}
colors = ["red", "green", "blue", "black"]
for color in colors:
    print(color)
```

::: fragment

```
red
green
blue
black
```

:::

---

## Modifying lists


::: incremental

* Unlike strings, lists can be changed in place
* You can reassign the item at a particular position

:::

::: fragment

``` {.python .numberLines}
x = ['hello', 'world']
x[1] = 'universe'
print(x)
```

:::

::: fragment
**['hello', 'universe']**
:::

---

## Exercise!

---

# Dictionaries

---

## What are dictionaries?

::: incremental

* Dictionaries are _unordered_ collections of key/value pairs
* They are what is referred to in other languages as an "associative array"
* They are similar to a phone book or real-life dictionary, except that the keys are not sorted by default

:::

---

## Creating dictionaries

::: incremental

* Create a dictionary with dict() or with curly braces (empty or not)
  * my\_dictionary = dict()
  * d = {}
  * phone_book = {'Bruce Banner': '555-555-1234', 'Sue Storm': '555-555-5678'}
* Notice how the keys and values are delimited by a colon
* And how the key/value pairs are separated by commas

:::

---

## Accessing dictionaries

::: incremental

* You can look up the values in a dictionary by referencing the key

:::

::: fragment

``` {.python .numberLines}
>>> phone_book['Bruce Banner']
555-555-1234
```
:::

::: incremental

* But the contents of the dictionary are **not** ordered
* If you iterate over a dictionary using a for loop, you get the keys, but not in a particular order

:::

---

## Accessing dictionaries

::: incremental

* You can access the keys of a dictionary with .keys()
* You can access the values of a dictionary with .values()
* Or, you can access all the key/value pairs with .items()
* In this last case, the pairs come back as tuples

:::

---
## Modifying dictionaries

::: incremental

* The keys of a dictionary can be assigned to different values directly

::: fragment

``` {.python .numberLines}
>>> phone_book['Bruce Banner'] = "555-555-9876"
```

:::

* If the key does not exist, a new key/value pair will be added
* Note that each key of a given dictionary must be unique

:::

---

# Tuples

---

## What are tuples?

::: incremental

* Tuples are ordered, immutable sequences of other objects
* You will hear tuple pronounced both "too-pull" and "tuh-pull"
* Contrary to how the name sounds, tuples can have any number of elements (not just two!)

:::

---

## Creating tuples

::: incremental

* Tuples can be created with tuple()
* Tuples are also often created with parentheses
  - x = ('foo', 'bar')
* But in fact, the comma is what allows python to recognize the tuple

:::

---

## Accessing tuples

::: incremental

* Similar to lists, the items in a tuple are accessed by index position
* A common pattern is to assign the elements of tuples in a single line
* For example, the .values() method of dictionaries returns key/value pairs as a tuple:

:::

::: fragment

``` {.python .numberLines}
for name, number in phone_book.items():
    print(name, number)
```

:::

---

## "Modifying" tuples

::: incremental

* Like strings, tuples are immutable
* If you try to reassign a value inside a tuple, Python will raise a type error

:::

---

# Exercise!

