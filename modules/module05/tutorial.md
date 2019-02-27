---
title: "Module 5 Tutorial"
css: ../../css/page.css
---

# Regular Expressions: Step-by-Step Tutorial

## Module import

The re (regular expressions) module is part of the standard library, but must be imported to be available in your program.

``` {.python .numberLines}
import re
```

## Pattern Declaration

Regular expression patterns are declared as strings.  Python has a special type of string (an r-string) that has been designed for use in regexes.  The advantage of r-strings is that you do not have to escape all the characters that would otherwise need to be escaped in a regular string.

The following pattern matches 'Sherlock' exactly.

``` {.python .numberLines}
import re

pattern = r'Sherlock'
```

## Applying the Pattern

In order to apply this expression you need to do two additional things:

1. locate some text to search
2. choose a function with which to apply the pattern

For this exercise download a copy of the [Adventures of Sherlock Holmes](holmes.txt). Save the file in the folder with the python file you are using for this tutorial.

Next, in your program


