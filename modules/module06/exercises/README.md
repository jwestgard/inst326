---
title: "Module 6 Exercises"
css: ../../../css/page.css
---

## Background

The [Enron Email Dataset](https://www.cs.cmu.edu/~./enron/) is a body of approximately 500,000 email messages from top executives in the [Enron Corporation](https://en.wikipedia.org/wiki/Enron), a Texas-based energy company which after going bankrupt in 2001 was revealed to have engaged in massive accounting fraud. The email dataset became evidence in the ensuing investigation, and subsequently was released into the public domain.

## Task: Email Message Class

1. The task is to create a class called Email() that can be used to analyze the  [provided sample of the dataset](../module05/enron-sample.zip).
2. Each instance of your class will represent a single email message, and should have the following attributes:
    - sender: the email address in the "From:" line;
    - recipients: a list of all email addresses in the "To:" line;
    - date: a datetime object derived from the string in the "Date:" line;
    - text: the full text of the message
3. Create a loop that scans a directory in the sample and creates Email objects from each message.
4. Create another loop that writes the sender, date, and recipients data to a CSV file.
