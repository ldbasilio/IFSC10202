"""
1. Create a python solution that reads a table containing the distansces between cities. Prompt for a From City and a To City, search the table, and print the distance between the cities.

2. Logic
    - The input file, 09.Project Distances.csv, is a conmma separated value file, with the From City in the zeroth colunmn and the To City in the zeroth row.
    - Read the input file and load each line into a row of a two dimensional list.
    - Print the two dimensional list
    - Prompt for a From City
    - Prompt for a To City
    - Search the zeroth column for the From City. Save the index of the row where the city was found.
    - Search the zeroth row for the To City. Save the index of the column where the city was found.
    - If the From City was not found, then display "Invalid From City".
    - If the To City was not found, then display "Invalid To City".
    - If both cities where found, display the From City, To City, and the Distance.
"""

"""
# Copy, paste and save the file below as 09.Project Distances.csv

Cities,Boston,Buffalo,Chicago,Cleveland,Dallas,Denver,Detroit,El Paso,Houston
Boston,0,457,983,639,1815,1991,702,2358,1886
Buffalo,457,0,536,192,1387,1561,252,1928,1532
Chicago,983,536,0,344,931,1050,279,1439,1092
Cleveland,639,192,344,0,1205,1369,175,1746,1358
Dallas,1815,1387,931,1205,0,801,1167,625,242
Denver,1991,1561,1050,1369,801,0,1310,652,1032
Detroit,702,252,279,175,1167,1301,0,1696,1312
El Paso,2358,1928,1439,1746,625,652,1696,0,756
Houston,1886,1532,1092,1358,242,1032,1312,756,0

# Expected Output

    Cities    Boston   Buffalo   Chicago Cleveland    Dallas    Denver   Detroit   El Paso   Houston
    Boston         0       457       983       639      1815      1991       702      2358      1886
   Buffalo       457         0       536       192      1387      1561       252      1928      1532
   Chicago       983       536         0       344       931      1050       279      1439      1092
 Cleveland       639       192       344         0      1205      1369       175      1746      1358
    Dallas      1815      1387       931      1205         0       801      1167       625       242
    Denver      1991      1561      1050      1369       801         0      1310       652      1032
   Detroit       702       252       279       175      1167      1301         0      1696      1312
   El Paso      2358      1928      1439      1746       625       652      1696         0       756
   Houston      1886      1532      1092      1358       242      1032      1312       756         0
Enter From City: Chicago
Enter To City: Houston
Chicago to Houston - 1092 miles
"""

print ("\nCity Distance Program\n")

filename = "09.Project Distances.csv"
distances = []

infile = open(filename, "r")

line = infile.readline()
while line != "":
    line = line.strip()
    row = line.split(",")
    distances.append(row)
    line = infile.readline()

infile.close()

print ("Distance Table\n")

for i in range(len(distances)):
    for j in range(len(distances[i])):
        print ("{:>10}".format(distances[i][j]), end = "")
    print ()

print ()

from_city = input("Enter From City (blank to exit): ")

while from_city != "":
    to_city = input("Enter To City: ")

    from_index = -1
    to_index = -1

    for i in range(1, len(distances)):
        if distances[i][0].lower() == from_city.lower():
            from_index = i

    for j in range(1, len(distances[0])):
        if distances[0][j].lower() == to_city.lower():
            to_index = j

    if from_index == -1:
        print ("Invalid From City")
    if to_index == -1:
        print ("Invalid To City")

    if from_index != -1 and to_index != -1:
        distance = distances[from_index][to_index]
        print (from_city, "to", to_city, "=", distance, "miles")

    print ()
    from_city = input("Enter From City (blank to exit): ")
