---
title: "Module 7 Exercise"
css: ../../../css/page.css
permalink: index.html
---

## Inheritance

Object Oriented Programming provides a way to __reuse__ software. When you reuse __classes__ you often need to adapt it in a particular way by adding or modifying behavior or data. One way of doing this is to create a new class that extends the existing one using the pattern of __inheritance__.

Imagine that you have been using the __Email__ class found in the __enron.py__ that has been uploaded to ELMS in Module 7. You would like the class to provide access to the __Subject__ of the email. But you don’t want to change the behavior of the Email class itself because other people are using it already. Write a new class called __ExtendedEmail__ that provides this additional method __get_subject()__.

## Composition

When you model things using classes in Object Oriented Programming you often find yourself discovering your classes contain multiple types of things that can also be modeled as classes. When your objects contain other objects you use the pattern of __composition__ to define your classes.

Download __pizza.py__ that has been uploaded to ELMS in Module 7. The Pizza class is being used by a restaurant that doesn’t like to put more than 7 toppings on pizzas. Update the __add_topping()__ method to print out a warning when a user tries to add more than 7 toppings.
