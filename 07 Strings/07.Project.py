"""
Create a python solution that reads a file containing angles in degrees, minutes, seconds format (DD°MM'SS"), converts the value to a decimal degree value, then write the values to a file.

To simplify you code, you will need to create the following functions:
    ParseDegreeString(ddmmss) - inputs a location value and returns the degrees, minutes, and seconds.
        Inputs
            ddmmss - inputs a string in the form of dd°mm'ss" and returns the degrees, minutes, and seconds.
        Returns
            Degrees - Floating Point
            Minutes - Floating Point
            Seconds - Floating Point
        Logic
            - Find the degree symbol (chr(176)) - degrees are between the beginning of the string and the position of the degree symbol.
            - Find the minutes symbol (') - minutes are between the degree symbol and the minute symbol.
            - Find the seconds symbol(") - seconds are between the minutes symbol and the seconds symbol.
            - Return the degrees, minutes, and seconds as floating point.
    DDMMSStoDecimal(degrees, minutes, seconds) - inputs degrees, minutes, and seconds and converts to a decimal value.
        Inputs
            - Degrees - Floating Point
            - Minutes - Floating Point
            - Seconds - Floating Point
        Returns
            - Decimal Degrees - Floating Point
        Logic
            - There are 60 minutes in a degree and 3600 seconds in a degree. Calculate the decimals degrees as degrees plus minutes divided by 60 plus seconds divided by 3600.

Copy, paste and save the file below as 07.Project Angles Input.txt
55°00'00"
55°30'00"
55°59'59"
55°60'00"
56°00'00"
5°0'0"

# Expected Output
6 records processed

# Expected 07.Project Angles Output.txt
55.0
55.5
55.999722222222225
56.0
56.0
5.0
"""

def ParseDegreeString(ddmmss):
    deg_symbol = chr(176)
    min_symbol = "'"
    sec_symbol = '"'

    deg_pos = ddmmss.find(deg_symbol)
    min_pos = ddmmss.find(min_symbol)
    sec_pos = ddmmss.find(sec_symbol)

    deg_str = ddmmss[0:deg_pos]
    min_str = ddmmss[deg_pos + 1:min_pos]
    sec_str = ddmmss[min_pos + 1:sec_pos]

    degrees = float(deg_str)
    minutes = float(min_str)
    seconds = float(sec_str)

    return degrees, minutes, seconds

def DDMMStoDecimal(degrees, minutes, seconds):
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    return decimal

print ("\nAngles Conversion Program\n")

infile = open("07.Project Angles Input.txt", "r")
outfile = open("07.Project Angles Output.txt", "w")

record_count = 0

line = infile.readline()
while line != "":
    line = line.strip()

    if line != "":
        deg, mins, secs = ParseDegreeString(line)
        decimal_angle = DDMMStoDecimal(deg, mins, secs)

        outfile.write(str(decimal_angle) + "\n")

        record_count += 1

    line = infile.readline()

infile.close()
outfile.close()

print (str(record_count) + " records processed")