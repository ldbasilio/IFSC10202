# Let's finally learn how to sum the integers from 1 to n inclusively.
# Remember: the maximum value in range(min_value, max_value), the 
# max_valueis not included! To make i running from 1 to n inclusive, 
# the maximum value in range() should be n + 1, not simply n.

sum = 0
n = input("Enter a number:")
for i in range(1, n + 1):
    sum += i
    # this ^^ is the shorthand for
    # sum = sum + i
print(sum)
