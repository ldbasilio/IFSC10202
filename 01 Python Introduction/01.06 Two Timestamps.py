#This is the Title Text. (used to assign the result of print, but would return "none")
stampOneTitle = "First Timestamp"
print(stampOneTitle)
print(f"Enter info for the {stampOneTitle.upper()}")

#This helps read the first timestamp variables as integers.
a = int(input("Enter Hours: ")) 
b = int(input("Enter Minutes: ")) 
c = int(input("Enter Seconds: ")) 

#This was optional, but I wanted to keep this string version of the data just in case.
stampOne = [str(a), str(b), str(c)]

stampTwoTitle = "Second Timestamp"
print(stampTwoTitle)
print(f"Enter info for the {stampTwoTitle.upper()}")

#This reads the second timestamp variables as integers.
d = int(input("Enter Hours: "))
e = int(input("Enter Minutes: "))
f = int(input("Enter Seconds: "))

stampTwo = [str(d), str(e), str(f)]

#This helps convert both timestamps into its total in seconds.
total1 = a * 3600 + b * 60 + c
total2 = d * 3600 + e * 60 + f

#Since the first timestamp has been stated to come BEFORE the second timestamp, normal subtraction has been shown to be okay.
#Also, it turns out that "abs()" is a good way to make the data more "order-agnostic."
result = abs(total2 - total1)

print(f"The difference in seconds for both timestamps is {result}")
