"""If you call find() with three arguments s.find(substring, left, right), the search is performed inside the s[left:right] slice. If you specify only two arguments, like s.find(substring, left), the search is performed in the slice s[left:], that is, starting with the character at index left until the end of a string. Method s.find(substring, left, right) returns the absolute index (an index in the whole string s, and not in the slice)."""

s = 'my name is bond, james bond, okay?'
print(s.find('bond'))
print(s.find('bond', 12))