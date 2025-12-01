"""
Did you know that you can read a file from the internet? Quite often, data is saved in ""Plain Textt" fromat, that allows you to read the file from the Internet then process the data, similar to reading a file on your hard drive.

To read a file from the Internet, you must import the "requests" library as shown in the example. You send it the URL of the file you would like to read. This returns a complicated object, that we will discuss in a future chapter. However, you can get the test associated with the file and put it into a python string. Finally, you can split the string by the newline character to give you a nice list, with one line of text in each list item.
"""

import requests
# Read a file from the Internet using GET
response = requests.get('https://example-files.online-convert.com/document/txt/example.txt')
# Get the text string of the response
filestring = response.text
# Split the string by newline character into a list
filestringlist = filestring.split("\n")
# Print the list
for i in range(len(filestringlist)):
    print(filestringlist[i])