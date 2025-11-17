"""Recall how indexes work on a string.

String S |   H   |   e   |   l   |   l   |   o   |
Index    |  S[0] |  S[1] |  S[2] |  S[3] |  S[4] |
Index    | S[-5] | S[-4] | S[-3] | S[-2] | S[-1] |
 
If you call slice with two parameters s[a:b], it returns the substring of length b - a, which starts with the character at index a and ends with the character at index b, not including it. For example, if s == 'Hello', s[1:4] == 'ell' (for slice s[1:4] only indexes 1,2 and 3 are included).

You can get the same substring using s[-4:-1] (recall negative indexing starts at the end of a string).

You may mix positive and negative indexes in the same slice: for example, s[1:-1] is exactly the same substring (the slice begins with the character with index 1 and ends with an index of -1, not including it)."""

s = 'Hello'
print(s[1:4])
print(s[-4:-1])
print(s[1:-1])