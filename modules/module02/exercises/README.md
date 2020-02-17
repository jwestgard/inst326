---
title: Module 2 Exercises
permalink: index.html
css: ../../../css/page.css
---

## Question 1

What error message do you get when you run this program (hint: there are at least two problems)

``` {.python .numberLines}
def get_energy(mass):
    speed_of_light = 300000000
    return mass * speed_of_light ** 2

weights = [1, 100, .5, .75]

while weights:
    joules = get_energy(kg)
    print(kg, "kg is equal to ", joules, "joules")
```

What output do you see when you fix it? In your own words describe what you did to fix this problem in the text box in ELMS.


## Question 2

Write a program that will let you enter a word or phrase and then tell you many
characters long it is. The program should allow the user to keep entering words
and phrases until they enter "quit".

Here's what a sample run might look like:

``` {.python .numberLines}
Enter a word/phrase: python
That is 6 characters long

Enter a word/phrase: holy coding, batman!
That is 20 characters long

Enter a word/phrase: quit
Bye!
```

Save your program in a text file and upload it to ELMS.

## Challenge

An additional task for those who complete the above questions and want to challenge themselves:

- Write a function called "is_prime()" that takes an integer as an input parameter and returns True if the integer is a prime number, False if it is not. 
- **Hint**: a prime number is defined as an integer greater than 1 that is evenly divisible by only itself and one.
- Use your function inside a loop to find the 1000th prime number in the series of all primes.
