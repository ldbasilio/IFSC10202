"""If you specify a slice with three parameters S[a:\b:d], the third parameter specifies the step, same as for function range(). In this case only the characters with the indexes a., a + d, a + 2 * d,... and so on are taken, until character with index b is reached and, as usual, not including it. For instance, if the third parameter is equal to 2, the slice takes every second character.

We want to tell you the fun fact: if the step of the slice equals to -1, the characters go in reverse order. :) You can reverse a string S with this: S[::-1]."""

s = 'abcdefg'
print(s[1])
print(s[-1])
print(s[1:3])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])
 
s = 'abcdefghijklm'
print(s[0:10:2])
for i in range(0, 10, 2):
    print(i, s[i])