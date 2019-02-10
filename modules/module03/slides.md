---
title: Python Data Structures
subtitle: Strings, Lists, Dictionaries, Tuples
revealjs-url: ../../lib/reveal
theme: inst326
transition: slide
---

## From atoms to molecules

::: incremental

* We have already introduced some of the basic building blocks of data (integers, floats, Booleans, strings)
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

``` {.python}
>>> foo = list()
>>> type(foo)
...
>>> dir(foo)
...
>>> help(list)
... 
```

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
>>> x = 'Hello'
>>> x[0]
H
```

:::

---

## String indices and slices

* The index is an integer representing the distance (offset) from the beginning of the string
* Sequences can be accessed by slicing (beginning and end separated by colon)
* Leaving one of the slice markers blank will default to beginning or end, respectively

---

## "Modifying" strings

::: incremental

* Strings are _immutable_ which means they do not change
* In practice, what seems like changing a string is usually just reassigning the variable to a new copy of the string with changes applied

:::

::: fragment

``` {.python .numberLines}
x = 'hello'
x = x.upper()  # reassigns x 
print(x)
```

:::

::: fragment
"HELLO" is a new string, and the original "hello" has not changed (though it may no longer be reference by any variable).
:::

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
* Like strings, elements can be accessed by index position
* Like strings, lists can be sliced
* Use len() to find out how many elements are in a list

:::

---

## Modifying lists


::: incremental

* Unlike strings, lists can be changed in place
* You can reassign the item at a particular position

``` {.python .numberLines}
x = ['hello', 'world']
x[1] = 'universe'
print(x)
['hello', 'universe']
```

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
  * x = dict()
  * x = {}
  * x = {'Bruce Banner': '555-555-1234', 'Sue Storm': '555-555-5678'}
* Notice how the keys and values are delimited by a colon
* And how the key/value pairs are separated by commas

:::

---

## Accessing dictionaries

::: incremental

* 

:::

---

## "Modifying" dictionaries

::: incremental

* 

:::


# Tuples

::: incremental

* 

:::

---

## What are tuples?

::: incremental

* 

:::

---

## Creating tuples

::: incremental

* 

:::

---

## Accessing tuples

::: incremental

* 

:::

---

## "Modifying" tuples

::: incremental

* 

:::

---

# Questions?

