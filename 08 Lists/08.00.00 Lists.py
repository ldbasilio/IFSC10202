"""
Most of programs work not only with variables. They also use lists of variables. For example, a program can handle an information about students in a class by reading the list of students from the keyboard or from a file. A change in the number of students in the class must not require modification of the program source code.

Previously we have already faced the task of processing elements of a sequence — for example, when computing the largest element of the sequence. But we haven't kept the whole sequence in computer's memory. However, in many problems it is necessary to keep the entire sequence, like if we had to print out all the elements of a sequence in ascending order ("sort a sequence").

To store such data, in Python you can use the data structure called list (in most programming languages the different term is used — “array”). A list is a sequence of elements numbered from 0, just as characters in the string. The list can be set manually by enumerating of the elements the list in square brackets, like here:
"""

Primes = [2, 3, 5, 7, 11, 13]
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

"""
The list Primes has 6 elements, namely: Primes[0] == 2, Primes[1] == 3, Primes[2] == 5, Primes[3] == 7, Primes[4] == 11, Primes[5] == 13. The list Rainbow has 7 elements, each of which is a string.

Like the characters in the string, the list elements can also have negative index, for example, Primes[-1] == 13, Primes[-6] == 2. The negative index means we start at the last element and go left when reading a list.

* Printing a List
You can obtain the number of elements in a list with the function len (meaning length of the list), e.g. len(Primes) == 6. Unlike strings, the elements of a list are changeable; they can be changed by assigning them new values.
"""

# Example 1
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Rainbow[0])
Rainbow[0] = 'red'
print('Print the rainbow')
for i in range(len(Rainbow)):
    print(Rainbow[i])

"""
* Creating a List
Consider several ways of creating and reading lists. First of all, you can create an empty list (the list with no items, its length is 0), and you can add items to the end of your list using append. For example, suppose the program receives the number of elements in the list n, and then n elements of the list one by one each at the separate line. Here is an example of input data in this format:
"""

5
1809
1854
1860
1891
1925

# In this case, you can organize the reading from such list as follows:

# Example 2
print()
print("Example 2")
a = [] # start an empty list
# read number of element in the list
n = int(input("Enter Number of Elements in List:")) 
for i in range(n):
	new_element = int(input("Enter a Number:"))  # read next element
	a.append(new_element)                        # add it to the list
for i in range(len(a)):
    print("Element {} = {}".format(i, a[i]))

"""
* Concatenation and Multiplication
There are several operations defined for lists: list concatenation (addition of lists, i.e. "gluing" one list to another) and repetition (multiplying a list by a number). For example:
"""

# Example 3
a = [1, 2, 3]
b = [4, 5]
c = a + b
d = b * 3
print(c)
print(d)
print([7, 8] + [9])
print([0, 1] * 3)

"""
The resulting list c will be equal to [1, 2, 3, 4, 5], and a list of d will be equal to [4, 5, 4, 5, 4, 5]. This allows you to organize the process of reading lists differently: first, consider the size of the list and create a list from the desired number of elements, then loop through the variable i starting with number 0 and inside the loop read i-th element of the list:
"""

a = [0] * int(input("Enter Number of Elements in List"))
for i in range(len(a)):
    a[i] = int(input("Enter an Element"))

"""
* More on Printing Lists
You can print elements of a list a with print(a); this displays the list items surrounded by square brackets and separated by commas. By formatting the value, you can print all the elements in one line or one item per line. Here are two examples of that, using other forms of loop:
"""

# Example 4
a = [1, 2, 3, 4, 5]
# Print all the values on a single line
for i in range(len(a)):
    print(a[i], " ", end="")
print()
# Print all the values one per line
for i in range(len(a)):
    print(a[i])

"""
* Split Method
List items can be given in one line separated by a character. If you run this program with the input data of 1 2 3, the list a will be equal to ['1', '2', '3']. Please note that the list will consist of strings, not of numbers. If you want to get the list of numbers, you have to convert the list items one by one to integers:
"""

# Example 5
a = "1 2 3"
b = a.split()
for i in range(len(b)):
    b[i] = int(b[i])
for i in range(len(b)):
    print(b[i])

"""
The method split() has an optional parameter that determines which string will be used as the separator between list items. For example, calling the method split('.') returns the list obtained by splitting the initial string where the character '.' is encountered:
"""

# Example 6
a = '192.168.0.1'.split('.')
for i in range(len(a)):
    print(a[i])

"""
* Join Method
In Python, you can display a list of strings using one-line commands. For that, the method join is used; this method has one parameter: a list of strings. It returns the string obtained by concatenation of the elements given, and the separator is inserted between the elements of the list; this separator is equal to the string on which is the method applied. We know that you didn't understand the previous sentence from the first time. :) Look at the examples:
"""

a = ['red', 'green', 'blue']
print(' '.join(a))    # prints red green blue
print('***'.join(a))  # prints red***green***blue

"""
* Generators
To create a list filled with identical items, you can use the repetition of list, for example:
"""

n = 5
a = [0] * n
print(a)

"""
* List Slices
With lists and strings, you can do slices. Namely:

A[i:j]     # slice j-i elements A[i], A[i+1], ..., A[j-1].
A[i:j:-1]  # slice i-j elements A[i], A[i-1], ..., A[j+1] (that is, changing the order of the elements).
A[i:j:k]   # cut with the step k: A[i], A[i+k], A[i+2*k],... . If the value of k<0, the elements come in the opposite order.

Each of the numbers i or j may be missing, what means “the beginning of line” or “the end of line" Lists, unlike strings, are mutable objects: you can assign a list item to a new value. Moreover, it is possible to change entire slices. Here we received a list [1, 2, 3, 4, 5], and then try to replace the two elements of the slice A[2:4] with a new list of three elements. The resulting list is as follows: [1, 2, 7, 8, 9, 5].
"""

A = [1, 2, 3, 4, 5]
A[2:4] = [7, 8, 9]
print(A)

"""
And here, the resulting list will be [40, 2, 30, 4, 20, 6, 10]. The reason is, A[::-2] is a list of elements A[-1], A[-3], A[-5], A[-7], and that elements are assigned to 10, 20, 30, 40, respectively.

If a discontinuous slice (i.e. a slice with a step k, k > 1) is assigned a new value, then the number of elements in the old and new slices necessarily coincide, otherwise error ValueError occurs. Note that A[i] is a list item, not a slice!
"""

A = [1, 2, 3, 4, 5, 6, 7]
A[::-2] = [10, 20, 30, 40]
print(A)

"""
* Operations on Lists
You can easily do many different operations with lists

1. "x in A" - Check whether an item in the list. Returns True or False.
2. "x not in A" - The same as not(x in A).
3. "mini(A)" - The smallest element of list.
4. "max(A)" - The largest element of list. 
5. "A.index(x)" - The index of the first occurrence of element x in the list; in its absense generates an exception ValueError.
6. "A.count(x)" - The number of occurrences of element x in the list.
"""

# Example 1
print()
print("Example 1")
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Rainbow[0])
Rainbow[0] = 'red'
print('Print the rainbow')
for i in range(len(Rainbow)):
    print(Rainbow[i])
    
# Example 2
print()
print("Example 2")
a = [] # start an empty list
# read number of element in the list
n = int(input("Enter Number of Elements in List:"))  
for i in range(n):
	new_element = int(input("Enter a Number:"))  # read next element
	a.append(new_element) # add it to the list    
for i in range(len(a)):
    print("Element {} = {}".format(i, a[i]))
 
# Example 3
print()
print("Example 3")
a = [1, 2, 3]
b = [4, 5]
c = a + b
d = b * 3
print(c)
print(d)
print([7, 8] + [9])
print([0, 1] * 3)
 
# Example 4
a = [1, 2, 3, 4, 5]
# Print all the values on a single line
for i in range(len(a)):
    print(a[i], " ", end="")
print()
# Print all the values one per line
for i in range(len(a)):
    print(a[i])
 
# Example 5
print()
print("Example 5")
a = "1 2 3"
b = a.split()
for i in range(len(b)):
	b[i] = int(b[i])
for i in range(len(b)):
	print(b[i])
 
# Example 6
print()
print("Example 6")
a = '192.168.0.1'.split('.')
for i in range(len(a)):
    print(a[i])
 
# Example 7
print()
print("Example 7")
a = ['red', 'green', 'blue']
print(' '.join(a))    # prints red green blue
print('***'.join(a))  # prints red***green***blue
print('***'.join(a))  # prints red***green***blue