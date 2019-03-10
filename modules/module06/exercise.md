---
title: "Module 6: Object-Oriented Programming Exercise"
css: ../../css/page.css
---

## Background

In the previous module recall that we used a sample of the [Enron Email Dataset](https://www.cs.cmu.edu/~./enron/). We will use the same sample for this exercise, to see how a custom class can facilitate working with data.

## Task: Email Message Class

1. The task is to create a class called Email() that can be used to analyze the  [provided sample of the dataset](enron-sample.zip).
2. Each instance of your class will represent a single email message, and should have the following attributes:
    - sender: the email address in the "From:" line;
    - recipients: a list of all email addresses in the "To:" line;
    - date: a datetime object derived from the string in the "Date:" line;
    - text: the full text of the message
3. Create a loop that scans a directory in the sample and creates Email objects from each message.
4. Create another loop that writes the sender, date, and recipients data to a CSV file.
