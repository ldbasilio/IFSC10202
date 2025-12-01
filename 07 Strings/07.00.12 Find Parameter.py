"""A method is a function that is bound to an object. When a method is called, the method is applied to an object and does some computations related to it. Methods are invoked as object_name.method_name(arguments). For example, in s.find("e") the string method find() is applied to the string s with one argument "e".

The method find() takes a substring as argument and searches for it inside the string on which it's called. The function returns the index of the first occurrence of a substring. If a substring is not found, the method returns -1."""

s = 'Hello'
print(s.find('e'))   # 1
print(s.find('ll'))  # 2
print(s.find('L'))   # -1 (not found)