---
title: "Module 5 Tutorial"
css: ../../css/page.css
---

## Regular Expressions: A Step-by-Step Tutorial

### Module import

The re (regular expressions) module is part of the standard library, but must be imported to be available in your program.

``` {.python .numberLines}
import re```

### Pattern Declaration

Regular expression patterns are declared as strings.  Python has a special type of string (an r-string) that has been designed for use in regexes.  The advantage of r-strings is that you do not have to escape all the characters that would otherwise need to be escaped in a regular string.

The following pattern matches 'Sherlock' exactly.

``` {.python .numberLines}
import re

pattern = r'Sherlock'```

### Applying the Pattern

In order to apply this expression you need to do two additional things:

1. locate some text to search
2. choose a function with which to apply the pattern

For this exercise download a copy of the [Adventures of Sherlock Holmes](holmes.txt). Save the file in the folder with the python file you are using for this tutorial.

Next, in your program you'll need to read the contents of the file into a variable in order to search it.

``` {.python .numberLines}
import re

pattern = r'Sherlock'

with open('holmes.txt') as handle:
    text = handle.read() ```

Now you can apply your pattern to the text. The re.search() function is good for many use-cases. Search() takes two arguments, the pattern and the text to search.

``` {.python .numberLines}
import re

pattern = r'Sherlock'

with open('holmes.txt') as handle:
    text = handle.read() 

hit = re.search(pattern, text)
print(hit) ```

Search() is good for finding a match within a block of text, and the match object returns, in addition to the text of the match, its position in the source text (both beginning and ending by offset).  If you want to find multiple occurances of the match, it is often easier to use either findall() or finditer().

#### re.findall()

The syntax of findall() is the same as search() but this function returns the text of *all matches* as a list.  This is useful for counting matches. Can you use this to count the number of occurances of "Sherlock Holmes" in our sample text?

#### re.finditer()

Finditer() is particularly useful if you need to find all matches of a pattern, and also need to perform some processing on the matches. It returns an iterable set of match objects which you can process one-by-one.  Can you use re.finditer() to find all numbers in our source text, convert them to integers, and calculate their sum?
