---
title: "Module 7 Exercises"
css: ../../../css/page.css
permalink: index.html
---

## Inheritance

Object Oriented Programming provides a way to _reuse_ software. When you reuse _classes_ you often need to adapt it in a particular way by adding or modifying behavior or data. One way of doing this is to create a new class that extends the existing one using the pattern of _inheritance_.

Imagine that you have been using the _Email_ class found in the _enron.py_ that has been uploaded to ELMS in Module 7. You would like the class to provide access to the _Subject_ of the email. But you don’t want to change the behavior of the Email class itself because other people are using it already. Write a new class called _ExtendedEmail_ that provides this additional method _get\_subject()_.

## Composition

When you model things using classes in Object Oriented Programming you often find yourself discovering your classes contain multiple types of things that can also be modeled as classes. When your objects contain other objects you use the pattern of _composition_ to define your classes.

Download _pizza.py_ that has been uploaded to ELMS in Module 7. The Pizza class is being used by a restaurant that doesn’t like to put more than 7 toppings on pizzas. Update the _add\_topping()_ method to print out a warning when a user tries to add more than 7 toppings.
