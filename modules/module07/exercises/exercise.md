---
title: "Module 7: Inheritance Exercise"
css: ../../css/page.css
---

## Inheritance

Object Oriented Programming provides a way to *reuse* software. When you
reuse *classes* you often need to adapt it in a particular way by adding or
modifying behavior or data. One way of doing this is to create a new class
that extends the existing one using the pattern of *inheritance*.

Imagine that you have been using the *Email* class found in the *enron.py* that
has been uploaded to ELMS in Module 7. You would like the class to provide access to the
*Subject* of the email. But you don't want to change the behavior of the Email
class itself because other people are using it already. Write a new class called 
*ExtendedEmail* that provides this additional method *get_subject()*.

## Composition

When you model things using classes in Object Oriented Programming you often find yourself discovering your classes contain multiple types of things that can also be modeled as classes. When your objects contain other objects you use the pattern of *composition* to define your classes.

Download *pizza.py* that has been uploaded to ELMS in Module 7. The Pizza class is being used by a restaurant that doesn't like to put more than 7 toppings on pizzas. Update the *add_topping()* method to print out a warning when a user tries to add more than 7 toppings.