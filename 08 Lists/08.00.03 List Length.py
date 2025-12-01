"""
Most of programs work not only with variables. They also use lists of variables. A program can handle an information about students by reading the list of students from the keyboard or from a file. A change in the number of students in a class must not require modification of the program source code.

We have already faced the task of processing elements of a sequence — for example, when finding the largest element of the sequence. But we haven't kept the whole sequence in computer's memory. However, in many situations it is necessary to keep the entire sequence, like if we had to print out all the elements of a sequence in ascending order ("sort a sequence").

You can obtain the number of elements in a list with the function len (meaning length of the list), e.g. len(primes) == 6.
"""

primes = [2, 3, 5, 7, 11, 13]
print(len(primes))