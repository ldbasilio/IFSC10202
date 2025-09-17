# Create a program that displays the following pattern for a given height
# Hint: Practice for this assignment by completing the 04.07 Ladder exercise

print ("This program takes a user-inputted number, and creates a pattern with it.")

x = int(input("Enter the maximum length: "))

for i in range(1, x + 1):
    print ("*" * i)

for i in range (x - 1, 0, -1):
    print ("*" * i)