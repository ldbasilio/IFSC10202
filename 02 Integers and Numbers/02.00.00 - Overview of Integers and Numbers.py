# The division operator / for integers gives a floating-point real number (an object of type float). 
# The exponentiation ** also returns a float when the power is negative:
print(17 / 3)       # gives 5.66666666667
print(2 ** 4)       # gives 16
print(2 ** -2)      # gives 0.25

# There is a special operation for integer division where the remainder is discarded: //. 
# The operation that yields a remainder of such a division looks like %. 
# Both operations always yield an object of type int.
print(17 / 3)       # gives 5.66666666667
print(17 // 3)      # gives 5
print(17 % 3)       # gives 2

#The int() function drops the decimal portion of a floating point number without rounding:
print(int(1.3))     # gives 1
print(int(1.7))     # gives 1
print(int(-1.3))    # gives -1
print(int(-1.7))    # gives -1

# There is also a function round() that performs the usual rounding:
print(round(1.3))   # gives 1
print(round(1.7))   # gives 2
print(round(-1.3))  # gives -1
print(round(-1.7))  # gives -2

# You can also specify the number of decimal digits to round to in the round() function:
print(round(3.14159,2))   # gives 3.14
print(round(3.14159,3))   # gives 3.142
print(round(3.14159,4))   # gives 3.1416

# Floating-point real numbers cannot be represented with exact precision due to hardware limitations. 
# This can lead to cumbersome effects.
print(0.1 + 0.2)    # gives 0.30000000000000004

# Python has many auxiliary functions for calculations with floats. They can be found in the math module. 
# First, we need to import it first by writing the following instruction at the beginning of the program:
import math
# For example, if we want to find a ceiling value for x (the smallest integer not less than x) 
# we call the appropriate function from the math module: math.ceil(x). 
# The syntax for calling functions from modules is always the same: module_name.function_name(argument_1, argument_2, ...)

#There is another way to use functions from modules: to import the certain functions by naming them:
from math import ceil 
x = 7 / 2
y = ceil(x)
print(y)

# Here is the description for some of the functions in the math module:
# floor(x) - Return the floor of x, the largest integer less than or equal to x.
# ceil(x) - Returns the ceiling of x, the smallest integer greater than or equal to x.
# sqrt(x) - Returns the square root of x
# log(x) - With one argument, return the natural logarithm of x (to base e). With two arguments, return the logarithm of x to the given base.
# e - The mathematical constant e = 2,71828...
# sin(x) - Return the sine of x radians
# asin(x) - Return the arcsine of x, in radians
# pi - The mathematical constant π = 3.1415...'''

# We have printed the default format for values. This can be a problem if we want to print several columns of values, 
# since they can vary in length. We can use the .format() method to format values. The general sytax of the .format() method 
# is: 
# {f1}{f2}{f3}".format(variable1, variable2, variable3), 
# where {f1} is the formatting string for variable1, {f2} is the formatting string for variable2, 
# {f3} is the formatting string for variable3. We will go into greater detail about the formatting values at the end of this chapter