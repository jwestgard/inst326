---
title: "Module 5 Exercises"
css: ../../../css/page.css
permalink: index.html
---

## Background

Regular Expressions are particularly useful for processing large amounts of textual data to find patterns, for example to find email addresses, phone numbers, or social security numbers. In the archival profession, a common use-case for locating personally-identifiable information is to redact it when making content available to researchers.

The [Enron Email Dataset](https://www.cs.cmu.edu/~./enron/) is a body of approximately 500,000 email messages from top executives in the [Enron Corporation](https://en.wikipedia.org/wiki/Enron), a Texas-based energy company that, after having gone bankrupt in 2001, was revealed to have engaged in massive accounting fraud. The email dataset became evidence in the ensuing investigation, and subsequently was released into the public domain.

## PII finder

- The task is to create a tool for locating personally identifiable information in the [provided sample of the dataset](enron-sample.zip).

- Create a function that takes a string to be searched as an argument, and that uses a regular expression to find patterns in the text matching the form of social security numbers (XXX-XX-XXXX). Your function should return a match object.

- Create a loop that scans a directory tree and calls your function on each file in the tree. If matches are returned, the loop should report the source and location of each match.
