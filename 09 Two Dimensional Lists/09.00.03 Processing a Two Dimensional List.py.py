"""
To process 2-dimensional list, you typically use nested loops. The first loop iterates through the row number, the second loop runs through the elements inside of a row. For example, that's how you display two-dimensional numerical list on the screen line by line, separating the numbers with spaces. Notice how you use the len(a), which is the number of rows in the array, and len(a[i]), which is the number of elements in that particular row:
"""

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

# This is how you can use 2 nested loops to calculate the sum of all the numbers in the 2-dimensional list:

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print("The sum is: {}".format(s))