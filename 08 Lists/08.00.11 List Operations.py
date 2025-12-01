"""
You can easily do many different operations with lists.

1. "x in A" - Check whether an item in the list. Returns True or False.
2. "x not in A" - The same as not(x in A).
3. "mini(A)" - The smallest element of list.
4. "max(A)" - The largest element of list. 
5. "A.index(x)" - The index of the first occurrence of element x in the list; in its absense generates an exception ValueError.
6. "A.count(x)" - The number of occurrences of element x in the list.
"""

a = [2, 3, 5, 8, 13, 5, 5]
# Check to see that 8 is in the list
if 8 in a:
	print("8 is in the list")
# Check to see if 15 is not in the list
if 15 not in a:
	print("15 is not in the list")
# Print the maximum of the list
print(max(a))
# Print the minumum of the list
print(min(a))
# Print the index of the element that has a value of 13
print (a.index(13))
# Print the number of occurrance of the value 5
print (a.count(5))