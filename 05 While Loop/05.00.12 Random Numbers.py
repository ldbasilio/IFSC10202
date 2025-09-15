# Random Numbers:
# Random numbers are often used to simulate game playing. Python has two 
# functions to generate random numbers.

# Random Integers
# You can import the randint function from the random library. In the randint 
# function, you provide a range for the random integers. If you want to simulate 
# roling of a dice with 6 sides, you would use:

from random import randint
x = randint(1,6)
 
# which would give you a random value between 1 and 6 inclusive

# Random Floating Point Numbers
# Sometimes you need a random multiplier, which is a random floating point 
# number between 0 and 1. This is generated using the random function with 
# no arguments, which is imported from the random library.

from random import random
x = random()