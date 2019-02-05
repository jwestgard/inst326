---
title: "Module 2 Exercise"
css: ../../css/page.css
---

What error message do you get when you run this program (1 point)

``` {.python .numberLines}
def get_energy(mass):
    speed_of_light = 300000000
    return mass * speed_of_light ** 2

weights = [1, 100, .5, .75]

while weights:
    joules = get_energy(kg)
    print(kg, "kg is equal to ", joules, "joules")
```

What output do you see when you fix it? (1 point)

## Extra Credit (1 point)

Can you write a program that will let you enter a word or phrase and tell you
many characters long it is? When the user enters "quit" it should stop.

Here's what a sample run might look like:

```
Enter a word/phrase: python
That is 6 characters long

Enter a word/phrase: holy coding, batman!
That is 20 characters long

Enter a word/phrase: quit
Bye!
```
