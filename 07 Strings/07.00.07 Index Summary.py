"""
String S |   H   |   e   |   l   |   l   |   o   |
Index    |  S[0] |  S[1] |  S[2] |  S[3] |  S[4] |
Index    | S[-5] | S[-4] | S[-3] | S[-2] | S[-1] |"""

s="Hello"
print("Hello Forward")
for i in range(0, len(s)):
	print(s[i])
 
print("Hello Backward")
for i in range(-1, -len(s)-1, -1):
	print(s[i])