---
title: Module 3 Lab Worksheet
permalink: index.html
css: ../../css/page.css
---

The following activities are designed to give you some practice with basic 
Python data structures, and to start thinking about combining individual 
components into a larger program.

Choose one of the following tasks, uploading your code (.py file) through the submission form on ELMS.

## Grouped-Frequency Word Counter

Create a function that takes a string as input, splits the string into words, and returns a dictionary representing the frequency counts of the words in the input string. For example:

``` {.python .numberLines}
text = "to be or not to be"
frequency(text)

# The function called above should return this dictionary:
{'to': 2, 
 'be': 2,
 'or': 1,
 'not': 1
 }
```

**Note**: the order of the key-value pairs being returned is not significant since dictionary items are not sorted.

Once you have a working function, implement the following additional requirements:

1. Write an interface that prompts the user to enter text and returns the frequency counts.
2. Write a second function that sorts the frequency counts in order of most frequent.  **HINT**: Converting the key value pairs to a list of tuples with the count first and the key second is one way to accomplish this task.
3. Add a "stopwords" feature that allows the user to supply a list of words to be ignored in the frequency counts. This concept is commonly used in word clouds to prevent "the" and "a", for example, from being displayed as the largest words.


## Hangman Game

The task is to implement a word guessing game on the model of "Hangman". The game starts with a hidden word in which hyphens are displayed in place of letters. The player guesses a letter, and if the letter is in the word, the word display is updated to reveal the letter in place.  If the word does not contain the letter guessed, the player gets one "strike".  

**NOTE**: you do not need to implement the drawing of the hanged man, as in the children's game.  

If the player gets five strikes before all letters are revealed, the player loses.  If the player is able to guess all letters before getting five strikes, the player wins.

Your program should do the following:

1. Include a function that take a word and list of letters guessed and returns a string that displays the letters guessed only, with hyphens in place of letters not guessed.  **HINT**: You can loop over the letters in a word and concatenate a new word from letters and hyphens depending on whether a given letter is present in a list of letters guessed.
2. Display the letters guessed so far to the user.
3. Be able to handle user input in either uppercase or lowercase.
4. Allow the user to quit the game by typing "quit".
