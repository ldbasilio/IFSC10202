# A key function for working with files in Python is the open() statement. The open() statement takes two parameters: filename, and mode.

# There are four different modes for opening a file:
# "r" - Read - Default value. Opens a file for reading, an error occurs if the file does not exist
# "a" - Append - Opens a file for appending (adding data to the end of a file), creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist; overwrites all data already in the file.
# "x" - Create - Creates the specified file, returns an error if the file exists

# # In addition you can specify if the file should be handled as binary or text mode:
# "t" - Text - Default value. File has letters and numbers; each line terminated with a linefeed
# "b" - Binary - Binary mode (e.g. images). File has unprintable characters, such as photos videos, and sound files.