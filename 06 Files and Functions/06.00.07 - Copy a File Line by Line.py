"""
This program is an example of copying one file to another. Note the following:

- The file names are string. You can use strings in your program or even prompt the user for the file name
- You will have to open the output file for writing
- When you read a line from the input file, the end of the string already has a linefeed it it. You don't have to append another 
    linefeed when you write the to the output file
- Be sure to close all of your open files
"""

# The name of the file can be a string
inputfilename = "06.00.00 DemoText.txt"
outputfilename = "06.00.07 NewDemoText.txt"
recordcount = 0
# Open the input file for reading
inputfile = open(inputfilename, 'r')
# Open the output file for writing
outputfile = open(outputfilename, 'w')  
# Read the first line of the input file
line = inputfile.readline()
# Read until the input is empty
while line != '':
# Write to the output file
# Note that line already contains a linefeed character,
# so we don't have to add one when we write it.
     outputfile.write(line)
     recordcount += 1
# Read the next line of the input file
     line = inputfile.readline()
# End of File on input file
# Close both files
inputfile.close()
outputfile.close()
print("{} records written".format(recordcount))