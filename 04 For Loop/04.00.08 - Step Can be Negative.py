# To iterate over a decreasing sequence, we can use the extended 
# form of range() with three arguments — range(start_value, end_value, step). 
# When omitted, the step is implicitly equal to 1. However, it can be any 
# non-zero value. The loop always includes start_value and excludes end_value during iteration:

for i in range(10, 0, -2):
    print(i)
