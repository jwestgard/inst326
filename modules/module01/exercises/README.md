---
title: "Module 1 Lab Exercise"
permalink: index.html
css: ../../css/page.css
---
 
## Learning Outcomes

- Be able to install Python
- Understand the difference between shell/command line and interactive mode
- Know how to use type(), help(), and dir() to discover built-in functionality
- Use conditionals to control output
- Use string methods to format output

## Practice with the Command Line

- Open a text file and enter:

```{.python .numberLines}
print("Hello World")
```
- Save the file as hello.py
- Open a terminal (search for cmd on Windows, terminal on Mac)
- execute your program as follows:

```{.numberLines}
$ python3 hello.py
# NOTE: You must specify the *path* to your program file
```
   
## Practice with Python's Interactive Mode

- Enter interactive mode by typing "python", "python3", or "python.exe" in the console.  You should see something like this:

```{.numberLines}
$ python3
Python 3.7.0 (default, Jul 23 2018, 20:22:55) 
[Clang 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

- Create a variable 's' and assign a string to it
- Use type(), dir(), and help() to discover information about your string

```{.python .numberLines}
s = "Open the pod bay doors, Hal"

# check the type of the variable s
type(s)

# see a list of string methods
dir(s)

# see built-in help on string objects
help(str) 
```

## Challenges

1. Write a program that takes a two-character string representing the day of the week (mo, tu, we, th, fr, sa, su) as input and uses a conditional to output "Happy [day of week]!":

```{.numberLines}
enter day: mo
Happy Monday!
```

2. Write a "banner printing" program that takes a string as input and outputs the string in uppercase, surrounded by a box made of stars. When run the output should look like this:

```{.numberLines}
Enter text for banner: It's full of stars
**********************
* IT'S FULL OF STARS *
**********************
```
