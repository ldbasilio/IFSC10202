#Overview of Strings: 
# A string can be read from the standard input using the fucntion "input()" or defined in single of double quotes. 
# Two strings can be concatenated, and we also repeat a string n times, multiplying by an integer. 

# Example 1
print('>_<' * 5) # >_< >_< >_< >_< >_<
# Result: 
# >_< >_< >_< >_< >_<

# Example 2
print(len('abcdefghijklmnopqrstuvwxyz'))
# Result: 
# 26

# Example 3
s = str(2 ** 100)
print(s)
print(len(s))
# Result: 
# 1267650600228229401496703205376
# 31

#Slices:
# A slice yields, from the given string, one character, or some fragment, substring or sequence.

#Slices: Single Character
# There are three forms of slices. The simplest form of the slice: a single character slice S[i] gives it character of the string. 
# We count the charcters starting from point 