---
title: Module 1 Exercises
css: ../css/page.css
---
 
## Learning Outcomes

- Be able to install Python
- Understand the difference between shell/command line and interactive mode
- Know how to use type(), help(), and dir() to discover built-in functionality
- Use conditionals to control output
- Use string methods to format output

## Command Line

- search for cmd on Windows, terminal on Mac

## Create your first program

- Open a text file and enter:

```print('Hello World')```

- Save the file as hello.py
- Open a terminal and execute the program with

```$ python3 hello.py
   # NOTE: You must specify the *path* to your program file```
   
## Interactive Mode

```$ python3
Python 3.7.0 (default, Jul 23 2018, 20:22:55) 
[Clang 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> ```

- Create a variable 's' and assign a string to it

```$ s = "Open the pod bay doors, Hal"```

- Discover information about your string with type(), help(), and dir()

## Challenges

1. Write a program that takes a two-character string representing the day of the week (mo, tu, we, th, fr, sa, su) as input and uses a conditional to output "Happy <day of week>!":

```enter day: mo
Happy Monday!```

2. Write a "banner printing" program that takes a string as input and outputs the string in uppercase, surrounded by a box made of stars. When run the output should look like this:

```Enter text for banner: It's full of stars
**********************
* IT'S FULL OF STARS *
**********************```
