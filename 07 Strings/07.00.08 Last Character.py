"""If the index in the slice s[i] is greater than or equal to len(s) or less than -len(s) the following error occurs:

IndexError: string index out of range.

So it's a bad idea to ask Python to print(s[100]) for a short string like s = "Good Morning".

For such string, there is no 101-th symbol (never forget any indexing in Python starts at 0; the first symbol always has index 0)."""

s = "Good Morning"
print(len(s))
# The last character is the length of the string minus 1
last = len(s) - 1
print(last)
print(s[last])