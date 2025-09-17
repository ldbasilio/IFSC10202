# Create a program that displays special numbers in a range. A special number 
# is defined to be a number that is the sum of its own digits, each raised to 
# the power of the number of digits.
# - 153 is 3 digits long and is equal to 1^3 + 5^3 + 3^3
# - 8208 is 4 digits long and is equal to 84 + 24 + 04 + 84
# Hint: First, determine the number of digits using a while loop and remainder 
# division by 10. Do not use any string functions or the len function.
# Hint: Recalculate the value using the power from above and see if you get the 
# original value
# Do not use the len function to determine the number of digits.

print ("\nThis program is meant to display a length of 'special numbers' within a range.\n")

x = int(input("Enter Start of Range: "))
y = int(input("Enter End of Range: "))

print ("Special Numbers between " + str(x) + " and " + str(y))

if x > y: 
    x, y = y, x

def count_digits(x):
    length = 0
    max_range = x
    while max_range > 0:
        max_range //= 10
        length += 1
    return length

def is_special(x):
    a = count_digits(x)
    length = 0 
    max_range = x 
    while max_range > 0:
        digit = max_range % 10
        length += digit ** a
        max_range //= 10
    return length == x

specialNum = False

for i in range (x, y + 1):
    if is_special(i):
        print (i)
        specialNum = True

if not specialNum:
    print ("No special numbers were found in this range.")
