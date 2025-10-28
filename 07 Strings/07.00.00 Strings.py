#Overview of Strings: 
# A string can be read from the standard input using the fucntion "input()" or defined in single of double quotes. Two strings can be concatenated, and we also repeat a string n times, multiplying by an integer. 

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
# There are three forms of slices. The simplest form of the slice: a single character slice S[i] gives it character of the string. We count the charcters starting from point 0. That is, if S = 'Hello', S[0] == 'H', S[1] == 'e', S[2] == 'l', S[3] == 'l', S[4] == 'o'. Note that in Python there is no separate type for characters of the string. S[i] also has the type str, just as the source string. The number i in S[i] is called an index. If you specify a negative index, then it is counted from the end, starting with the number -1. That is, S[-1] == 'o', S[-2] == 'l', S[-3] == 'l', S[-4] == 'e', S[-5] == 'H'. Let's summarize it in the following table:

# Example 4
"""
String S |   H   |   e   |   l   |   l   |   o   |
Index    |  S[0] |  S[1] |  S[2] |  S[3] |  S[4] |
Index    | S[-5] | S[-4] | S[-3] | S[-2] | S[-1] |
"""
# If the index in the slice S[i] is greater than or equal to len(S), or less than -len(S), the following error is caused:
# IndexError: string index out of range.

#Slices: Substring 
# Slice with two parameters S[a:b] returns the substring of length b - a, starting with the character at index and lasting until the character at index b, not including the last one. For example, S[1:4] == 'ell', and you can get the same substring using S[-4:-1]. You can mix positive and negative indexes in the same slice, for example, S[1:-1] is a substring without the first and the last character of the string (the slice begins with the character with index 1 and ends with an index of -1, not including it). Slices with two parameters never cause IndexError. For example, for S == 'Hello' the slice S[1:5] returns the string 'ello', and the result is the same even if the second index is very large, like S[1:100]. If you omit the second parameter (but preserve the colon), then the slice goes to the end of string. For example, to remove the first character from the string (its index is 0) take the slice S[1:]. Similarly if you omit the first parameter, then Python takes the slice from the beginning of the string. That is, to remove the last character from the string, you can use slice S[:-1]. The slice S[:] matches the string S itself.

#Slices: Subsequence
# If you specify a slice with three parameters S [a : b : d ], the third parameter specifies the step, same as for function range(). In this case only the characters with the following index are taken: a, a + d, a + 2 * d,... and so on, until and not including the character with index b. If the third parameter equals to 2, the slice takes every second character, and if the step of the slice equals to -1, the characters go in reverse order. For example, you can reverse a string like this: S[::-1]. Let's see the examples:

# Example 5
"""
s = 'abcdefg'
print(s[1])     #b
print(s[-1])    #g
print(s[1:3])   #bc
print(s[1:-1])  #bcdef
print(s[:3])    #abc
print(s[2:])    #cdefg
print(s[:-1])   #abcdef
print(s[::2])   #aceg
print(s[1::2])  #bdf
print(s[::-1])  #gfedcba
"""
# Note how the third parameter of the slice is similar to the third parameter of the function range()

# Example 6
"""
s = 'abcdefghijklm'
print(s[0:10:2])
for i in range(0, 10, 2):
    print(i, s[i])

Result:
acegi
0 a
2 c
4 e
6 g
8 i
"""

#String methods: find() and rfind() 
# A method is a function that is bound to the object. When the method is called, the method is applied to the object and does some computations related to it. Methods are invoked as object_name.method_name(arguments). For example, in s.find("e") the string method find() is applied to the string s with one argument "e". The find() method searches a substring, passed as an argument, inside the string on which it's called. The function returns the index of the first occurrence of the substring. If the substring is not found, the method returns -1.

# Example 7
"""
s = 'Hello'
print(s.find('e'))
print(s.find('ll'))
print(s.find('L'))

Result:
1
2
-1
"""
# Similarly, the rfind() method returns the index of the last occurrence of the substring.

# Example 8
""""
s = 'abracadabra'
print(s.find('b'))
print(s.rfind('b'))

Result:
1 
8
"""
# If you call find() with three arguments s.find(substring, left, right), the search is performed inside the slice s[left:right]. If you specify only two arguments, like s.find(substring, left), the search is performed in the slice s[left:], that is, starting with the character at index left to the end of the string. Method s.find(substring, left, right) returns the absolute index, relatively to the whole string s, and not to the slice.

# Example 9
"""
s = 'my name is bond, james bond, okay?'
print(s.find('bond'))
print(s.find('bond', 12))

Result:
11
23
"""

#String method: replace() 
# Method replace() replaces all occurrences of a given substring with another one. Syntax: s.replace(old, new) takes the string s and replaces all occurrences of substring old with the substring new.

# Example 10
"""
print('a bar is a bar, essentially'.replace('bar', 'pub'))

Result:
a pub is a pub, essentially
"""
# One can pass the third argument count, like this: s.replace(old, new, count). It makes replace() to replace only first count occurrences and then stop.

# Example 11
"""
print('a bar is a bar, essentially'.replace('bar', 'pub', 1))

Result:
a pub is a bar, essentially
"""

#String methods: count()
# This method counts the number of occurrences of one string within another string. The simplest form is this one: s.count(substring). Only non-overlapping occurrences are taken into account:

# Example 12
"""
print('Abracadabra'.count('a'))    # 4
print(('aaaaaaaaaa').count('aa'))  # 5
"""
# If you specify three parameters s.count(substring, left, right), the count is performed within the slice s[left:right].

#Remove Leading and Trailing Whitspace
# To remove leading and trailing whitespace from a string, use the strip method: mystring = mystring.strip()

#Upper Case
# To convert a string to upper case, use the upper method: mystring = mystring.upper()

#Lower Case
# To convert a string to lower case, use the lower method: mystring = mystring.lower()

#Remove a Line Feed (when reading a file)
# To remove the line feed character at the end of string during a readline: mystring = mystring.replace("\n","")

#Summary of String Methods
"""
*Method
- Definition

'capitalize()`
- Converts the first character to upper case

'casefold()`
- Converts string into lower case

'center()`
- Returns a centered string

'count()`
- Returns the number of times a specified value occurs in a string

'encode()`
- Returns an encoded version of the string

'endswith()`
- Returns true if the string ends with the specified value

'expandtabs()`
- Sets the tab size of the string

'find()`
- Searches the string for a specified value and returns the position of where it was found

'format()`
- Formats specified values in a string

'index()`
- Searches the string for a specified

'isalnum()`
- Returns True if all characters in the string are alphanumeric

'isalpha()`
- Returns True if all characters in the string are in the alphabet

'isdecimal()`
- Returns True if all characters in the string are decimals

'isdigit()`
- Returns True if all characters in the string are digits

'isidentifier()`
- Returns True if the string is an identifier

'islower()`
- Returns True if all characters in the string are lower case

'isnumeric()`
- Returns True if all characters in the string are numeric

'isprintable()`
- Returns True if all characters in the string are printable

'isspace()`
- Returns True if all characters in the string are whitespaces

'istitle()`
- Returns True if the string follows the rules of a title

'isupper()`
- Returns True if all characters in the string are upper case

'join()`
- Joins the elements of an iterable to the end of the string

'ljust()`
- Returns a left justified version of the string

'lower()`
- Converts a string into lower case

'lstrip()`
- Returns a left trim version of the string - removes whitespace (blanks, tabs, conrol characters)

'maketrans()`
- Returns a translation table to be used in translations

'partition()`
- Returns a tuple where the string is parted into three parts

'replace()`
- Returns a string where a specified value is replaced with a specified value

'rfind()`
- Searches the string for a specified value and returns the last position of where it was found

'rindex()`
- Searches the string for a specified value and returns the last position of where it was found

'rjust()`
- Returns a right justified version of the string

'rpartition()`
- Returns a tuple where the string is parted into three parts

'rsplit()`
- Splits the string at the specified separator, and returns a list

'rstrip()`
- Returns a right trim version of the string - removes whitespace (blanks, tabs, conrol characters)

'split()`
- Splits the string at the specified separator, and returns a list

'splitlines()`
- Splits the string at line breaks and returns a list

'startswith()`
- Returns true if the string starts with the specified value

'strip()`
- Returns a trimmed version of the string - removes whitespace (blanks, tabs, conrol characters)

'swapcase()`
- Swaps cases, lower case becomes upper case and vice versa

'title()`
- Converts the first character of each word to upper case

'translate()`
- Returns a translated string

'upper()`
- Converts a string into upper case

'zfill()`
- Fills the string with a specified number of 0 values at the beginning
"""
# Example 1
print("Example 1")
print('>_< ' * 5)  # >_< >_< >_< >_< >_<
 
# Example 2
print("Example 2")
print(len('abcdefghijklmnopqrstuvwxyz'))
# 26
 
# Example 3
print("Example 3")
s = str(2 ** 100)
print(s)  
# 1267650600228229401496703205376
print(len(s))
# 31
 
# Example 4
print('Example 4')
s='Hello'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
 
# Example 5
print('Example 5')
s = 'abcdefg'
print(s[1])     #b
print(s[-1])    #g
print(s[1:3])   #bc
print(s[1:-1])  #bcdef
print(s[:3])    #abc
print(s[2:])    #cdefg
print(s[:-1])   #abcdef
print(s[::2])   #aceg
print(s[1::2])  #bdf
print(s[::-1])  #gfedcba
 
# Example 6 
print('Example 6')
s = 'abcdefghijklm'
print(s[0:10:2])
for i in range(0, 10, 2):
    print(i, s[i])
    
# Example 7 
print("Example 7")
s = 'Hello'
print(s.find('e'))   # 1
print(s.find('ll'))  # 2
print(s.find('L'))   # -1
 
# Example 8
print('Example 8')
s = 'abracadabra'
print(s.find('b'))  # 1
print(s.rfind('b')) # 8
 
# Example 9
print('Example 9')
s = 'my name is bond, james bond, okay?'
print(s.find('bond'))     # 11
print(s.find('bond', 12)) # 23
 
# Example 10
print('Example 10')
print('a bar is a bar, essentially'.replace('bar', 'pub'))  # 'a pub is a pub, essentially'
 
# Example 11
print('Example 11')
print('a bar is a bar, essentially'.replace('bar', 'pub', 1)) # 'a pub is a bar, essentially'
 
# Example 12
print('Example 12')
print('Abracadabra'.count('a'))    # 4
print(('aaaaaaaaaa').count('aa'))  # 5