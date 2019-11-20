---
title: Data Visualization
revealjs-url: ../../lib/reveal
theme: inst326
transition: slide
---

## Overview

::: incremental

* This is a big topic
* This lecture will just walk through one hands-on example

:::


## matplotlib

::: incremental

* A library for graphing and plotting of all sorts
* [https://matplotlib.org](https://matplotlib.org)
* installed with pandas and anaconda python
* pip install matplotlib

:::


## Creating a plot with pyplot

``` {.python .numberLines}
# import the library
from matplotlib import pyplot

# create a plot
pyplot.plot()

# display the plot
pyplot.show()
```


## Elements of a basic plot 

::: incremental

* mapping x over y
* adding labels to the axes
* adding labels to the plots
* choosing colors for the plots
* adding a title
* adding a legend

:::


## Examples

``` {.python .numberLines}
from matplotlib import pyplot

# create some data
years = range(2000,2010)
data1 = [90, 85, 27, 36, 84, 99, 73, 56, 49, 79]

pyplot.plot(years, data1)
pyplot.show()
```

## Examples

``` {.python .numberLines}
from matplotlib import pyplot

# create some data
years = range(2000,2010)
data1 = [90, 85, 27, 36, 84, 99, 73, 56, 49, 79]

# plot the data
pyplot.plot(
    years, data1, label='foo', color='green'
    )
pyplot.show()
```

## Examples

``` {.python .numberLines}
years = range(2000,2010)
data1 = [90, 85, 27, 36, 84, 99, 73, 56, 49, 79]
data2 = [25, 50, 12, 26, 24, 29, 22, 26, 35, 50]

pyplot.plot(years, data1, label='foo', color='green')
pyplot.plot(years, data2, label='bar', color='red')

# add labels
pyplot.title(f'Plot some thing over time')	
pyplot.xlabel('year')
pyplot.ylabel('percentage')
pyplot.legend(loc='upper left')
pyplot.show()
```

## Hands-On

Let's practice with some more hands-on examples!

