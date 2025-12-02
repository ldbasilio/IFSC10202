"""
Suppose that two numbers are given: the number of rows of n and the number of columns m. You must create a list of size n×m, filled with zeros. You can do this by appending a list with a lenght of m.
"""

n = 3
m = 4
a = []
for i in range(n):
    a.append([0] * m)
print(a)