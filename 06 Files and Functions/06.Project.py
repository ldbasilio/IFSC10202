"""
Create a python solution that merges the contents of two files into a new file.
- Open 06.Project Output File.txt for writing
- Open and read 06.Project Input File.txt, copying lines from 06.Project Input File.txt to 06.Project Output File.txt line by line. Keep a count 
of the number of input records and output records.
- Inspect each line of the input file for the text: **Insert Merge File Here**
- At this point, open 06.Project Merge File.txt, copying lines from 06.Project Merge File.txt to 06.Project Output File.txt line by line. Keep a 
count of the number of merge records and output records.
- At the end of 06.Project Merge File.txt, continue copying lines from 06.Project Input File.txt to 06.Project Output File.txt line by line. Keep 
a count of the number of input records and output records.
- Close all files
- Print the number of records in the input file, merge file, and output file.
"""

projIn = "06.Project Input File.txt"
projMer = "06.Project Merge File.txt"
projOut = "06.Project Output File.txt"

inputRecords = 0 
mergeRecords = 0 
outputRecords = 0

output = open(projOut, "w")
input = open(projIn, "r")

for line in input:
    if "**Insert Merge File Here**" in line:
        merge = open(projMer, "r")
        for mergeLine in merge:
            output.write(mergeLine)
            mergeRecords += 1
            outputRecords += 1
        merge.close()
    else:
        output.write(line)
        inputRecords += 1
        outputRecords += 1

output.close()
input.close()

print(f"{inputRecords} input file records")
print(f"{mergeRecords} merge file records")
print(f"{outputRecords} output file records")