---
title: Module 2 Lab Worksheet
permalink: index.html
css: ../../../css/page.css
---
 
## Learning Outcomes

- Learn to use the Python turtle module
- Practice functions and loops by drawing shapes in turtle

## Python's Turtle Module

- Turtle is easiest to learn when controlled interactively
- For an overview of available commands, [see the documentation](https://docs.python.org/3.7/library/turtle.html)
- Open a terminal/command prompt and launch Python (by tyting py, python.exe, python, or python3 depending on your system)
- Interactive mode should show this prompt: ">>>"

### Create a Turtle object called testudo

```{.python .numberLines}
import turtle
testudo = turtle.Turtle()
```

### Move testudo around to draw a square

```{.python .numberLines}
testudo.forward(200)
testudo.left(90)
testudo.forward(200)
testudo.left(90)
testudo.forward(200)
testudo.left(90)
testudo.forward(200)
testudo.left(90)
```
- Notice how this shape consists of the same steps repeated 4 times

### Make this into a function

- First define a function
- Note that in interactive mode you have to be careful not to hit enter more than once inside your function definition or python will think your function is finished

```{.python .numberLines}
def square(t, length):
  for x in range(4):
      t.forward(200)
      t.left(90)
```

- Next, you need to call your function, passing in the testudo object and the length of a side

```{.python .numberLines}
square(testudo, 200)
```

- By now your screen might be getting cluttered, so to start again you can break out of the interactive session with CTRL-D or exit()
- When you restart python interactively, use up/down arrows to scroll through your command history in order to save some typing


## Challenge

1. Write a function called polygon() that takes two parameters, sides and length.
2. Sides represents the number of sides (3 is a triangle, 4 is a square, etc.)
3. Length represents the length of a single side
4. Note that for any polygon the interior angles will add up to 360
5. This means that a generic polygon function can compute the interior angle by dividing 360 by the number of sides (a square has 4 sides and 360/4 = 90)

