"""
Often, tasks have to store rectangular data table. Such tables are called matrices or two-dimensional arrays. In Python any table can be represented as a list of lists (a list, where each element is in turn a list). For example, here's the program that creates a numerical table with two rows and three columns, and then makes some manipulations with it
"""

#Example 1
a = [1, 2, 3, 4]
b = [5, 6]
c = [7, 8, 9]
d = []
d.append(a)
d.append(b)
d.append(c)
print (d)
print(d[0])
print(d[1])
print(d[2])
print(d[0][0])
print(d[0][1])
print(d[0][2])
print(d[0][3])
print(d[1][0])
print(d[1][1])
print(d[2][0])
print(d[2][1])
print(d[2][2])
d[0][0] = 10
d[0][1] = 11
d[0][2] = 12
d[0][3] = 13
print(d[0][0])
print(d[0][1])
print(d[0][2])
print(d)

# Copy, paste and run the above code as 09.00.00 Two Dimensional Lists.py

#The first element — a[0] — is a list of numbers [1, 2, 3]. The elements of the two dimensional array are:

a[0][0] == 1  
a[0][1] == 2  
a[0][2] == 3  
a[1][0] == 4  
a[1][1] == 5  
a[2][0] == 6  
a[2][1] == 7  
a[2][2] == 8

# Note that if you try to access a[1][2], you will get an index out of range error, because the element does not exist.