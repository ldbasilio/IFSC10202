# For Loop With a Range
for i in range(5, 8):
    print(i, i ** 2)
print('End of Loop')

# For Loop (Reduced Form)
for i in range(3):
    print(i)

# For Loop Parameters
x = 4
for i in range(x):
    print('Hello, world!')

# For Loop Empty Sequence
for i in range(-5):
    print("Hello, world!")
print("End of Loop")

# More Complex Example
result = 0
n = 5
for i in range(1, n + 1):
    result += i
    # this ^^ is the "shorthand for"
    # result = result + i
print(result)

# Decreasing Sequence
for i in range(10, 0, -2):
    print(i)
10
8
6
4
2

# More About the Print Function
print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep=", ", end=". ")
print(4, 5, 6, sep=", ", end=". ")
print()
print(1, 2, 3, sep="", end=" -- ")
print(4, 5, 6, sep=" * ", end=".")
