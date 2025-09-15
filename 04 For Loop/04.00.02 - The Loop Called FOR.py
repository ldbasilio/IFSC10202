# If you have to do fixed amount of operations — say, sum the 100 first numbers — the for loop saves the day.
# There are for and while loop operators in Python, in this lesson we cover for.
# The for loop iterates over any sequence. Let's see the simplest example of using for. Same as with if-else, indentation is what specifies which instructions are controlled by for.sum = 0

for i in range (1, 101):
    sum = sum + i
print(sum)
