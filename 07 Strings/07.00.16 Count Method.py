"""This method count() counts the number of occurrences of one string within another string.

The simplest form is this one: s.count(substring). Only non-overlapping occurrences are taken into account.

If you specify three parameters s.count(substring, left, right), the count is performed within the slice s[left:right]."""

print('Abracadabra'.count('a'))   # this will print '4'
print(('aaaaaaaaaa').count('aa')) # and this will print '5'
print('A sailor went to sea to see what he could see, but all he could have see, was sea, sea, sea'.count('se', 25, -3))