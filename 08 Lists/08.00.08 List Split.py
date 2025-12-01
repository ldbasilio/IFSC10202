"""
List items can be given in one line separated by a character; in this case, the entire list can be read using input(). You can then use a string method split(), which returns a list of strings resulting after cutting the initial string by spaces. You can also specify a seperator other than a space.
"""

s = "a, b, c"
a = s.split(",")
for i in range(len(a)):
	print (a[i])