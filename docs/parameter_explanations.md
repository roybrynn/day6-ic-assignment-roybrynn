# How-To-Guide

The How-To-Guide dives deeper into the types of things you can do with each function to gain experience in Python. It generally explains the parameters and the range of possible use cases for each function.

### [`my_adder`](adder.md)

Here is a deeper explanation of how `my_adder` can be used. 

To start, the three numeric values `a`, `b`, and `c` that are input to the function can be any sort of floating point or integer value. The inputs can be negative, positive, or 0. The function automatically casts inputs to float for consistency. 

```python
a = float
b = float
c = float
```

We can pass these values to the `my_adder` function:

```python
ans = my_adder(a,b,c)
```

The `my_adder` function adds the three values `a`, `b`, and `c`. This means that the expected output is `a + b + c`. For further reference on summation, please visit the following [link](https://en.wikipedia.org/wiki/Summation). This function can be used for anytime the programmer wants to add three numeric values.


### [`has_digits`](digits.md)

Here is a deeper explanation of how `has_digits` can be used. 

To start, the text string value `string` can be any input of type `str`. The inputs can contain spaces and utilize special characters.

```python
string = str
```

We can pass this value to the `has_digits` function:

```python
ans = has_digits(string)
```

The `has_digits` function uses the built-in `.isdigit()` function from Python. This function takes a single character and determines if the character is a digit or not and returns either `1` or `0` as a binary indicator for the precense of digits. For further reference on the `.isdigit()` function, please visit the following [link](`.isdigits()` function). This function can be used for anytime the programmer wants to check for the presence of a numeric character in a string of text.

### [`my_thermostat`](thermostat.md)

Here is a deeper explanation of how `my_thermostat` can be used. 

To start, the two numeric values `current_temperature` and `desired_temperature` are input to the function and can be any sort of floating point or integer value. The inputs can be negative, positive, or 0. The function automatically casts inputs to float for consistency. 

```python
current_temperature = float
desired_temperature = float
```

We can pass these values to the `my_thermostat` function:

```python
ans = my_thermostat(current_temperature,desired_temperature)
```

The `my_thermostat` function determines the action the 'thermostat' should take given the two temperatures. This happens by comparing the current and desired temperatures. If the current and desired temperatures have a difference of 5 degrees or more, than the thermostat indicates an action- either "Heat" or "AC". In the case where there current and desired temperature are within 5 degrees of one another, the the function returns "Off". This function can be used to mimic the behavior of a thermostat and compare different temperatures. 