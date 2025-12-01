"""Slices with two parameters never cause IndexError. For example, for s == 'Hello' the slice s[1:5] returns the string 'ello', and the result is the same as if the second index was very large, like s[1:100].

If you omit the second parameter (but preserve the colon), then the slice continues until the end of a string. For example, to remove the first character from a string (its index is 0) take the slice s[1:]. Similarly, if you omit the first parameter (s[:7]), then Python takes the slice, starting at the beginning of a string. That is, to remove the last character from a string, you can use slice s[:-1]. The slice s[:] is equal to a string s itself."""

s = 'Hello'
print(s[1:5])    
print(s[1:100])  
print(s[1:])     
print(s[:-1])    
print(s[:])
