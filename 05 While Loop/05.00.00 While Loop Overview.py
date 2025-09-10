# The while loop repeats the sequence of actions many times until some condition evaluates to False. 
# The condition is given before the loop body and is checked before each execution of the loop body. Typically, the while loop is 
# used when it is impossible to determine the exact number of loop iterations in advance.

'''The syntax of the while loop in the simplest case looks like this:
while some condition:
    a block of statements'''

# Python first checks the condition. If it is False, then the loop is terminated and control is passed to the next statement after the while loop body. 
# If the condition is True, then the loop body is executed, and then the condition is checked again. This continues while the condition is True. Once the 
# condition becomes False, the loop terminates and control is passed to the next statement after the loop.

# For example, the following program fragment prints the squares of all integers from 1 to 10. Here one can replace the while loop by the for ... in range(...) loop:
i = 1
while i <= 10:
    print(i ** 2)
    i += 1

# In this example, the variable i inside the loop iterates from 1 to 10. Such a variable whose value changes with each new loop iteration is called a counter. 
# Note that after executing this fragment the value of the variable i is defined and is equal to 11, because when i == 11 the condition i <= 10 is False for the first time.
# Here is another example use of the while loop to determine the number of digits of an integer n:
n = int(input("Enter a Number: "))
length = 0
while n > 0:
    n //= 10  # this is equivalent to n = n // 10
    length += 1
print(length)

# On each iteration we cut the last digit of the number using integer division by 10 (n //= 10). In the variable length we count how many times we did that.
# In Python there is another, easier way to solve this problem: length = len(str(i)).

# One can write an else: statement after a loop body which is executed once after the end of the loop:
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Loop ended, i =', i)

# At the first glance, this statement doesn't seem to have sense, because the else: statement body can just be put after the end of 
# the loop. The else statement after a loop only has sense when used in combination with the instruction break. If during the execution 
# of the loop Python interpreter encounters a break, it immediately stops the loop execution and exits out of it. In this case, 
# the else: branch is not executed. So, a break is used to abort the loop execution during the middle of any iteration.

# Here is a Black Jack-like example: a program that reads numbers and sums it until the total gets greater or equal to 21. The input 
# sequence ends with 0 for the program to be able to stop even if the total sum of all numbers is less than 21.
# Let's see how it behaves on the different inputs.
# Scenario 1. The loop is exited normally after checking the condition, so the else branch is executed.
# Scenario 2. The loop is aborted by break, so the else branch is skipped.
total_sum = 0
a = int(input("Enter a Number: "))
while a != 0:
    total_sum += a
    if total_sum >= 21:
        print('Total sum is', total_sum)
        break
    a = int(input())
else:
    print('Total sum is less than 21 and is equal to', total_sum, '.')
# Else branch can also be used with the for loop. Let's look at the example when a program reads 5 integers but stops right when 
# the first negative integer is met.

# Scenario 1. The loop is exited normally, so the else branch is executed.
# Scenario 2. The loop is aborted, so the else branch isn't executed.
for i in range(5):
    a = int(input("Enter a Number: "))
    if a < 0:
        print('Met a negative number', a)
        break
else:
    print('No negative numbers met')

# Another instruction used to control the loop execution is continue. If Python interpreter meets continue somewhere in the 
# middle of the loop iteration, it skips all the remaining instructions and proceeds to the next iteration.
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# If the break and continue are placed inside several nested loops, they affect only the execution of the innermost one. 
# Let's look at rather silly example to demonstrate it:
for i in range(3):
    for j in range(5):
        if j > i:
            # breaks only the for on line 2
            break
        print(i, j)

# The instructions break and continue are discouraged, if you can implement your idea without using them. Here is a 
# typical example of a bad usage of the break: this code counts the number of digits in an integer.
n = int(input("Enter a Number: "))
length = 0
while True:
    length += 1
    n //= 10
    if n == 0:
        break
print('Length is', length)

# It's cleaner and easier-to-read to rewrite this loop with a meaningful loop condition:
n = int(input())
length = 0
while n != 0:
    length += 1
    n //= 10
print('Length is', length)

# In Python it is possible for a single assignment statement to change the value of several variables. Let's see:
a, b = 0, 1
# The effect demonstrated above code can be written as:
a = 0
b = 1
# The difference between the two versions is that multiple assignment changes the values of two variables simultaneously.

# Multiple assignment is useful when you need to exchange (swap) the values of two variables. In older programming languages without 
# the support of multiple assignment this can be done using the auxiliary variable:
a = 1
b = 2
tmp = a
a = b
b = tmp
print(a, b)

# In Python, the same swap can be written in one line:
a = 1
b = 2
a, b = b, a
print(a, b)

# The left-hand side of "=" should have a comma-separated list of variable names. The right-hand side can be any expressions, 
# separated by commas. The left-hand side and the right-hand side lists should be of equal length.

# Random numbers are often used to simulate game playing. Python has two functions to generate random numbers.

# You can import the randint function from the random library. In the randint function, you provide a range for the 
# random integers. If you want to simulate roling of a dice with 6 sides, you would use:
from random import randint
x = randint(1,6)
# which would give you a random value between 1 and 6 inclusive

# Sometimes you need a random multiplier, which is a random floating point number between 0 and 1. This is generated using 
# the random function with no arguments, which is imported from the random library.
from random import random
x = random()

