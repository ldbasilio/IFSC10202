"""
We want to tell you several ways of creating and reading lists. First of all, you can create an empty list (the list with no items, its length is 0), and you can add items to the end of your list using append. For example, suppose the program receives the number of elements in the list n, and then n elements of the list one by one each at the separate line. Look at the example of input data in this format.
"""

a = [] # create an empty list
n = int(input()) # read number of element in the list
for i in range(n): 
    new_element = int(input()) # read next element
    a.append(new_element) # add it to the list
print(a)