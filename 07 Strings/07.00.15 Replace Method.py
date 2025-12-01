"""Method replace() replaces all occurrences of a given substring with another one. Syntax s.replace(old, new) takes the string s and replaces all occurrences of substring old with the substring new.

You can pass the third argument count using replace() method, like this: s.replace(old, new, count). If the third argument is passed, only first count occurrences are replaced."""

print('a bar is a bar, essentially'.replace('bar', 'pub'))
print('a bar is a bar, essentially'.replace('bar', 'pub', 1))