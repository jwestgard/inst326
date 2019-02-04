---
title: Loops & Iteration
subtitle: Programming Repeated Steps
revealjs-url: ../../lib/reveal
theme: inst326
transition: slide
---

# Loops

::: columns 

:::: {.column .left}

Python programs are made up of a series of **statements** that execute in order.

**Loops** allow you to repeat a set of statements while a particular
**expression** evaluates to **True**.

::::

:::: column

<img src="images/loop.jpg">

::::

:::


# Why Loops? 

::: left

Imagine you want to print all the positive integers less than 10. You wouldn't really want to do this:

:::

``` {.python .numberLines}
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
```

# While Loops

::: left

Instead you could use a **while loop** with a **variable** counter. This is very
useful if you want to print all the positive integers less than 1 million...

:::

``` {.python .numberLines}
i = 0
while i < 1000000:
    i += 1
    print(i)
```

#

::: left

### iterate, v.

1. *transitive.* To do (something) over again; to perform (an action) a second
   time, or reproduce (an effect); to repeat; to renew. Now rare.
2. To say, mention, or assert again or repeatedly; to repeat.
3. To make double or twofold; to duplicate. Obsolete. rare.
4. *intransitive. Mathematics.* To employ iteration; to make repeated use of a
   formula by substituting in it each time the result of the previous
   application.

:::


# For Loops

::: left
The **for loop** lets you to **iterate** through a series of values. We'll be
learning more about **lists** in Module 3.
:::

``` {.python .lineNumbers}
for day in ["Sun", "Mon", "Tue", "Wed", "Thu", 
            "Fri", "Sat"]:
    print(day)
```

# Loops In Loops

Imagine you want to print all possible combinations of two lists of numbers.

``` {.python .numberLines}
list1 = [1, 5, 9, 21, 42, 86]
list2 = [3, 6, 7, 98, 13, 45]

for i in list1:
    for j in list2:
        print(i, j)
```

# Iteration and Functions


It's often useful to combine loops with functions. For example: convert a
list of temperatures from Fahrenheit to Celsius:

``` {.python .numberLines}
def celsius(f):
    return (f - 32) * (5 / 9)

farenheit = [32, 81, 95, 21]

for f in farenheit:
    print(f, celsius(f)
```

#

::: left
**less_than_prev** takes a list **l** and returns the first element of **l** that is less than the list element before it.
:::

``` {.python .numberList}
def less_than_prev(l):
    last = None
    found = None
    for n in l:
        if last is not None and n < last:
            found = n
            break
        last = n
    return found

less_than_prev([8, 21, 42, 29, 85, 51, 432])
```

::: fragment
29
:::

# Continue


